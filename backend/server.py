from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import boto3
from starlette.staticfiles import StaticFiles

from tusserver.tus import create_api_router


s3 = boto3.client(
        "s3",
        endpoint_url="http://s3:9000",
        aws_access_key_id="root",
        aws_secret_access_key="adminpass",
    )

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def on_upload_complete(file_path: str):
    print('Upload complete')
    print(file_path)


app.include_router(
    create_api_router(
        files_dir='/backend/uploads/', # OPTIONAL
        location='http://localhost:3000/chunk', # OPTIONAL
        on_upload_complete=on_upload_complete # OPTIONAL
    ),
    prefix="/files"
)


@app.post("/chunk")
async def upload_chunk(file: UploadFile):
    print("received")

    save_path = f"uploads/{file.filename}"
    with open(save_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

    s3.upload_file(save_path, "user_files", file.filename)
    print("Received chunk")
    return


@app.post("/multipart")
async def upload_chunk(file: UploadFile):
    print("received")

    save_path = f"uploads/{file.filename}"
    with open(save_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

    s3.upload_file(save_path, "user_files", file.filename)
    print("Received chunk")
    return



if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", port=8000, reload=True, host='0.0.0.0'
    )
    print("start")