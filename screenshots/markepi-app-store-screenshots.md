# Markepi — App Store Screenshot Plan

> Guidance for the screenshots to submit to the **Apple App Store** for Markepi.
> Optimized for conversion **and** App Review compliance. The first 2–3
> screenshots are ~80% of the decision — they appear in search results before
> anyone taps. Lead with the flagship differentiator and the most visually
> obvious benefit, not a feature tour.

---

## Apple constraints to respect

- **Show the real app UI** (Guideline 2.3.3 — accurate metadata). Marketing text
  overlays and a device frame are fine, but the phone in every frame must display
  an **actual Markepi screen**, not a pure logo/splash. Any "privacy" or concept
  frame must have a real screen behind it.
- **No pricing / "Free" / "Coming soon" text in screenshots.** Prices change and
  Apple can reject for it → **no pricing screenshot.** Price is shown separately on
  the listing.
- **No misleading or overclaimed capability.** Markepi's honest C2PA wording
  ("device signing identity," "signature intact") is an asset — show exactly what
  the app outputs; never imply a verified *legal/personal* identity.
- **Clean status bar** (full signal/battery, neutral time e.g. 9:41), **your own
  photos only** (you are asserting authorship — use images you own), no other-brand
  logos in frame.
- **Sizes:** 6.9" iPhone (1290×2796) is the required set; add **iPad 13"
  (2064×2752)** since the app is iPad-native. Up to 10 per device.
- **First image = search thumbnail:** must read at tiny size and must depict the app.

---

## Shot list (real Markepi screen in every frame)

### The critical first three

1. **Content Credentials — Export Receipt**
   - Screen: the actual "Signed · Signature intact · Certificate trusted · Rights
     embedded" result screen.
   - Overlay: **"Prove it's real. Prove it's yours."**
   - Why: no other consumer iPhone app does on-device C2PA signing. This is the
     moat → must be screenshot #1.

2. **Before / after watermark**
   - Screen: a plain photo → the same photo with an elegant signature/logo + white
     frame, done inside the editor. Use a genuinely beautiful photo you own.
   - Overlay: **"Your mark, beautifully placed."**
   - Why: communicates what the app does with zero reading.

3. **White frame + auto EXIF caption**
   - Screen: the gallery frame with a real auto-filled caption
     (e.g. "Shot on iPhone 16 Pro · 24mm · f/1.8 · 1/125 · ISO 100").
   - Overlay: **"Captions fill themselves in."**
   - Why: recognizable and aspirational to photographers; very screenshot-friendly.

### Next tier

4. **The live editor + layers**
   - Screen: the editor with the tool dock (Text · Logo · Sign · Frame · Layers)
     and stacked layers visible.
   - Overlay: **"A full watermarking studio."**

5. **Video / Live Photo watermarking**
   - Screen: the editor over a video with the frame scrubber on screen.
   - Overlay: **"Photos, video & Live Photos."**
   - Why: rare capability — worth calling out.

6. **Hand-drawn signature**
   - Screen: the signing canvas (Apple Pencil).
   - Overlay: **"Sign in your own hand."**

7. **Batch processing**
   - Screen: the batch thumbnail strip with real thumbnails + progress
     ("12 of 12 processed").
   - Overlay: **"Mark a whole set at once."**

8. **On-device privacy — shown through UI**
   - Screen: the metadata-privacy picker, or the "verify incoming Content
     Credentials" screen (a real screen carries the claim, so it stays compliant).
   - Overlay: **"On-device. No account. No cloud."**

### Optional closer

9. **Retro date stamp**
   - Screen: the warm-orange film "databack" date result.
   - Overlay: **"That film-camera look."**

---

## Production tips (help review + conversion)

- Put the text overlay in the **top third**, real device screen below — highest-
  converting layout and Apple-safe.
- Reuse **one gorgeous hero photo** across frames 2, 3, and 5 for cohesion.
- Capture at **native resolution** from a real device/simulator so the UI is
  pixel-crisp (no upscaling).
- Keep captions **≤ 5 words** and inside the safe area for both iPhone and iPad crops.
- If you can, make an **App Preview video** — before/after watermarking animates
  really well.

---

## Handoff to the website

When the final screenshots are exported, drop them into
`docs/markepi/assets/` and the placeholder device-frames on the Markepi landing
page (`docs/markepi/index.html`) can be swapped for the real shots.
