from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.core.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    role = relationship(
        "Role",
        back_populates="users"
    )

    datasets = relationship(
        "Dataset",
        back_populates="user"
    )

    reports = relationship(
        "Report",
        back_populates="user"
    )

    audit_logs = relationship(
        "AuditLog",
        back_populates="user"
    )