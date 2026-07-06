from pydantic import BaseModel
from typing import Optional


class WorkflowCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "open"
    priority: str = "medium"
    owner_id: Optional[int] = None


class WorkflowUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None


class WorkflowRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    owner_id: Optional[int]

    class Config:
        from_attributes = True
