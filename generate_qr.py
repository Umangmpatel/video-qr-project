"""
generate_qr.py
--------------
Generates a QR code PNG from your GitHub Pages URL.

Usage
-----
1. Install the dependency (one-time):
       pip install qrcode[pil]

2. Run the script:
       python generate_qr.py

   You will be prompted to enter your GitHub Pages URL, e.g.:
       https://<your-username>.github.io/<your-repo-name>/

3. A file called  qrcode_output.png  is saved in this folder.
   Print it or display it — anyone who scans it opens your video page.
"""

import sys

# ── Dependency check ──────────────────────────────────────────────────────────
try:
    import qrcode
    from PIL import Image  # comes with qrcode[pil]
except ImportError:
    print("\n[ERROR] Required packages not found.")
    print("Please install them by running:\n")
    print("    pip install qrcode[pil]\n")
    sys.exit(1)

# ── Input ─────────────────────────────────────────────────────────────────────
print("=" * 55)
print("         QR Code Generator for Your Video Page")
print("=" * 55)

url = input("\nEnter your GitHub Pages URL\n(e.g. https://yourname.github.io/your-repo/): ").strip()

if not url.startswith("http"):
    print("\n[WARNING] URL doesn't start with 'http'. Adding 'https://' prefix.")
    url = "https://" + url

output_file = "qrcode_output.png"

# ── Generate ──────────────────────────────────────────────────────────────────
print(f"\nGenerating QR code for:\n  {url}\n")

qr = qrcode.QRCode(
    version=None,          # auto-size based on data length
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% damage tolerance
    box_size=12,           # pixels per QR "box"
    border=4,              # quiet zone (minimum is 4)
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(output_file)

print(f"[OK] QR code saved as:  {output_file}")
print("\nNext steps:")
print("  1. Open qrcode_output.png and print it (or display on screen).")
print("  2. Scan with your phone camera — it should open your video page.")
print("  3. Make sure your video.mp4 is uploaded to GitHub first!\n")
