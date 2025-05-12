from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_smth():
    return {"hello": "world"}
