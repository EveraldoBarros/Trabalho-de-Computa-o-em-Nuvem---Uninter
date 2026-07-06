from fastapi import FastAPI
from app.core.database import Base, engine
from app.api import auth, users, workflows, uploads

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudFlow SaaS",
    description="API SaaS cloud-native para gestão de fluxos de trabalho.",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(workflows.router)
app.include_router(uploads.router)


@app.get("/")
def root():
    return {
        "app": "CloudFlow SaaS",
        "message": "API funcionando com sucesso.",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "cloudflow-saas"}
