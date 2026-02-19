from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import cloudinary.uploader

app = FastAPI()
cloudinary.config(
    cloud_name='dtefc9vkq',
    api_key='724627291312128',
    api_secret='4Ss2oD4GIkdGAGJ7ZZDszlsY6Y4'
)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):

    if not files:
        raise HTTPException(400, "No files provided")

    allowed = ["pdf","ppt","pptx","png","jpg","jpeg","doc","docx"]

    uploaded_urls = []

    for file in files:

        if not file.filename:
            continue

        ext = file.filename.split(".")[-1].lower()

        if ext not in allowed:
            raise HTTPException(400, f"{file.filename} type not allowed")

        result = cloudinary.uploader.upload(
            file.file,
            resource_type="auto",
            folder="uploads"
        )

        uploaded_urls.append({
            "filename": file.filename,
            "secure_url": result["secure_url"],
            "public_id": result["public_id"]
        })

    return {
        "message": "Files uploaded successfully",
        "files": uploaded_urls
    }
