import os

from app.models.dataset import Dataset


UPLOAD_FOLDER = "app/uploads"


def save_dataset(
    db,
    filename,
    filepath,
    user_id
):

    dataset = Dataset(
        name=filename,
        file_path=filepath,
        uploaded_by=user_id
    )

    db.add(dataset)

    db.commit()

    db.refresh(dataset)

    return dataset