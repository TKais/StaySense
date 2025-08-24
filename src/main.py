from fastapi import FastAPI
from fastapi.responses import JSONResponse
import data/listings.json

app = FastAPI(title="StaySense Recommender API")

@app.get("/")
def home():
    content = 
    return JSONResponse(content=content, status_code=200)