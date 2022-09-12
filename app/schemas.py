from typing import List
from pydantic import BaseModel

class API_Params(BaseModel):
    a : int
    b : int