from pathlib import Path
import shutil
import boto3
from fastapi import UploadFile
from app.core.config import UPLOAD_MODE, LOCAL_UPLOAD_DIR, AWS_REGION, AWS_S3_BUCKET


def save_file(file: UploadFile, workflow_id: int) -> tuple[str, str]:
    if UPLOAD_MODE == "s3":
        key = f"workflows/{workflow_id}/{file.filename}"
        s3 = boto3.client("s3", region_name=AWS_REGION)
        s3.upload_fileobj(file.file, AWS_S3_BUCKET, key)
        return f"s3://{AWS_S3_BUCKET}/{key}", "s3"

    upload_dir = Path(LOCAL_UPLOAD_DIR) / str(workflow_id)
    upload_dir.mkdir(parents=True, exist_ok=True)
    destination = upload_dir / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(destination), "local"
