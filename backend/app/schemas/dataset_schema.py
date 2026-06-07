from pydantic import BaseModel


class DatasetResponse(BaseModel):

    id: int

    name: str

    file_path: str

    uploaded_by: int