import os
import pandas as pd
from loguru import logger

RAW_PATH = "data/raw/ASRS_DBOnline.csv"
PROCESSED_DIR = "data/processed/asrs"
PROCESSED_PATH = f"{PROCESSED_DIR}/ASRS_clean.parquet"


def load_raw_csv():
    logger.info(f"Loading ASRS raw CSV → {RAW_PATH}")
    df = pd.read_csv(RAW_PATH, encoding="ISO-8859-1", low_memory=False)
    logger.success(f"Loaded {len(df)} rows")
    return df


def clean_asrs(df: pd.DataFrame):

    # Identify narrative fields
    narrative_cols = [c for c in df.columns if "report" in c.lower()]

    logger.info(f"Found {len(narrative_cols)} narrative segments")

    # Combine narrative text
    df["narrative"] = df[narrative_cols].astype(str).agg(" ".join, axis=1)

    # Keep metadata
    meta_cols = [c for c in df.columns if c.lower() in ["time", "place", "environment", "aircraft"]]

    # Minimal keep
    keep_cols = ["narrative"] + meta_cols

    df = df[keep_cols].copy()

    # Drop empty
    df["narrative"] = df["narrative"].str.strip()
    df = df[df["narrative"].notna() & (df["narrative"] != "")]
    df = df.drop_duplicates()

    logger.success(f"Cleaned → {len(df)} rows")
    return df


def save_parquet(df):
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df.to_parquet(PROCESSED_PATH, index=False)
    logger.success(f"Saved cleaned ASRS → {PROCESSED_PATH}")


def ingest_asrs():
    df = load_raw_csv()
    df = clean_asrs(df)
    save_parquet(df)


if __name__ == "__main__":
    ingest_asrs()
