# test_db.py
from sqlalchemy import create_engine, text
from config import settings

def test_connection():
    print("=" * 50)
    print("DB 연결 테스트 시작")
    print("=" * 50)
    
    # 1. 설정 확인
    print(f"\n[설정 정보]")
    print(f"Host: {settings.db_host}")
    print(f"Port: {settings.db_port}")
    print(f"Database: {settings.db_name}")
    print(f"Username: {settings.db_username}")
    print(f"Password: {'*' * len(settings.db_password)}")
    
    # 2. 연결 문자열 확인
    print(f"\n[연결 문자열]")
    # 비밀번호 가리기
    safe_url = settings.database_url.replace(settings.db_password, "****")
    print(f"{safe_url}")
    
    # 3. DB 연결 시도
    print(f"\n[연결 시도 중...]")
    try:
        engine = create_engine(settings.database_url)
        
        # 간단한 쿼리 실행
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ 연결 성공!")
            
            # MySQL 버전 확인
            version = connection.execute(text("SELECT VERSION()"))
            print(f"✅ MySQL 버전: {version.fetchone()[0]}")
            
            # 현재 DB 확인
            db = connection.execute(text("SELECT DATABASE()"))
            print(f"✅ 현재 DB: {db.fetchone()[0]}")
            
    except Exception as e:
        print(f"❌ 연결 실패: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("테스트 완료!")
    print("=" * 50)
    return True

if __name__ == "__main__":
    test_connection()