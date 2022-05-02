import starlette.responses as _responses
from fastapi import FastAPI
from data_converter_model import DataConverterInput
from data_converter_service import DataConverterService

app = FastAPI()

@app.get("/")
async def root():
    return _responses.RedirectResponse("/redoc")

@app.post("/convert")
async def convert_pdf(input: DataConverterInput):
    service = DataConverterService(input)
    return service.convert()

@app.get(
    e
)
