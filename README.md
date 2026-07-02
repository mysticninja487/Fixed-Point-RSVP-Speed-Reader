# Fixed Point — Speed Reader

An installable RSVP (Rapid Serial Visual Presentation) speed-reading app. Words
flash one at a time, each aligned so its "optimal recognition point" letter
stays in the exact same spot on screen — your eyes never have to move, only
the word changes underneath them.

**[Live demo →](https://mysticninja487.github.io/Fixed-Point-RSVP-Speed-Reader/)**

## Features
- Adjustable words-per-minute (150–700)
- Automatically pauses longer on punctuation and long words
- Keyboard shortcuts: `Space` play/pause, `←`/`→` jump 10 words, `Esc` edit text
- Upload a `.txt`, `.pdf`, or `.docx` file to extract text automatically
- Installable as a standalone app (PWA) on desktop, Android, and iOS
- Works fully offline once installed

## Run it locally
```bash
python3 serve.py
```
Then open http://localhost:8000 — click **"Install app"** in the header to
add it as a standalone app.

(Any static file server works — `npx serve`, `php -S localhost:8000`, etc.
The service worker requires the app to be served over `http://` or `https://`,
not opened directly as a `file://` path.)

## Deploy to GitHub Pages
This repo includes a GitHub Actions workflow that deploys automatically.

1. Push this repo to GitHub.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **GitHub Actions**.
4. Push to `main` (or run the workflow manually from the **Actions** tab).
5. Your app will be live at `https://<your-username>.github.io/<repo-name>/`.

Once live, visit the link on your phone:
- **Android/Chrome** — tap the install prompt, or menu → "Install app"
- **iPhone/Safari** — tap Share → "Add to Home Screen"

## Project structure
```
index.html               the app
manifest.json             PWA metadata (name, icons, colors)
sw.js                     service worker — caches the app for offline use
icon-192.png               app icon
icon-512.png               app icon
icon-512-maskable.png       app icon (Android adaptive/maskable)
serve.py                   tiny local dev server
.github/workflows/deploy.yml   auto-deploy to GitHub Pages
```

## License
MIT — see [LICENSE](LICENSE).
