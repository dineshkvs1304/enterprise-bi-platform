from app.models.user import User
from app.security.security import hash_password


def create_user(
    db,
    full_name,
    email,
    password,
    role_id
):

    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return None

    new_user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        role_id=role_id
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user