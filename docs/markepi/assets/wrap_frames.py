from PIL import Image, ImageDraw
import os
import glob

FRAME_PATH = "/Users/osama/Projects/Apple-Screenshots/static/assets/frames/iOS/17 Pro/Silver/frame.png"
SCREENSHOTS_DIR = "/Users/osama/Projects/VisionCrafter/docs/markepi/assets/how-it-works"
OUT_DIR = os.path.join(SCREENSHOTS_DIR, "framed")

SCREEN_X = 100
SCREEN_Y = 100
SCREEN_W = 1206
SCREEN_H = 2622

frame = Image.open(FRAME_PATH).convert("RGBA")
FRAME_W, FRAME_H = frame.size

# Screen mask = the transparent region enclosed by the phone body. The frame is also
# transparent *outside* the body, so inverting alpha would leak the screenshot's square
# corners past the rounded screen — flood fill from the center to get the screen only.
flood = frame.getchannel("A").copy()
ImageDraw.floodfill(flood, (FRAME_W // 2, FRAME_H // 2), 200, thresh=128)
screen_mask = flood.point(lambda v: 255 if v == 200 else 0)

os.makedirs(OUT_DIR, exist_ok=True)
screenshots = sorted(
    p
    for ext in ("png", "PNG", "jpg", "jpeg", "JPG", "JPEG")
    for p in glob.glob(os.path.join(SCREENSHOTS_DIR, f"*.{ext}"))
)

print(f"Processing {len(screenshots)} screenshots...")
print(f"Frame: {FRAME_W}x{FRAME_H}, Screen area: ({SCREEN_X},{SCREEN_Y}) {SCREEN_W}x{SCREEN_H}")

for i, path in enumerate(screenshots):
    ss = Image.open(path).convert("RGBA")

    # Scale screenshot to cover the screen area (aspect-fill)
    ss_ratio = ss.width / ss.height
    screen_ratio = SCREEN_W / SCREEN_H
    if ss_ratio > screen_ratio:
        new_h = SCREEN_H
        new_w = int(ss.width * SCREEN_H / ss.height)
    else:
        new_w = SCREEN_W
        new_h = int(ss.height * SCREEN_W / ss.width)

    ss_scaled = ss.resize((new_w, new_h), Image.LANCZOS)

    # Center-crop to exact screen dimensions
    left = (new_w - SCREEN_W) // 2
    top = (new_h - SCREEN_H) // 2
    ss_cropped = ss_scaled.crop((left, top, left + SCREEN_W, top + SCREEN_H))

    # Create a canvas with the screenshot at screen position, then mask to screen shape
    screenshot_layer = Image.new("RGBA", (FRAME_W, FRAME_H), (0, 0, 0, 0))
    screenshot_layer.paste(ss_cropped, (SCREEN_X, SCREEN_Y))

    # Apply screen mask: only show screenshot where the frame is transparent (the screen area)
    masked_screenshot = Image.new("RGBA", (FRAME_W, FRAME_H), (0, 0, 0, 0))
    masked_screenshot.paste(screenshot_layer, (0, 0), screen_mask)

    # Composite frame on top
    masked_screenshot.paste(frame, (0, 0), frame)

    out = os.path.join(OUT_DIR, os.path.splitext(os.path.basename(path))[0] + ".png")
    masked_screenshot.save(out, "PNG")
    print(f"[{i+1}/{len(screenshots)}] {os.path.basename(out)}")

print("Done.")
