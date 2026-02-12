from pydantic import BaseModel

class EnrollRequest(BaseModel):
    name: str
