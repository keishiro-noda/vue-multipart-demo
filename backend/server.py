from fastapi import FastAPI, Depends
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
def signin(data):
    print(data)
    return 



if __name__ == "__main__":
    thread = 0
    uvicorn.run(
        "__main__:app", port=8000, reload=True, host='0.0.0.0'
    )