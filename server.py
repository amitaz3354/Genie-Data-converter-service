from fastapi import FastAPI
from data_converter_model import DataConverterInput
from data_converter_service import DataConverterService

app = FastAPI()

@app.get("/")

@app.post("/convert")
async def convert_pdf(input: DataConverterInput):
    service = DataConverterService(input)
    return service.convert()
