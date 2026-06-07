import pandas as pd

from app.models.dataset import Dataset


def product_analysis(db, dataset_id: int):

    dataset = (
        db.query(Dataset)
        .filter(Dataset.id == dataset_id)
        .first()
    )

    if not dataset:
        return None

    df = pd.read_csv(dataset.file_path)

    revenue_by_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    profit_by_product = (
        df.groupby("Product")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    return {
        "top_products_by_revenue":
            revenue_by_product.to_dict(),

        "top_products_by_profit":
            profit_by_product.to_dict(),

        "best_product":
            revenue_by_product.idxmax(),

        "worst_product":
            revenue_by_product.idxmin()
    }