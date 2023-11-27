from pydantic import BaseModel
from typing import Optional

# User Input Objects

class ValueQuery(BaseModel):
    value: Optional[int] = 0
    note: Optional[str] = None