from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.core.base import Base


class KPI(Base):

    __tablename__ = "kpis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    dataset_id = Column(
        Integer,
        ForeignKey("datasets.id")
    )

    metric_name = Column(
        String(100),
        nullable=False
    )

    metric_value = Column(
        Float,
        nullable=False
    )

    dataset = relationship(
        "Dataset",
        back_populates="kpis"
    )