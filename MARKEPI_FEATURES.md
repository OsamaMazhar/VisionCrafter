# Markepi — Marketing & Feature Reference Document

> Website source-of-truth for the Markepi product page(s) on orbitaar.com.
> Companion to `MARKETING_FEATURES.md` (SyncAlbum). Covers every feature — major
> and minor — plus step-by-step tutorials and the product philosophy, written so
> it can be lifted directly into landing-page copy, a user guide, an App Store
> description, blog posts, and structured data.

---

## The One-Line Pitch

**Markepi is a privacy-first watermarking and photo-provenance studio for iPhone and iPad. Add text, logos, hand-drawn signatures, elegant white frames, and retro date stamps to your photos, videos, and Live Photos — and cryptographically sign them with tamper-evident Content Credentials (C2PA) that prove they're yours — then share anywhere, without ever saving a copy to your device.**

---

## The Problem

Watermarking on a phone is usually a mess. You want to put your name, logo, or signature on a photo before you post it — to protect your work, to brand it, or just to make it look finished. But the typical flow is painful:

- You export the photo out of Photos, into some editor.
- The editor saves a **duplicate** to your camera roll (now you have two copies to manage).
- Most watermark apps **strip your metadata** — your GPS location, capture date, camera info, and, critically, the **HDR gain map** that makes modern iPhone photos look vivid. Your beautiful HDR shot comes out flat.
- Videos and Live Photos are usually not supported at all, or they lose their audio and motion.
- Free apps push their **own** watermark onto your image, or lock every useful control behind a subscription wall.
- Many of them quietly **upload your photos to a server** to do the processing. You have no idea where your images went.
- And when AI-generated imagery is everywhere, there's **no easy way to prove a photo is genuinely yours** or to declare how it was made.

You just want to stamp your mark on something and send it — without duplicates, without losing quality, without handing your photos to a stranger's cloud, and without a monthly bill for a one-second edit.

**Markepi fixes all of this.**

---

## What Markepi Does

Markepi is a complete, on-device watermarking studio. Pull media in from **Photos** or the **Files** app (or via the **Share sheet** from any other app), stack up your watermark layers in a live preview, and send the finished result **directly to wherever you want it** — Messages, Mail, Instagram, AirDrop, Files, or back to Photos — **without a mandatory local save step**.

It handles **photos, videos, and Live Photos**, preserves **all** of your original metadata (including HDR), never uploads anything, requires no account, and offers a genuinely usable free tier.

And uniquely for a phone app, it can seal **Content Credentials (C2PA)** into your exports — cryptographically signed, tamper-evident proof of who made a photo and how — **the flagship feature that answers the "is this real?" problem of the AI era.**

---

## The Philosophy (put this front and center on the site)

### 1. No data retention. No backend. No account.

Markepi has **no server**. There is no sign-up, no login, no cloud, and no analytics harvesting your images. **Every watermark is rendered entirely on your device** using Apple's native imaging frameworks. Your photos never leave your iPhone or iPad. Nothing is uploaded, cached in a data center, or retained anywhere we can see. When you close the app, there's nothing left on any server, because there is no server.

This is the same privacy stance across all Orbitaar apps: **your photos are yours.**

### 2. A frictionless workflow: from Photos or Files → straight to share, no forced save.

Markepi is built around one core belief: **watermarking should be a pass-through, not a detour.**

- **In:** Pick from the Photos library, import from Files, or send media straight into Markepi from any app via the iOS **Share sheet**.
- **Edit:** Everything happens in a single live editor with an instant preview.
- **Out:** Tap **Share** and send the finished file **directly** to its destination.

You do **not** have to save a copy to your camera roll first. There's no "export to library, then open Instagram, then find the photo, then post" dance. Markepi hands the finished file straight to the iOS share sheet, so you go from original to shared in a few taps — **no duplicate clutter in your photo library**, unless *you* choose to save one.

### 3. Quality and metadata are sacred.

Watermarking should never degrade your photo. Markepi preserves:

- **HDR gain maps** — your HDR photos stay HDR (most watermark apps flatten them).
- **All original metadata** — GPS location, capture date, camera and lens info, color profile, device details.
- **The source format** — a HEIC stays a HEIC, a JPEG stays a JPEG (unless you deliberately convert it).
- **Video and Live Photo integrity** — audio, motion, and metadata are carried through.

### 4. Provenance you can prove — without giving anything up.

Markepi is one of the only consumer apps that lets you attach **Content Credentials (C2PA)** — cryptographically signed, tamper-evident proof of authorship and origin — **entirely on-device**, with a hardware-backed key that never leaves your iPhone. No account, no upload, no cloud signing service. In the age of AI-generated images, this is how an ordinary creator says "this is real, and it's mine" in a way that anyone can verify. **This is the flagship reason to choose Markepi.**

