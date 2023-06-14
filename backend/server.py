from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



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
async def upload_chunk(files: list[UploadFile]):
    print("received")
    res = []
    for file in files:
        res.append(file.filename)
    print("Received chunk:", res)
    return res



if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", port=8000, reload=True, host='0.0.0.0'
    )
    print("start")