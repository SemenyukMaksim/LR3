from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def get_status_with_image_link():
    return {
        "status": "кчау",
        "message": "оу є це маквін",
    }