### 5. Fair, honest pricing.

A real free tier that lets you get work done every day, and a one-time **lifetime** unlock for people who don't want subscriptions. No app-branded watermark forced onto your images, ever.

---

## Hero Features (the headline list)

### 1. Text Watermarks
Add your name, brand, handle, or copyright line in a choice of typefaces, with full control over color, opacity, size, and position. Stack multiple text layers.

### 2. Logo / Image Watermarks
Drop in a PNG or image logo from Photos or Files. Add several logos, resize them, set their transparency, and place them anywhere on the image.

### 3. Hand-Drawn Signatures
Sign your work with your finger or Apple Pencil on a real drawing canvas. Adjust ink color and stroke thickness. Your signature renders in your chosen color on the final image.

### 4. Elegant White Frames with Smart Captions
Add a clean white border (the popular "gallery" look) with an **optional caption that auto-fills from your photo's own EXIF data** — camera model, lens, focal length, aperture, shutter speed, ISO, date, dimensions, format, and GPS.

### 5. Retro Date Stamps
Burn a warm, glowing, orange film-camera "databack" date into the corner of your photo, in six authentic formats.

### 6. Photos, Videos **and** Live Photos
Watermark not just still images but full videos (with audio) and Live Photos (with motion). Very few watermark apps do all three.

### 7. HDR & Full-Metadata Preservation
Your HDR gain map, GPS, capture date, camera info, and color profile all survive the watermark. Your photo comes out exactly as good as it went in — just with your mark on it.

### 8. Batch Processing (up to 20 items)
Load a whole set, apply one watermark configuration to all of them, and export the entire batch at once — with **per-photo overrides** when a single image needs something different.

### 9. ⭐ Content Credentials (C2PA) — Prove Your Work Is Yours *(flagship)*
The headline feature. **Cryptographically sign your photos on-device** with tamper-evident **Content Credentials** (the open C2PA standard behind Adobe, the BBC, Sony, Nikon, and Leica). Embed IPTC rights metadata, declare how the image was made (camera, AI, AI-edited, composite), preserve any existing provenance, and get a verifiable **Export Receipt** — all with a Secure Enclave key that never leaves your device. In an era where you can't tell real from AI, Markepi lets an everyday creator assert authenticity that anyone can verify. *(See the dedicated deep-dive below.)*

### 10. Share-Anywhere Workflow with No Forced Save
Send the finished file straight to any app or destination through the iOS share sheet — no mandatory copy to your library, no duplicates.

### 11. Reusable Templates
Save any watermark setup as a named template and apply it instantly to future photos. Build your look once, reuse it forever.

### 12. Adaptive, Beautiful Editor (Portrait & Landscape)
A modern Liquid-Glass interface that reshapes itself for portrait and landscape, with a live preview at every step. Fully accessible (Dynamic Type, VoiceOver, Reduce Motion/Transparency) and available in light, dark, or system appearance.

---

## The Editor at a Glance

The editor is organized around a **tool dock** with six tools:

| Tool | What it does |
|------|--------------|
| **Text** | Add and style text watermark layers |
| **Logo** | Add image/logo watermark layers |
| **Sign** | Draw a signature watermark |
| **Frame** | Add a white frame with an optional EXIF caption |
| **Layers** | Reorder, hide/show, adjust, and delete all watermark layers |
| **More** | Output format & quality, templates, Content Credentials, metadata privacy |

Above the tools you'll find the chrome: **Back**, **Settings**, **Add photos**, **Import from Files**, **Reset overrides** (in batch mode), and the prominent blue **Share** button. When you load more than one item, a **batch strip** of thumbnails appears so you can move between photos. The dock and strip run along the bottom in portrait and re-flow into side rails in landscape, so the photo always gets maximum space.

---

## Detailed Features & Step-by-Step Tutorials

### Getting media into Markepi

Markepi accepts media three ways:

**A) From the Photos library**
1. Launch Markepi (or tap **Add photos** in the editor toolbar).
2. The system photo picker appears.
3. Select up to **20** photos and/or videos (it matches images, videos, and Live Photos).
4. Tap **Add**. Your media loads into the editor with a live preview.

**B) From the Files app**
1. Tap **Import from Files** (the folder icon).
2. Browse to any image, movie, or audiovisual file.
3. Select it — it opens directly in the editor.

**C) From another app via the Share sheet (the fast path)**
1. In **Photos**, or any app that can share an image/video, tap the **Share** button.
2. Choose **Markepi** from the share sheet.
3. Markepi opens with your media already loaded, ready to watermark.
   *(The Share extension hands the media to the main app instantly — you go from "I found a photo" to "I'm watermarking it" in two taps, without saving anything first.)*

