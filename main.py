from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model for the text field
class TextData(BaseModel):
    text: str

# Welcome Note
@app.get("/")
def read_root():
    return {"message": "Welcome to Jennifer's Python API!"}

# FastAPI validates the JSON body against TextData, which requires a string "text" field.
@app.post("/generate/")
def generate(data: TextData):
    """Accept JSON containing text and return its MD5 checksum."""
    # Encode the text and represent its MD5 digest as a hexadecimal string.
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    return {"checksum": checksum}
