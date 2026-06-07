import pandas as pd


def generate_kpis(df: pd.DataFrame):

    revenue_column = "Revenue"

    profit_column = "Profit"

    total_revenue = float(
        df[revenue_column].sum()
    )

    total_profit = float(
        df[profit_column].sum()
    )

    average_revenue = float(
        df[revenue_column].mean()
    )

    average_profit = float(
        df[profit_column].mean()
    )

    profit_margin = round(
        (total_profit / total_revenue) * 100,
        2
    )

    best_product = (
        df.loc[
            df[profit_column].idxmax()
        ]["Product"]
    )

    worst_product = (
        df.loc[
            df[profit_column].idxmin()
        ]["Product"]
    )

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "average_revenue": average_revenue,
        "average_profit": average_profit,
        "profit_margin": profit_margin,
        "best_product": best_product,
        "worst_product": worst_product
    }