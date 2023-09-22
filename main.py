from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from mongolian_to_ipa import mongolian_convert_to_ipa

app = FastAPI()

app.mount("/site", StaticFiles(directory="static"), name="static")


@app.get("/api/ipa")
def convert(text: str):
    ipa = mongolian_convert_to_ipa(text)
    return {'ipa': ipa}
