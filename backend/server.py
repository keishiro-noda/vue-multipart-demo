from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import boto3



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



@app.post("/multipart")
async def upload_chunk(file: UploadFile = File(...)):
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