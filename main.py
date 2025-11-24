from fastapi import FastAPI
from storage.router import router as storage_router

app = FastAPI()

@app.get("/status")
def get_status_with_image_link():
    return {
        "status": "кчау",
        "message": "оу є це маквін",
    }

app.include_router(storage_router)