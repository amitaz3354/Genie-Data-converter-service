from pydantic import BaseModel


class DataConverterInput(BaseModel):
    data: str


class DataConverterOutput(BaseModel):
    data: str
