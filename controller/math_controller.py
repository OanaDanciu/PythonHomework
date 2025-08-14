from service.math_service import power, fibonacci, factorial, sum_digits
from model.request_model import MathRequest
from storage.db import save_request
from utils.log_config import logger
from utils.async_worker import run_in_thread


def handle_operation(operation: str, inputs: list[int]) -> str:
    request = MathRequest(operation=operation, inputs=inputs)
    logger.info(f"Received request: {request}")

    try:
        if request.operation == "power":
            result = run_in_thread(power, *request.inputs)
        elif request.operation == "fibonacci":
            result = run_in_thread(fibonacci, *request.inputs)
        elif request.operation == "factorial":
            result = run_in_thread(factorial, *request.inputs)
        elif request.operation == "sum_digits":
            result = run_in_thread(sum_digits, *request.inputs)

        save_request(request.operation, request.inputs, str(result))
        logger.info(f"Processed successfully: {request} = {result}")
        return f"Result: {result}"

    except Exception as e:
        logger.error(f"Error while processing request {request}: {str(e)}")
        raise
