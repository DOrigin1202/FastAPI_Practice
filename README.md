# FastAPI MySQL CRUD

FastAPI + MySQL 연동 CRUD API

## 환경 설정

1. 패키지 설치
```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic-settings
```

2. `.env` 파일 생성
```bash
DB_USERNAME=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=db_fastapi
```

3. MySQL DB 생성
```sql
CREATE DATABASE db_fastapi;
```

4. 서버 실행
```bash
uvicorn main:app --reload
```

5. API 문서 확인
```
http://localhost:8000/docs
```

## 파일 구조
```
FastAPI/
├── .env              # 환경변수 (Git 제외)
├── .gitignore        # Git 무시 파일
├── config.py         # 설정
├── test_db.py        # DB 연결 테스트
├── main.py           # FastAPI 앱
└── README.md         # 프로젝트 설명
```