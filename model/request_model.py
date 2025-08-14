from pydantic import BaseModel
from typing import List


class MathRequest(BaseModel):
    operation: str  # "power", "fibonacci", or "factorial"
    inputs: List[int]
