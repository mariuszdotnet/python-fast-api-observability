import os
from dotenv import load_dotenv
#from enum import Enum
from fastapi import FastAPI
#from pydantic import BaseModel
import uvicorn
# Import the `configure_azure_monitor()` function from the
# `azure.monitor.opentelemetry` package.
# Config details - https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=aspnetcore
from azure.monitor.opentelemetry import configure_azure_monitor # type: ignore
# Import the tracing api from the `opentelemetry` package.
from opentelemetry import trace # type: ignore
from logging import getLogger

load_dotenv()

logger = getLogger(__name__)

def test():
    # try:
    #     print("Error: Division by zero, instance 1")
    #     val = 1/0
    # except ZeroDivisionError:
    #     logger.exception("Error: Division by zero 1")
    try:
        print("Error: Division by zero, instance 2")
        val = 1/0
    except ZeroDivisionError:
        logger.exception("Error: Division by zero 2", stack_info=True, exc_info=True)

app = FastAPI()

# Path Parameters
@app.get("/")
async def root():
    test()
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)