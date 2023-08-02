from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def sayHi():
    return {'hello':'FastAPI'}
# path & Query parameters: -----------------------------
@app.get('/users/{userId}')
def getUser(userId: int):
    return {'user id': userId}
# ------------------------------------------------------
@app.get('/users/')
def getUserData(userId: int, userName: str):
    return {'user id': userId, 'user name': userName}
# follow the link bellow to try this out
# http://127.0.0.1:8000/users/?userId=1&userName=Hassan
# ------------------------------------------------------