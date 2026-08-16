from datetime import datetime

from pydantic import BaseModel,Field

class DocumentCreate(BaseModel):
    user_id:int = Field(gt=0) #强制要求这个数字必须大于 0，不能传负数或 0
    title:str = Field(min_length=1,max_length=200)
    content:str | None = None

class DocumentUpdate(BaseModel):
    title:str = Field(min_length=1,max_length=200)
    content:str | None = None

class DocumentOut(BaseModel):
    id:int
    user_id:int
    title:str
    content:str | None
    created_at:datetime

class AiTaskRequest(BaseModel):
    taskId:str = Field(min_length=1)
    prompt:str = Field(min_length=1,max_length=1000)

class AiTaskResponse(BaseModel):
    requestId: str
    taskId: str
    status: str
    result: str