import os
import zipfile

if os.path.exists("erp_bundle.zip"):
    with zipfile.ZipFile("erp_bundle.zip", "r") as zf:
        zf.extractall(".")

os.makedirs("uploads/media", exist_ok=True)
os.makedirs("uploads/dispatch", exist_ok=True)

from erp_core import app  # noqa: E402,F401

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
