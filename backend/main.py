from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
import os

from backend.services.enrollment_service import enroll_user
from backend.services.identification_service import identify_user

app = FastAPI(title="AI Biometric Authentication API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend running successfully"}


@app.post("/enroll")
def enroll(name: str, files: List[UploadFile] = File(...)):

    file_paths = []

    for file in files:
        file_location = f"temp_{file.filename}"

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_paths.append(file_location)

    enroll_user(name, file_paths)

    # Cleanup temp files
    for path in file_paths:
        if os.path.exists(path):
            os.remove(path)

    return {
        "message": f"{name} enrolled successfully with {len(files)} images"
    }


@app.post("/identify")
def identify(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = identify_user(file_location)

    # Cleanup temp file
    if os.path.exists(file_location):
        os.remove(file_location)

    return result
