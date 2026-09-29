def validate_comparison(compare) -> dict:

    return {
        "passed": compare.matches(),
        "all_columns_match": compare.all_columns_match(),
        "all_rows_overlap": compare.all_rows_overlap(),
        "intersect_rows_match": compare.intersect_rows_match(),
    }