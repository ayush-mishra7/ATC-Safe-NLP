import os
import pandas as pd
from loguru import logger

CLUSTERED = "data/processed/asrs/ASRS_labeled.parquet"
KEYWORDS  = "data/processed/asrs/ASRS_cluster_summary.csv"
OUT_CSV   = "data/exports/ASRS_tableau.csv"

def main():
    logger.info(f"Loading {CLUSTERED}")
    df = pd.read_parquet(CLUSTERED)

    # keep tidy columns for BI
    keep = [
        "narrative", "phase", "aircraft_type", "airport",
        "umap_x", "umap_y", "cluster", "cluster_label"
    ]
    keep = [c for c in keep if c in df.columns]
    df = df[keep].copy()

    # join cluster keywords (optional but useful)
    if os.path.exists(KEYWORDS):
        kw = pd.read_csv(KEYWORDS)
        df = df.merge(kw, on="cluster", how="left")  # adds 'keywords'

    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    logger.success(f"Exported → {OUT_CSV} ({df.shape[0]} rows)")

if __name__ == "__main__":
    main()
