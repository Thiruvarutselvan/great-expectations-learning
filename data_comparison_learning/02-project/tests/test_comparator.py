import pandas as pd

from src.comparator import compare_datasets


def test_matching_data():

    df1 = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
    })

    df2 = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
    })

    compare = compare_datasets(
        df1,
        df2,
        join_columns=["id"],
    )

    assert compare.matches()


def test_mismatched_data():

    df1 = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
    })

    df2 = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 250],
    })

    compare = compare_datasets(
        df1,
        df2,
        join_columns=["id"],
    )

    assert not compare.matches()