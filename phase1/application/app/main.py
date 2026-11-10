
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4

app = FastAPI(
    title="GreenOps Platform API",
    description="Cloud-native platform for energy-efficient workload scheduling",
    version="1.0.0"
)

deployments = {}

class DeploymentRequest(BaseModel):
    application_name: str = Field(min_length=2, max_length=50)
    image: str = Field(min_length=3, max_length=200)
    cpu_cores: float = Field(gt=0, le=4)
    memory_mb: int = Field(gt=0, le=8192)

@app.get("/")
def home():
    return {
        "project": "GreenOps",
        "message": "GreenOps Platform API is running",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/api/v1/info")
def platform_info():
    return {
        "platform": "GreenOps",
        "architecture": "Cloud-Native",
        "backend": "FastAPI",
        "scheduling": "Energy and SLA Aware",
        "phase": 1
    }

@app.post("/api/v1/deployments", status_code=201)
def create_deployment(request: DeploymentRequest):
    deployment_id = str(uuid4())

    deployment = {
        "deployment_id": deployment_id,
        "application_name": request.application_name,
        "image": request.image,
        "cpu_cores": request.cpu_cores,
        "memory_mb": request.memory_mb,
        "status": "PENDING",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    deployments[deployment_id] = deployment

    return deployment

@app.get("/api/v1/deployments")
def list_deployments():
    return {
        "total": len(deployments),
        "deployments": list(deployments.values())
    }

@app.get("/api/v1/deployments/{deployment_id}")
def get_deployment(deployment_id: str):
    deployment = deployments.get(deployment_id)

    if not deployment:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )

    return deployment
