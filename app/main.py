from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import product, sale

app = FastAPI()

# ここでフロントエンドのURLを指定
origins = [
    "https://tech0-gen8-step4-pos-app-79.azurewebsites.net"  # フロントエンドURL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンを制限
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(product.router)
app.include_router(sale.router)