> **Tip:** If you already have photos loaded and add more, Markepi asks whether to **Add to Batch** or **Replace Current** — so you never lose work by accident.

---

### Tool 1 — Text Watermarks

Add styled text — your name, your studio, a copyright line, or your social handle.

**To add a text watermark:**
1. Tap **Text** in the tool dock.
2. Tap the **"Enter your watermark text"** field and type your text (e.g. `© Jane Doe 2026`).
3. Choose a **Font** from the font picker (the default is *Pacifico*, a friendly script that reads like a signature; other typefaces cover serif, sans-serif, script, and monospace looks).
4. Tap the **Color** swatch to pick any color for the text.
5. Drag the **Opacity** slider to set how bold or subtle the mark is (0–100%).
6. Set the **Position** using the nine-point grid (see *Positioning* below).
7. Resize the text with the scale control — it's sized as a fraction of the image so it looks right on any resolution (the default is a tasteful ~4.5% of image height).

**To add more than one text layer:**
- Tap **Add Another Text**. Each text layer is independent — its own words, font, color, opacity, size, and position. Stack a copyright line at the bottom and a big brand name in the center, for example.

---

### Tool 2 — Logo / Image Watermarks

Brand your photos with a logo, monogram, or any image (transparent PNGs work beautifully).

**To add a logo:**
1. Tap **Logo** in the tool dock.
2. Tap **Add Logo**.
3. Choose the source:
   - **From Photos** — pick a logo image from your library.
   - **From Files** — pick a logo file (e.g. a transparent PNG) from Files.
4. The logo appears on your photo in the live preview.
5. Adjust:
   - **Scale** — resize the logo (relative to the image, so it stays proportional on any output size).
   - **Opacity** — make it a bold stamp or a faint watermark.
   - **Position** — snap it to any of the nine positions.

**To add multiple logos:**
- Tap **Add another logo** to stack more image layers (e.g. a logo in one corner and a "verified" badge in another).

---

### Tool 3 — Hand-Drawn Signatures

Sign your work by hand — the personal touch that a font can't replicate.

**To add a signature:**
1. Tap **Sign** in the tool dock.
2. Tap **Add Signature** to open the drawing canvas.
3. **Draw your signature** with your finger or **Apple Pencil**. The canvas gives you a clear, high-contrast surface to write on.
4. Adjust before you commit:
   - **Ink Color** — choose the color your signature will actually render in on the photo.
   - **Thickness** — set the stroke width for a fine pen or a bold marker look.
5. Place and size it like any other layer (**Position**, **Scale**, **Opacity**).
6. Use **Remove** if you want to redraw.

> **Note:** The canvas draws in a high-contrast color so you can see what you're writing, but your signature renders in the **ink color you chose** (white is a common choice for a subtle mark on darker photos).

---

### Tool 4 — White Frame with Smart EXIF Caption

The clean, gallery-style white border — with an optional caption that fills itself in from your photo's own shooting data.

**To add a white frame:**
1. Tap **Frame** in the tool dock.
2. Toggle **White Frame** on. A crisp white border appears around your photo.
3. *(Optional)* Turn on the **caption** to print information beneath the image.
4. Choose which fields to include — Markepi reads them straight from the photo's EXIF metadata and renders them in a fixed, tasteful order:
   - **Camera / Device** (e.g. *iPhone 16 Pro*)
   - **Lens**
   - **Focal length**
   - **Aperture**
   - **Shutter speed**
   - **ISO**
   - **Date**
   - **Dimensions**
   - **Format**
   - **GPS**
5. Tick only the fields you want. The caption assembles automatically — no typing required.

This is perfect for photographers who want that "shot on…" info card look without manually copying numbers out of their camera app.

---

### Tool 5 — Retro Date Stamp

Recreate the nostalgic look of a film camera's databack — the warm orange, slightly glowing date burned into a corner.

**To add a date stamp:**
1. Open the date-stamp control (in the Frame/More area).
2. Toggle the **Date Stamp** on.
3. Pick a **format** — six authentic styles:
   - `DD MM YYYY` — spaced, classic databack default (e.g. `24 06 2026`)
   - `DD-MM-YYYY` — day-first, dashed
   - `YYYY-MM-DD` — ISO order, sortable
   - `MM-DD-YYYY` — month-first (US)
   - `'YY MM DD` — two-digit year with apostrophe (most authentic point-and-shoot look)
   - `DD MMM YYYY` — day with abbreviated month name (e.g. `24 JUN 2026`)
4. The stamp uses the photo's **capture date** and renders in that signature warm-orange glow.

---

### Tool 6 — Layers (managing your stack)

