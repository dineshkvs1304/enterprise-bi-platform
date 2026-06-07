import pandas as pd

from app.analytics.kpi_engine import (
    generate_kpis
)

from app.models.dataset import Dataset


def get_dataset_kpis(
    db,
    dataset_id
):

    dataset = (
        db.query(Dataset)
        .filter(
            Dataset.id == dataset_id
        )
        .first()
    )

    if not dataset:
        return None

    df = pd.read_csv(
        dataset.file_path
    )

    return generate_kpis(df)