# VisionCrafter
Repo for knowledge sharing about our Computer Vision apps.

## Local development

The website lives in the `docs/` folder (served via GitHub Pages on `www.orbitaar.com`).

To preview the site locally:

```bash
cd docs
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

Other options:

- `npx serve .` (Node)
- `php -S localhost:8000` (PHP)
- VS Code "Live Server" extension → right-click `index.html` → *Open with Live Server*

Use a real server (not `file://`) so absolute paths like `/autoalign/blog/` resolve the same way they do in production.

> Note: blog articles reference images via absolute `https://www.orbitaar.com/assets/...` URLs, so when running locally those images load from the live site (or won't load if you're offline).
