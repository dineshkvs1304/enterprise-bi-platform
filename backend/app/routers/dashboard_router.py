from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db
)

from app.dashboard.dashboard_service import (
    generate_dashboard_summary
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary/{dataset_id}")
def dashboard_summary(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    result = generate_dashboard_summary(
        db,
        dataset_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return result