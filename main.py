from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from mongolian2ipa import mongolian2ipa

app = FastAPI()

app.mount("/site", StaticFiles(directory="static"), name="static")


@app.get("/api/ipa")
def convert(text: str):
    ipa = mongolian2ipa(text)
    return {'ipa': ipa}
