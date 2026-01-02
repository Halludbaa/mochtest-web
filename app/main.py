from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"ping!": "pong"}