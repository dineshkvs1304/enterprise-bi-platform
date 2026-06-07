from app.models.user import User

from app.security.security import (
    verify_password
)

from app.auth.jwt_handler import (
    create_access_token
)


def authenticate_user(
    db,
    email,
    password
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    token = create_access_token(
        {
            "sub": user.email,
            "role_id": user.role_id
        }
    )

    return token