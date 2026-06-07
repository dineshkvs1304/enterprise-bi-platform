from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db
)

from app.services.kpi_service import (
    get_dataset_kpis
)

router = APIRouter(
    prefix="/kpi",
    tags=["KPI Engine"]
)


@router.get("/{dataset_id}")
def calculate_kpis(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    kpis = get_dataset_kpis(
        db,
        dataset_id
    )

    if kpis is None:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return {
        "dataset_id": dataset_id,
        "kpis": kpis
    }