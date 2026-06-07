from pydantic import BaseModel


class TokenResponse(BaseModel):

    access_token: str
    token_type: str


class UserProfile(BaseModel):

    id: int
    full_name: str
    email: str
    role_id: int