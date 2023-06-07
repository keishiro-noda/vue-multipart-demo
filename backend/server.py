from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

thread = 0


@app.post("/multipart")
async def upload_chunk(chunk):
    # チャンクを保存または処理する必要のある任意の処理を実行します
    # この例では、チャンクの名前を表示しています
    print("received")
    print("Received chunk:", chunk.filename)
    return {"message": "Chunk uploaded"}



if __name__ == "__main__":
    thread = 0
    uvicorn.run(
        "__main__:app", port=8000, reload=True, host='0.0.0.0'
    )
    print("start")