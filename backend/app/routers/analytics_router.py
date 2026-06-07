from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.analytics.analytics_service import (
    product_analysis
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/products/{dataset_id}")
def analyze_products(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    result = product_analysis(
        db,
        dataset_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return result