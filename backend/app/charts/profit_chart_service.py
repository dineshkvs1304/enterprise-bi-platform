import os

import pandas as pd

import matplotlib.pyplot as plt

from app.models.dataset import Dataset


OUTPUT_FOLDER = "app/charts_output"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


def generate_profit_chart(
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

    profit_by_product = (
        df.groupby("Product")["Profit"]
        .sum()
    )

    plt.figure(
        figsize=(8, 5)
    )

    profit_by_product.plot(
        kind="bar"
    )

    plt.title(
        "Profit By Product"
    )

    plt.ylabel(
        "Profit"
    )

    plt.tight_layout()

    chart_path = (
        f"{OUTPUT_FOLDER}/profit_chart_{dataset_id}.png"
    )

    plt.savefig(
        chart_path
    )

    plt.close()

    return {
        "chart_path": chart_path
    }