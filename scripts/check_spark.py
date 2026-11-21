from pathlib import Path

from pyspark.sql import SparkSession


def main():
    root = Path(__file__).resolve().parents[1]
    sample = root / "data/raw/data/data_20250501.txt"
    spark = SparkSession.builder.master("local[2]").appName("FunnelLag-check").getOrCreate()
    try:
        print(f"Spark {spark.version}")
        rows = spark.read.text(sample.as_uri()).take(5)
        if len(rows) < 5:
            raise ValueError(f"Expected at least five records in {sample.name}")
        for number, row in enumerate(rows, start=1):
            fields = row.value.split("\t")
            print(f"Row {number}: {len(fields)} columns, first three = {fields[:3]}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
