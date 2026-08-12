from fastapi import FastAPI

from app.routes.documents import router as documents_router


app = FastAPI(
    title="Day011 Document CRUD API",
    version="0.1.0",
)

#每隔几秒访问这个接口，判断这个服务进程是否还活着
@app.get("/health")
def health():
    return {
        "status": "ok",
    }

#把定义好的文档 CRUD 接口（/documents、/documents/{id} 等）挂载到主应用上
app.include_router(documents_router)