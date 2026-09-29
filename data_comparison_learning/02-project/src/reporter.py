import json
from pathlib import Path


def build_report(compare, validation: dict) -> dict:

    return {
        "validation": validation,
        "mismatch_count": len(compare.all_mismatch()),
        "df1_unique_columns": compare.df1_unq_columns(),
        "df2_unique_columns": compare.df2_unq_columns(),
    }


def save_report(report: dict, path: str):

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump(report, f, indent=2, default=str)