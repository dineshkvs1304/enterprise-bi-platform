from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.analytics.trend_service import (
    revenue_profit_trend
)

router = APIRouter(
    prefix="/trend",
    tags=["Trend Analytics"]
)


@router.get("/{dataset_id}")
def get_trend(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    result = revenue_profit_trend(
        db,
        dataset_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return result