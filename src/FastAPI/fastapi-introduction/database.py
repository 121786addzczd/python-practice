from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# データベース接続に必要な情報を個別の変数に格納
DB_USER = "fastapiuser"
DB_PASSWORD = "fastapipass"
DB_HOST = "0.0.0.0"
DB_PORT = "5432"
DB_NAME = "fleamarket"

# これらの変数を使用してSQLAlchemyのデータベースURLを設定
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# commitを明示的にする
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
