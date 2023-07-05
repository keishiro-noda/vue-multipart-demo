from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import boto3
import json
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
    expose_headers=["*"]
)


def on_upload_complete(file_path: str):
    print('Upload complete')
    print(file_path)
    try:
        with open(file_path + ".info", "r") as info_file:
            file_info = json.load(info_file)
            file_name = file_info.get("metadata").get("name")
            print( {"file_info": file_info})
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=".info file not found")
    s3.upload_file(file_path, "user_files", file_name)
    print("send s3")


def on_your_specific_auth():
    pass


app.include_router(
    create_api_router(
        files_dir='/home/guest/my-vue-app/backend/uploads/',
        location='http://localhost:8000/files',
        on_upload_complete=on_upload_complete,
        auth=on_your_specific_auth,
    ),
    prefix="/files"
)

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