Every watermark you add — text, logo, or signature — becomes a **layer**. Layers composite from bottom to top, so you have full control over what sits in front of what.

**To manage layers:**
1. Tap **Layers** in the tool dock.
2. You'll see every watermark layer in a list. For each one you can:
   - **Reorder** — drag to change stacking order (which mark sits on top).
   - **Show / Hide** — toggle a layer's visibility without deleting it (great for A/B comparisons).
   - **Adjust opacity** — set per-layer transparency.
   - **Delete** — remove a layer you no longer want.

This is how you build up a rich composition — e.g. a faint tiled brand behind a bold signature on top.

---

### Positioning (works for every layer)

Every text, logo, and signature layer uses the same **nine-point position grid**:

```
Top Left      Top Center      Top Right
Middle Left   Center          Middle Right
Bottom Left   Bottom Center   Bottom Right
```

**To reposition a layer:**
1. Select the layer's tool (or open it in **Layers**).
2. Tap **Position**.
3. Choose one of the nine presets.

Markepi keeps a consistent **padding** from the edges so nothing sits awkwardly flush against the border.

---

### Tool 7 — "More" (Output, Templates, and Content Credentials)

The **More** panel holds everything about how your file is written out.

#### Output format & quality
1. Tap **More** → **Format**.
2. Choose your output format:
   - **Preserve source** *(default)* — keep the original format (HEIC → HEIC, JPEG → JPEG). This is the safest choice and preserves HDR.
   - **HEIC** — modern, efficient, HDR-capable.
   - **JPEG** — universal compatibility. *(Note: JPEG can't carry HDR; Markepi warns you it will convert to standard dynamic range.)*
   - **PNG** — lossless, supports transparency.
   - **TIFF** — lossless archival.
3. For lossy formats (HEIC/JPEG), drag the **Quality** slider (shown as a percentage; default 100% for maximum quality). The slider is disabled for lossless formats where it doesn't apply.

#### Templates (save your look once, reuse forever)
1. Tap **More** → **Save as Template**.
2. Give it a name (e.g. *"Instagram signature"* or *"Client proofs"*).
3. Later, tap **Load Template** to instantly apply that entire watermark configuration to any new photo or batch.

Templates capture your **whole setup** — every layer, the frame, the date stamp, output settings, and rights metadata — so brand consistency takes one tap.

---

## ⭐ Content Credentials (C2PA) — Markepi's Flagship Feature

> **This is the reason Markepi exists in the AI era, and it should be a lead story on the website.** Anyone can add a watermark. Almost no consumer app can **cryptographically prove who made a photo, how it was made, and that it hasn't been altered since.** Markepi does — on-device, for free-tier and Pro users alike.

### Why it matters (the pitch for the page)

We've crossed the line where you **can't tell a real photo from an AI-generated one by looking at it.** Screenshots get faked, real photos get called fake, and creators have no simple way to assert "this is my work." The industry's answer is **C2PA / Content Credentials** — an open standard backed by Adobe, Microsoft, the BBC, Sony, Nikon, Leica, and the Coalition for Content Provenance and Authenticity (C2PA) and the Content Authenticity Initiative (CAI). It attaches a **tamper-evident, cryptographically signed "nutrition label"** to an image describing its origin and edit history.

Camera makers are baking it into hardware. Platforms are starting to read and display it. **Markepi brings it to your pocket** — so an everyday photographer, journalist, or seller can sign their photos with verifiable provenance, right on their iPhone, without a desktop suite or a cloud account.

**Positioning line for the site:** *"A watermark says it's yours. Content Credentials prove it."*

### What Markepi's Content Credentials actually do

When you enable Content Credentials, every export can carry a **signed C2PA manifest** — a sealed record of authorship and edit history that any C2PA-aware tool (Adobe, [Content Credentials Verify](https://contentcredentials.org/verify), and a growing list of platforms) can inspect. Markepi's manifest can assert, **honestly**:

- **Who made it** — your authorship, via a `schema.org CreativeWork` author assertion and IPTC rights fields.
- **How it was made** — your source declaration (camera, AI, AI-edited, composite).
- **What was done to it** — that Markepi watermarked/edited it, with the **original file preserved as an *ingredient*** so any prior Content Credentials remain intact and the edit chain is unbroken.
- **That it's unaltered since signing** — the manifest is cryptographically signed, so any later tampering with the pixels breaks the signature and shows up as invalid on verification.

### On-device signing with a Secure Enclave key — no cloud, ever

This is the part that sets Markepi apart from web-based provenance tools:

- **Signing happens entirely on your device.** No image, key, or manifest is uploaded. There is **no network call** in the signing path.
- **Your signing key is hardware-protected.** On a real device, Markepi uses a **Secure Enclave-backed** signing key whose private key is **non-exportable by construction** — it physically cannot leave the device. (A local Keychain software key is used only where the Secure Enclave isn't available, such as the simulator.)
- **Honest identity wording.** The credential is labeled a **"Markepi device signing identity."** Markepi is scrupulously clear that this proves the *device/app* signed it — it does **not** masquerade as a verified legal or personal identity. That honesty is a feature: it's provenance you can trust *because* it doesn't overclaim.

### Honesty by design — you can only claim what the evidence supports

Markepi will not let you fabricate provenance. Before you export, it **analyzes the source photo** and gathers **evidence** of its origin, each rated for strength (**weak / moderate / strong**):

| Evidence type | Example |
|---------------|---------|
| **C2PA manifest** | The source already carries signed Content Credentials |
| **IPTC digital source type** | Embedded "captured"/"AI-generated" declaration |
| **EXIF camera make/model** | Real camera/lens metadata consistent with a capture |
| **Software tag** | Editing software that touched the file |
| **User declaration** | What you told Markepi about the source |
| **Detector hint** | Signals suggesting AI generation |

From that evidence Markepi assigns a **provenance state** and shows it plainly:

- **Verified source** — strong evidence of genuine camera capture
- **AI-marked source** — the file declares itself AI-generated
- **User-declared** — provenance rests on your statement
- **Unknown source** — not enough evidence to say
- **Suspected AI** — signals point to AI generation

Crucially, the app **gates the claims you can make** to what the evidence supports — e.g. it only offers a "verified camera capture" claim when the metadata backs it up, only offers a "no AI" style claim when appropriate, and always allows rights/authorship protection. **You can't sign a lie.**

### Verify incoming photos, too

Content Credentials aren't just for export. Markepi can **read and verify** any C2PA manifest already present in a photo you bring in — so you can check whether an image you received is signed, by what, and whether that signature is intact before you trust or re-share it.

### Post-sign verification & the Export Receipt

Markepi doesn't just sign and hope. **Immediately after signing, it reads the manifest back and verifies it**, then shows you an **Export Receipt** — a plain-language summary of exactly what happened:

- The **source provenance report** (evidence and state, above).
- The **signing result**: whether a manifest was genuinely attached, whether the **signature is intact**, whether the **certificate is trusted**, and any validation issues found by the C2PA verifier.
- The **rights metadata** written (creator, copyright, credit, usage terms, licensor URL).
- The **metadata privacy profile** applied and the concrete **privacy actions** taken.

So you always know — and can prove — precisely what your file carries.

### IPTC rights metadata (embedded alongside the manifest)

Independently of the cryptographic manifest, Markepi seals standard **IPTC rights fields** into your export so your ownership travels with the file even in tools that only read IPTC:

- **Creator**
- **Copyright notice**
- **Credit line**
- **Usage terms**
- **Licensor URL**

### Step-by-step: sign a photo with Content Credentials

1. Tap **More** and turn on **Content Credentials**. (It's **off by default** — with it off, exports are shared directly with no provenance work, no receipt, and no metadata changes.)
2. Fill in your **rights metadata** — at minimum your creator name and copyright; optionally credit, usage terms, and a licensor URL.
3. Set your **source declaration** — *Photographed (camera)*, *AI-generated*, *AI-edited*, or *Composite*. Markepi shows the detected provenance state to guide you.
4. Tap **Sign** and confirm the short explainer. (Signing is **always user-initiated** — Markepi never signs silently.)
5. **Export.** Markepi renders on-device, attaches the signed manifest (preserving any existing credentials as an ingredient), verifies the result, and shows your **Export Receipt**.
6. Share the file anywhere — its Content Credentials travel with it and can be verified by anyone, anytime.

### Batch signing

You can enable Content Credentials for a whole batch, including batches that mix photos and videos.

> **Scope note (this version):** Batch processing is **not** image-only — Markepi watermarks and exports **photos *and* videos** in the same batch, with full metadata preserved on everything. The only step that's currently image-only is the **cryptographic C2PA signature itself**: in a mixed batch, Markepi **signs the photos** and continues to **watermark and export the videos normally, without a C2PA signature** — and videos are **never** counted as signing failures. Every video still keeps all of its other metadata.

### Content Credentials — feature summary

- ✅ On-device, Secure Enclave-backed signing — **no cloud, no network, no account**
- ✅ Tamper-evident signed C2PA manifest on export
- ✅ Preserves prior provenance as an **ingredient** (unbroken edit chain)
- ✅ Author + rights assertions (schema.org CreativeWork + IPTC)
- ✅ Honest source declaration (camera / AI / AI-edited / composite)
- ✅ Evidence-gated claims — **you can only claim what's supported**
- ✅ Reads & verifies incoming Content Credentials
- ✅ Post-sign verification with a plain-language **Export Receipt**
- ✅ Non-exportable, hardware-protected signing key
- ✅ Clearly labeled device identity — never overclaims a legal identity
- ✅ Batch Content Credentials — signs photos in a mixed batch; videos are watermarked and exported normally (the C2PA *signature* step is image-only in this version, but batch processing is not)
- ✅ Entirely opt-in and off by default

---

### Metadata Privacy Controls

You decide how much of your original metadata rides along with the exported file. Markepi offers three privacy profiles:

- **Preserve all** *(default)* — keep every piece of original metadata (GPS, date, camera, HDR, device). Nothing is stripped.
- **Strip sensitive** — remove sensitive fields (like precise location) while **keeping** your rights/copyright info, the HDR gain map, and color profile.
- **Minimal public** — a lean, share-safe metadata set.

**To set it:**
1. Tap **More** → metadata privacy.
2. Choose the profile that matches where the photo is going (e.g. *Preserve all* for your archive, *Strip sensitive* before posting publicly).

> HDR gain map and color profile are always re-attached correctly on export regardless of the privacy profile, so your photo never loses its look.

---

## Batch Processing (in depth)

Watermark a whole set in one pass — up to **20** items at a time. A batch can freely **mix photos, videos, and Live Photos** — it is not limited to images. Every item type is watermarked and exported with its metadata preserved (videos keep their audio; Live Photos keep their motion).

**The batch workflow:**
1. Load multiple items — **photos, videos, and Live Photos together** (from Photos, Files, or repeated Share-sheet imports).
2. A **thumbnail strip** appears showing every item. The current item is highlighted.
3. Set up your watermark **once** — it applies to the whole batch by default.
4. Tap between thumbnails to preview how the shared watermark looks on each image.
5. Tap **Share** to export the entire batch. A progress overlay shows how many are done and an estimated time; you can **Cancel** at any point (completed items are kept).
6. When it finishes, you get a summary (e.g. *"12 of 12 processed successfully"*), then the share sheet with all results ready to send.

**Per-item overrides — when one photo needs something different:**
1. Touch-and-hold (long-press) a thumbnail, or use its context menu → **Adjust This Photo**.
2. A per-item detail sheet opens. Change that single photo's watermark independently of the rest.
3. Overridden items show a small dot indicator on their thumbnail.
4. Tap **Reset overrides** in the toolbar to snap everything back to the shared configuration.

**Reordering and removing:**
- **Reorder** — drag thumbnails in the strip to change their order.
- **Remove** — tap **Edit** on the strip to reveal a red ✕ on each thumbnail; tap it to remove that item (with a confirmation, so nothing goes by accident).

---

## Video & Live Photo Support

Markepi isn't just for stills.

- **Videos** — apply the same text/logo/signature/frame watermarks to a full video. Audio is preserved, and a progress bar with estimated time keeps you informed during export.
- **Live Photos** — watermark both the still and the motion so the Live Photo stays "live."
- **Frame scrubber** — for videos, a scrub bar lets you preview the watermark at any point in the clip, so you can confirm placement against the actual footage before exporting.

All video and Live Photo exports carry their **metadata** through (a common failure point in other apps — Markepi explicitly sets export metadata so nothing is dropped).

---

## Exporting & Sharing (the no-forced-save finish)

1. Tap the blue **Share** button.
2. Markepi renders the final file(s) on-device.
3. The iOS **share sheet** appears with your finished media.
4. Send it **anywhere**:
   - **Save to Photos** *(if you want a copy)*
   - **Save to Files**
   - **AirDrop**
   - **Messages, Mail, WhatsApp, Instagram, Threads** — any app
5. Done. **No copy was forced into your camera roll** — you only keep one if you chose "Save to Photos."

For subscription/premium context, exports are gated by a simple daily allowance on the free tier (see Pricing) — the free limit is generous enough for everyday use.

---

## Settings & Personalization

Open **Settings** (the gear icon) for:

- **Remember Last Settings** — reopen the app with the exact watermark you used last time, or start clean each launch. Your choice.
- **Open Photo Picker on Launch** — jump straight into picking a photo when you open the app, or land on the home screen.
- **Appearance** — choose **Light**, **Dark**, or **System** for the editor.
- **Start From Scratch** — clear the current text, logo, signature, and frame to begin fresh.
- **About** — developer info, version, Terms of Use, and Privacy Policy.

---

## Design, Accessibility & Platform

- **Liquid Glass interface** — a modern, translucent UI that matches the latest iOS design language, with a real-glass toolbar and controls (with a clean material fallback where needed).
- **Adaptive layout** — the editor reflows intelligently between **portrait** (bottom dock + strip) and **landscape** (side rails, vertical dock, vertical batch strip) so the photo always gets the most room. Rotation is smooth, with no white flash.
- **Fully accessible** — supports **Dynamic Type** (the whole UI scales, including thumbnails and controls), **VoiceOver** (every control is labeled with helpful hints and actions), **Reduce Motion**, and **Reduce Transparency**.
- **Platforms** — iPhone and iPad (iOS/iPadOS 18 and later).

---

## Use Cases

### Photographers & Creators
- Brand every shot with a logo or signature before posting.
- Use the white frame + EXIF caption for that professional "shot on…" card.
- Attach signed Content Credentials to assert authorship and copyright.

### Small Businesses & Brands
- Save a template with your logo and brand color; apply it to every product photo in a batch.
- Consistent watermarking across dozens of images in one pass.

### Real Estate & Listings
- Batch-watermark a whole property shoot with your agency logo and contact line.
- Preserve HDR so interiors still look bright and true.

### Social Media
- Add a subtle handle or signature, strip your location for privacy, and share straight to Instagram or Threads — no camera-roll clutter.

### Selling Online (Marketplaces)
- Watermark listing photos to deter image theft before uploading.

### Protecting Work in the AI Era *(flagship use case)*
- **Photographers & journalists:** sign genuine camera captures with Content Credentials so editors and audiences can verify they're real and unedited — critical when authentic photos are being dismissed as "probably AI."
- **Creators & artists:** attach signed authorship and copyright to every piece you publish, so your ownership is provable and travels with the file.
- **Anyone re-sharing:** verify the Content Credentials on a photo you received *before* you trust or repost it.
- **Honest AI disclosure:** if your image is AI-generated or AI-edited, declare it truthfully in the credential — building trust instead of hiding it.
- All of it **on-device**, with a hardware-backed key, no cloud, and a receipt proving exactly what was signed.

### Everyday Memories
- Add a retro date stamp for a nostalgic film look on family photos and videos.

---

## How Markepi Solves Your Problems

| Problem | Markepi's Solution |
|---------|--------------------|
| Watermark apps save duplicates to my camera roll | **Direct share, no forced save** — one copy only if you choose |
| Editors strip my metadata and flatten HDR | **Full metadata + HDR gain map preservation** |
| Most apps can't watermark videos or Live Photos | **Photos, videos, and Live Photos** all supported |
| Free apps stamp their own logo on my photo | **No app-branded watermark, ever** |
| Everything useful is behind a subscription | **Real free tier**; optional one-time **lifetime** unlock |
| I don't know if my photos get uploaded | **No backend, no account** — 100% on-device |
| I want the same look every time | **Reusable templates** |
| One photo in the set needs a different mark | **Per-item overrides** in batch mode |
| I need that gallery white-frame with shot info | **White frame with auto EXIF caption** |
| I can't prove a photo is really mine | **Signed Content Credentials (C2PA) + IPTC rights** |
| AI images are everywhere — how do I show mine is real? | **On-device C2PA signing** with an honest, evidence-gated source declaration |
| Someone edited my photo after I shared it | **Tamper-evident manifest** — any change breaks the signature and shows as invalid |
| I received a photo — is it authentic? | **Read & verify** incoming Content Credentials before you trust it |
| Web provenance tools want me to upload my photo | **Everything is signed on-device** — no upload, no account, key never leaves the phone |
| I want to remove my location before posting | **Metadata privacy profiles** (strip sensitive / minimal) |
| Watermarking many photos is tedious | **Batch up to 20** with one shared configuration |
| Getting a photo from Photos into an editor and out is slow | **Share-sheet in, share-sheet out** |

---

## Competitive Advantages

1. **Content Credentials (C2PA) on-device** — the flagship differentiator. Cryptographically signed, tamper-evident proof of authorship and origin, signed with a Secure Enclave key that never leaves the device. Virtually no other consumer iPhone app offers this.
2. **Evidence-gated, honest provenance** — you can only claim what the source metadata supports; the app never lets you fake authenticity, and never overclaims a legal identity.
3. **Reads *and* verifies incoming Content Credentials** — check a photo's provenance before you trust it, plus a post-sign **Export Receipt**.
4. **No forced save / no duplicates** — a true pass-through workflow.
5. **On-device, no backend, no account** — genuine privacy across the whole app.
6. **HDR + full metadata preservation** — quality is never sacrificed.
7. **Photos, videos, and Live Photos** — the rare app that does all three.
8. **No app-branded watermark** — your image, your mark only.
9. **White frame with automatic EXIF captions** — pro look, zero typing.
10. **Batch with per-item overrides** — power and flexibility together.
11. **Reusable templates** — brand consistency in one tap.
12. **Fair pricing** — usable free tier + one-time lifetime option.
13. **Hand-drawn signatures** with Apple Pencil support.
14. **Retro date stamps** for the nostalgic film look.
15. **Fully accessible & adaptive** — Dynamic Type, VoiceOver, portrait/landscape.

---

## Pricing (Markepi Pro)

Markepi is **free to download and use every day**, with an optional upgrade to remove limits.

**Free tier (daily allowance):**
- **3 photo exports per day**
- **1 video export per day**
- *(Photos and videos are tracked in separate daily buckets, and the count resets each day.)*
- **No app-branded watermark on any export**, ever — even on the free tier.

**Markepi Pro — unlimited exports.** Three ways to unlock the exact same "unlimited" entitlement:
- **Lifetime** — a one-time purchase that lifts the daily limit forever (no subscription).
- **Monthly** — auto-renewable subscription.
- **Annual** — auto-renewable subscription (best value).

Pro users export as much as they want, with no daily cap and no quota tracking.

---

## Marketing Taglines

### Primary
**"A watermark says it's yours. Markepi proves it."**

### C2PA / Content Credentials (lead with these — flagship)
- "Prove your photo is real. Prove it's yours."
- "Content Credentials, signed on your iPhone. No cloud, no account."
- "In the age of AI, sign what's real."
- "Tamper-evident proof of authorship — in your pocket."
- "The signature you can't forge — and neither can anyone else."
- "Verify what comes in. Sign what goes out."

### Supporting
- "Your mark. Your photo. Nobody else's."
- "Watermark anything — photos, videos, Live Photos."
- "From Photos to shared, no copy left behind."
- "On-device. No account. No cloud. No catch."
- "Keep your HDR. Keep your metadata. Just add your mark."
- "Sign your work. Prove it's yours."
- "The white-frame gallery look — captions fill themselves in."
- "Batch it once. Ship it all."
- "No forced saves. No duplicates. No app watermark."
- "A real free tier, and a lifetime option instead of a subscription."

---

## Feature Icons & Visual Elements

- ✍️ Text Watermarks
- 🖼️ Logo Watermarks
- 🖊️ Hand-Drawn Signatures
- ⬜ White Frame
- 🏷️ Auto EXIF Captions
- 📆 Retro Date Stamp
- 🎞️ Video Support
- 🌀 Live Photo Support
- 🌈 HDR Preservation
- 🧬 Full Metadata Preservation
- 🗂️ Batch Processing (up to 20)
- 🎯 Per-Item Overrides
- 🧩 Layers
- 💾 Templates
- 🛡️ Content Credentials (C2PA)
- 🔏 IPTC Rights Metadata
- 🕵️ Provenance Verification
- 🔒 Metadata Privacy Profiles
- 📤 Share Anywhere (no forced save)
- 📥 Photos & Files Import
- 🔗 Share-Sheet Handoff
- 🚫 No Backend / No Account
- 📱 On-Device Processing
- 🌗 Light / Dark / System
- ♿ Full Accessibility
- 🔄 Portrait & Landscape
- 💠 Liquid Glass UI
- 🆓 Real Free Tier
- ♾️ Lifetime Unlock

---

## SEO Keywords (for the page's meta and structured data)

Content Credentials app iPhone, C2PA app iOS, sign photo Content Credentials, prove photo is real, photo authenticity app, C2PA signing on device, verify photo provenance iPhone, content authenticity initiative app, tamper-evident photo signature, prove photo not AI, IPTC copyright iPhone, photo provenance app, photo watermark app iPhone, add watermark to photos iPad, watermark videos iPhone, Live Photo watermark, signature watermark app, logo watermark photos, white frame photo app, EXIF caption border, batch watermark photos, date stamp app film look, protect photo copyright, watermark without saving, private on-device watermark, HDR-safe watermark, no watermark free watermark app, remove location before sharing photo.

---

## App Facts (for llms.txt / structured data)

- **App name:** Markepi
- **Category:** Photo & Video / Productivity
- **Platforms:** iOS 18+, iPadOS 18+
- **Developer:** Orbitaar
- **Privacy:** No backend, no account, no data collection; all processing on-device
- **Media types:** Photos (HEIC, JPEG, PNG, TIFF), Videos, Live Photos
- **Standout capabilities:** watermarking with metadata + HDR preservation, direct share-sheet workflow, Content Credentials (C2PA) signing, batch processing with per-item overrides
- **Monetization:** Free tier (3 photos + 1 video/day); Markepi Pro via one-time Lifetime, Monthly, or Annual

---

*Document Version: 1.0*
*Last Updated: July 2026*
