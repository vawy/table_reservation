from pydantic import BaseModel


class BasicResultResponseSchema(BaseModel):
    result: str = 'OK'
