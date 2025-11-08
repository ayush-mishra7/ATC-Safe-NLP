import os
import pandas as pd
from loguru import logger

INPUT_PATH = "data/processed/asrs/ASRS_clustered.parquet"
OUTPUT_PATH = "data/processed/asrs/ASRS_labeled.parquet"


CLUSTER_LABELS = {
    0: "Approach / Terrain Awareness",
    1: "Hazmat / Dangerous Goods",
    2: "Taxi / Ramp Ground Ops",
    3: "Engine / Fuel / Mechanical",
    4: "NMAC / Traffic Pattern",
    5: "Runway Ops / Clearance",
    6: "Cabin / Smoke / Maintenance",
    7: "Training / Student Landing",
    8: "Landing Gear / Mechanical",
    9: "Altitude / ATC Comm",
    10: "Drone / Unauthorized Airspace",
    11: "Weather / Wake Turbulence"
}


def main():
    logger.info(f"Loading → {INPUT_PATH}")
    df = pd.read_parquet(INPUT_PATH)

    df["cluster_label"] = df["cluster"].map(CLUSTER_LABELS)

    # Save
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)

    logger.success(f"Saved labeled data → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
