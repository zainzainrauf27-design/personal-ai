from fastapi import FastAPI

app = FastAPI(title="Personal AI")


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Personal AI backend is running."
    }
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "personal-ai-backend"
    }
