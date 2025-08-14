from fastapi import FastAPI, HTTPException
from model.request_model import MathRequest
from controller.math_controller import handle_operation
from utils.log_config import logger

app = FastAPI()


@app.post("/calculate")
def calculate(request: MathRequest):
    logger.info(f"API received: {request}")
    try:
        result = handle_operation(request.operation, request.inputs)
        return {"result": result}
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
