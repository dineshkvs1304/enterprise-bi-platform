import pandas as pd

from app.models.dataset import Dataset


def revenue_profit_trend(
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

    revenue = (
        df["Revenue"]
        .tolist()
    )

    profit = (
        df["Profit"]
        .tolist()
    )

    return {
        "revenue_trend": revenue,
        "profit_trend": profit
    }