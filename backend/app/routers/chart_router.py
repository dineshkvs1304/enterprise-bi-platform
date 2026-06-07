from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.charts.chart_service import (
    generate_revenue_chart
)

router = APIRouter(
    prefix="/charts",
    tags=["Charts"]
)


@router.get("/revenue/{dataset_id}")
def revenue_chart(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    result = generate_revenue_chart(
        db,
        dataset_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return result