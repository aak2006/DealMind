from fastapi import FastAPI

app = FastAPI(title="DealMind API")


@app.get("/")
def root():
    return {
        "message": "DealMind API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }