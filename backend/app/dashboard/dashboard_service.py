import pandas as pd

from app.models.dataset import Dataset

from app.analytics.kpi_engine import (
    generate_kpis
)


def generate_dashboard_summary(
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

    kpis = generate_kpis(df)

    summary = {
       "dataset_info": {
    "dataset_id": dataset.id,
    "file_path": dataset.file_path,
    "rows": len(df),
    "columns": len(df.columns)
},
        "kpis": kpis,

        "executive_summary": {
            "best_product": kpis["best_product"],
            "profit_margin": kpis["profit_margin"],
            "total_revenue": kpis["total_revenue"],
            "total_profit": kpis["total_profit"]
        }
    }

    return summary