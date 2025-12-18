# db의 구조
from database import Base
from sqlalchemy import Column, Integer, String, Boolean
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(200), index = True)
    completed= Column(Boolean,default= False)