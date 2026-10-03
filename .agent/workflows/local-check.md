---
description: how to check this website locally
---

To check the website locally, you can use a simple HTTP server. Since this is a static site, there are several ways to do this:

### Option 1: Python (Recommended)
To see the website directly, run the server from the `docs` directory:

```bash
cd docs && python3 -m http.server 8000
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Option 2: Live Server (VS Code Extension)
If you use VS Code, you can install the "Live Server" extension and click "Go Live" at the bottom of the editor while an HTML file is open.

### Option 3: Direct File Opening
You can simply double-click the `index.html` file in the `docs` folder to open it in your browser. *Note: Some features like relative paths might behave differently than on a web server.*
