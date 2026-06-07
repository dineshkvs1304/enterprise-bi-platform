import os
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.auth.current_user import (
    get_current_user
)

from app.services.dataset_service import (
    save_dataset
)

from app.services.analytics_service import (
    analyze_dataset
)

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"]
)

UPLOAD_FOLDER = "app/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/upload")
def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    dataset = save_dataset(
        db,
        file.filename,
        file_path,
        current_user.id
    )

    analysis = analyze_dataset(
        file_path
    )

    return {
        "dataset_id": dataset.id,
        "file_name": dataset.name,
        "uploaded_by": current_user.id,
        "analysis": analysis
    }