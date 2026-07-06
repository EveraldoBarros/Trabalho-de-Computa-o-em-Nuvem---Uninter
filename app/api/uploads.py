from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workflow import Workflow
from app.models.attachment import Attachment
from app.schemas.attachment import AttachmentRead
from app.services.storage import save_file

router = APIRouter(prefix="/uploads", tags=["Uploads"])


@router.post("/{workflow_id}", response_model=AttachmentRead)
def upload_file(workflow_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Fluxo não encontrado.")

    storage_path, storage_type = save_file(file, workflow_id)
    attachment = Attachment(
        workflow_id=workflow_id,
        file_name=file.filename,
        storage_path=storage_path,
        storage_type=storage_type,
    )
    db.add(attachment)
    db.commit()
    db.refresh(attachment)
    return attachment


@router.get("", response_model=list[AttachmentRead])
def list_uploads(db: Session = Depends(get_db)):
    return db.query(Attachment).all()
