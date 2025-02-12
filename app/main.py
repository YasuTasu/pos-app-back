from fastapi import FastAPI
from app.routes import product, sale
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ルーター登録
app.include_router(product.router)
app.include_router(sale.router)

# 本番環境では特定のフロントエンドのみ許可
origins = [
    "https://tech0-gen8-step4-pos-app-79.azurewebsites.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンを設定
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッド（GET, POST, PUT, DELETEなど）を許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)
