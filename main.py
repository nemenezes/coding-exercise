"""
API with 3 endpoints.
Run `uvicorn main:app` and go to 127.0.0.1:8000 in the browser.
Docs: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def hello_world():
    return {"msg": "Hello World"}


@app.get("/add/")
async def add_two_numbers(first: int = 0, second: int = 0):
    return {"sum": first + second}


@app.get("/joinstrings/")
async def join_strings(first_str: str = "", second_str: str = ""):
    return {"output": f"{first_str}-{second_str}"}
