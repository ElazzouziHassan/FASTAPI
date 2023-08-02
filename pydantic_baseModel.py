from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Package(BaseModel):
    id: int
    name: str
    title: Optional[str] = None
  

app = FastAPI()

@app.get('/')
async def helloWorld():
    return {'Hello': 'World!'}

@app.post('/package/')
async def createPackage(package: Package):
    return package
# use this link to try it:
# http://127.0.0.1:8000/docs#/default/createPackage_package__post