from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from OpenShift 4.21!"}

@app.get("/health")
def health_check():
    return {"status": "up"}