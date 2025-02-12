from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# .env ファイルの読み込み
load_dotenv()

# DATABASE_URL の取得
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL が設定されていません。")

# Azure 環境の SSL 証明書パスを設定
ssl_cert_path = "/home/site/wwwroot/app/DigiCertGlobalRootCA.crt.pem"

# Azure の場合だけ SSL 設定を適用
if "azurewebsites.net" in DATABASE_URL:
    connect_args = {"ssl": {"ca": ssl_cert_path}}
else:
    connect_args = {}

# MySQL エンジン作成（接続安定性向上のため pool_pre_ping=True を追加）
engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースモデル定義
Base = declarative_base()

# モデル定義
class Product(Base):
    __tablename__ = "product"
    JAN = Column(String(13), primary_key=True)
    name = Column(String(100))
    price = Column(Integer)

# セッションの取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
