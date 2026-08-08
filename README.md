# Video QR Project

A simple webpage that plays a video, hosted for free on GitHub Pages.
Scan the QR code → phone opens the page → video plays.

---

## Project Structure

```
video-qr-project/
├── index.html          ← the webpage with the video player
├── video.mp4           ← YOUR video file (you add this)
├── generate_qr.py      ← Python script to create the QR code
├── qrcode_output.png   ← QR image (created after running the script)
└── .gitignore          ← tells Git what NOT to upload
```

---

## Step 1 — Install Git (one-time)

Git is needed to push your project to GitHub.

1. Go to https://git-scm.com/download/win
2. Download and run the installer (keep all default options).
3. Open a new PowerShell window and confirm it works:
   ```
   git --version
   ```
   You should see something like `git version 2.x.x`.

---

## Step 2 — Install Python (one-time, if not already installed)

Python is needed to run the QR code script.

1. Go to https://www.python.org/downloads/
2. Download the latest version and run the installer.
3. **Important:** tick the box that says **"Add Python to PATH"** before clicking Install.
4. Confirm it works:
   ```
   python --version
   ```

---

## Step 3 — Create a GitHub account and a new repository

1. Go to https://github.com and sign up (it's free).
2. Click the **+** button (top-right) → **New repository**.
3. Fill in:
   - **Repository name:** `video-qr-project` (or any name you like)
   - **Visibility:** Public  ← required for free GitHub Pages
   - Leave everything else as default — do NOT tick "Add a README"
4. Click **Create repository**.
5. GitHub will show you a page with setup commands. Keep this tab open.

---

## Step 4 — Add your video file

Copy your video file into the project folder and rename it to `video.mp4`:

```
e:\video-qr-project\video.mp4
```

> **Note:** The .gitignore file intentionally excludes video files because
> they are large and GitHub has a 100 MB file size limit. See Step 6 for
> how to handle large videos.

---

## Step 5 — Push the project to GitHub

Open PowerShell, navigate to the project folder, and run these commands
**one by one** (replace the placeholders in angle brackets):

```powershell
# Move into the project folder
cd e:\video-qr-project

# Set up your identity (one-time, use your GitHub email)
git config --global user.email "<your-email@example.com>"
git config --global user.name "<Your Name>"

# Initialise the repo and stage the files
git init
git add index.html .gitignore generate_qr.py README.md

# Commit
git commit -m "Initial commit: video webpage"

# Point to your GitHub repository (copy the URL from the GitHub tab)
git remote add origin https://github.com/<your-username>/video-qr-project.git

# Push
git branch -M main
git push -u origin main
```

GitHub will ask for your username and password the first time.
Use your GitHub username and a **Personal Access Token** as the password
(GitHub no longer accepts plain passwords over HTTPS).

To create a token: GitHub → Settings → Developer settings →
Personal access tokens → Tokens (classic) → Generate new token →
tick "repo" scope → copy the token and use it as your password.

---

## Step 6 — Handle large video files (over 25 MB)

GitHub blocks files over 100 MB and warns on files over 25 MB.
There are two easy options:

**Option A — Use Git LFS (recommended)**
```powershell
# Install Git LFS (one-time)
git lfs install

# Track mp4 files with LFS
git lfs track "*.mp4"
git add .gitattributes

# Now add and commit your video normally
git add video.mp4
git commit -m "Add video file via LFS"
git push
```
Git LFS is free up to 1 GB of storage on GitHub.

**Option B — Host video elsewhere**
Upload your video to Google Drive, OneDrive, or YouTube (unlisted),
then update the `<source src="...">` line in index.html to point to
the direct video URL instead of `video.mp4`.

---

## Step 7 — Enable GitHub Pages

1. On GitHub, open your repository.
2. Click **Settings** (top menu of the repo).
3. In the left sidebar click **Pages**.
4. Under **Source**, choose:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**.
6. Wait about 1–2 minutes, then refresh. GitHub will show you your URL:
   ```
   https://<your-username>.github.io/video-qr-project/
   ```
   Open that URL in your browser — you should see your video page.

---

## Step 8 — Generate the QR code

Install the Python dependency (one-time):
```powershell
pip install qrcode[pil]
```

Run the script:
```powershell
cd e:\video-qr-project
python generate_qr.py
```

When prompted, paste your GitHub Pages URL:
```
https://<your-username>.github.io/video-qr-project/
```

The script saves `qrcode_output.png` in the project folder.
Open it, print it, or display it on screen — scanning it opens your video page.

---

## Step 9 — Test the QR code on your phone

1. Open your phone's camera app (works on both iPhone and Android).
2. Point it at the QR code image on your screen or printed paper.
3. Tap the notification/banner that appears.
4. Your video page should open in the phone's browser.

If the video doesn't play:
- Make sure `video.mp4` was pushed to GitHub (check the repo on github.com).
- Check that GitHub Pages is enabled (Step 7).
- Try opening the URL directly in your phone browser first.

---

## Step 10 — Pushing updates after changes

Any time you edit `index.html` or add a new video, push the update:

```powershell
cd e:\video-qr-project

git add index.html
# or: git add .   (to stage all changed files)

git commit -m "Update: describe what you changed"
git push
```

GitHub Pages picks up the changes automatically within a minute or two.
The QR code URL stays the same — no need to regenerate it.

---

## Quick Reference

| Task | Command |
|---|---|
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push to GitHub | `git push` |
| Generate QR code | `python generate_qr.py` |
| Install QR dependency | `pip install qrcode[pil]` |

---

## Troubleshooting

**"git is not recognized"** → Git is not installed. See Step 1.

**"python is not recognized"** → Python is not installed or not in PATH. See Step 2.

**Video doesn't play on phone** → Most phone browsers support MP4/H.264.
Re-encode your video with HandBrake (free) if it doesn't play:
https://handbrake.fr — use the "Fast 1080p30" preset.

**GitHub Pages shows a 404** → Wait 2 minutes and refresh. If it persists,
double-check that the branch is set to `main` in the Pages settings.

**QR code scans but page looks broken** → Clear your phone browser cache
and reload, or try a different browser (Chrome, Safari).
