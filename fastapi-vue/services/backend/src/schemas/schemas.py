from typing import Optional
from pydantic import BaseModel


class ParamsForPipeline(BaseModel):
    task_name: str
    k: int
    text: str
