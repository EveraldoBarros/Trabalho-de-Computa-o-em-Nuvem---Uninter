from pydantic import BaseModel


class AttachmentRead(BaseModel):
    id: int
    workflow_id: int
    file_name: str
    storage_path: str
    storage_type: str

    class Config:
        from_attributes = True
