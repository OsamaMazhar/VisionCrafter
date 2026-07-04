# Removed Markepi Content

**Date removed:** 2026-07-04

## What was removed

The public-facing Markepi product page and references were removed from the main website to hide the product while keeping its legal pages (privacy policy & terms of use) accessible.

### Files moved here (backup)
| File | Original location |
|------|-------------------|
| `index.html` | `docs/markepi/index.html` |
| `assets/markepi-icon.png` | `docs/markepi/assets/markepi-icon.png` |
| `assets/markepi-icon-1024.png` | `docs/markepi/assets/markepi-icon-1024.png` |

### Files still live (kept accessible)
| File | URL |
|------|-----|
| `docs/markepi/privacy-policy.html` | `/markepi/privacy-policy.html` |
| `docs/markepi/terms-of-use.html` | `/markepi/terms-of-use.html` |

### Edits made to existing pages
| File | What changed |
|------|--------------|
| `docs/index.html` | Removed "Markepi" from meta description; removed "Introducing Markepi" news item |
| `docs/apps.html` | Removed the Markepi app card from the apps grid |
| `docs/llms.txt` | Removed the Markepi section |
| `docs/sitemap.xml` | Removed the `/markepi/` product page entry (kept privacy & terms entries) |

---

## How to restore

1. **Restore the product page & assets:**
   ```bash
   cp _removed_markepi/index.html docs/markepi/index.html
   cp -r _removed_markepi/assets/* docs/markepi/assets/
   ```

2. **Restore homepage references** (`docs/index.html`):
   - **Meta description** (line ~7): Add back ` and Markepi watermarking with Content Credentials (C2PA)` before the closing `" />`
   - **News section**: Re-insert the following block before the SyncAlbum news item:
     ```html
     <div class="news-item">
         <div class="news-date">
             <i class="bi bi-lightning-fill news-flash me-1"></i>
             02.07.2026
         </div>
         <div class="news-content">
             <h4>Introducing Markepi — Coming Soon!</h4>
             <p>Meet our newest app: <strong>Markepi</strong>, a privacy-first watermarking and photo-provenance studio for iPhone and iPad. Add text, logos, signatures, white frames, and retro date stamps to photos, videos, and Live Photos — then cryptographically sign them with tamper-evident <strong>Content Credentials (C2PA)</strong>, entirely on-device. <a href="markepi/index.html" class="btn-link-styled">Learn More <i class="bi bi-arrow-right"></i></a></p>
         </div>
     </div>
     ```

3. **Restore apps page** (`docs/apps.html`): Add back the Markepi app card inside the `.apps-grid` div:
   ```html
   <div class="app-card fade-in-up delay-4">
       <div class="app-icon"><img src="markepi/assets/markepi-icon.png" alt="Markepi Icon"></div>
       <h2>Markepi</h2>
       <p>A privacy-first watermarking studio. Add text, logos, signatures, and frames to photos, videos, and Live Photos — then cryptographically sign them with Content Credentials (C2PA). 100% on-device.</p>
       <a href="markepi/index.html" class="app-button"><span>Learn More</span><i class="bi bi-arrow-right"></i></a>
   </div>
   ```

4. **Restore llms.txt**: Add back the Markepi block:
   ```text
   - Markepi: https://www.orbitaar.com/markepi/
     - Status: Coming soon to the App Store
     - Purpose: Privacy-first watermarking and photo-provenance studio...
     - Platforms: iOS 18+, iPadOS 18+
   ```

5. **Restore sitemap.xml**: Add back the `/markepi/` entry:
   ```xml
   <url>
     <loc>https://www.orbitaar.com/markepi/</loc>
     <lastmod>2026-07-02</lastmod>
     <changefreq>monthly</changefreq>
     <priority>0.8</priority>
   </url>
   ```
