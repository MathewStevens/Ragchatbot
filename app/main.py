from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_health_status() -> dict:
    return {"status": "healthy"}