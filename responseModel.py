from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class PackageIn(BaseModel):
    secretId: int
    name: str
    title: Optional[str] = None

class PackageOut(BaseModel):
    name: str
    title: Optional[str] = None

app = FastAPI()

@app.get('/')
async def helloWorld():
    return {'Hello': 'World!'}

@app.post("/package/", response_model=PackageOut)
async def makePackage(package: PackageIn):
    return package

# follow link to try it out:
# http://127.0.0.1:8000/docs#/default/makePackage_package__post