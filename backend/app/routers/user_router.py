from fastapi import (
    APIRouter,
    Depends
)

from app.auth.current_user import (
    get_current_user
)

from app.schemas.auth_schema import (
    UserProfile
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/me",
    response_model=UserProfile
)
def get_me(
    current_user=Depends(
        get_current_user
    )
):

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role_id": current_user.role_id
    }