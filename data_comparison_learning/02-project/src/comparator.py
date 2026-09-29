import pandas as pd
from datacompy import PandasCompare


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compare_datasets(
    source_df: pd.DataFrame,
    target_df: pd.DataFrame,
    join_columns: list[str],
    abs_tol: float = 0,
    rel_tol: float = 0,
) -> PandasCompare:

    return PandasCompare(
        source_df,
        target_df,
        join_columns=join_columns,
        abs_tol=abs_tol,
        rel_tol=rel_tol,
    )