import os
import sys
sys.path.insert(1, "src/")
sys.path.insert(2, "app/")
sys.path.insert(3, "configs/")

import json
import uvicorn
from custom_logger import CustomizeLogger
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.script import function
from schemas import API_Params

# Loading Logger
config_path = os.path.join(os.path.dirname(__file__), "../configs/logging_config.json")
logger = CustomizeLogger.make_logger(config_path)

app = FastAPI(
    title="APP",
    description="Sample App",
    version=0.1,
)

@app.post("/division")
def divide(request:Request, payload:API_Params):
    params = json.loads(payload.json())
    result = function(params['a'], params['b'])
    response_body = {"result": result}
    response = JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(response_body),
        )
    return response

@app.exception_handler(ZeroDivisionError)
def _zero_division_error(request: Request, exc: ZeroDivisionError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"error": {"title": "Internal Server Error", "detail": exc.args[0]}}),
    )

if __name__ == "__main__":
    uvicorn.run(app, port=int("9000"), host="0.0.0.0", debug=True)