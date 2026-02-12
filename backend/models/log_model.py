from pydantic import BaseModel

class IdentifyResponse(BaseModel):
    name: str
    similarity_score: float
    status: str
