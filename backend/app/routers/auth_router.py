from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.schemas.user_schema import (
    UserRegister,
    UserLogin
)

from app.schemas.auth_schema import (
    TokenResponse
)

from app.core.dependencies import get_db

from app.services.user_service import (
    create_user
)

from app.services.auth_service import (
    authenticate_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    created_user = create_user(
        db=db,
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role_id=2
    )

    if not created_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return {
        "message": "User registered successfully",
        "email": created_user.email
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    token = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }