# Request구조 Get Post구조 설정 부분
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    
class ToDoResponse(BaseModel):
    id : int
    title: str
    completed: bool
    
    class Config:
        from_attributes = True