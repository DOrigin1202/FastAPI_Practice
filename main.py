from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from schemas import TodoCreate, ToDoResponse
from models import Todo

# DB 테이블 생성 부터
Base.metadata.create_all(bind=engine)

app = FastAPI()
# 전체 조회
@app.get("/todos",response_model =list[ToDoResponse])
def to_do_page(db:Session = Depends(get_db)):
    return db.query(Todo).all()

# 할일 생성
@app.post("/todos", response_model = ToDoResponse)
def create_todo(todo : TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# 개별 조회
@app.get("/todos/{todo_id}",response_model= ToDoResponse)
def get_todo(todo_id : int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model = ToDoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=400, detail="To Do Not Found")
    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)
    return todo

@app.get("/")
def root_page():
    return {"message":"This page is main Page."}