import logging
import yaml

from src.comparator import load_csv, compare_datasets
from src.validator import validate_comparison
from src.reporter import build_report, save_report


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main():

    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    for job in config["comparisons"]:

        logger.info("Starting comparison: %s", job["name"])

        source_df = load_csv(job["source"])
        target_df = load_csv(job["target"])

        compare = compare_datasets(
            source_df,
            target_df,
            join_columns=job["join_columns"],
            abs_tol=job.get("abs_tol", 0),
            rel_tol=job.get("rel_tol", 0),
        )

        validation = validate_comparison(compare)

        report = build_report(compare, validation)

        output_path = f"output/{job['name']}.json"

        save_report(report, output_path)

        logger.info(
            "Comparison complete: %s | status=%s",
            job["name"],
            "PASS" if validation["passed"] else "FAIL",
        )

        print(compare.report())


if __name__ == "__main__":
    main()