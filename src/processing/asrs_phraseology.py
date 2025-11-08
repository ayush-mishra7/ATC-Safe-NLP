import re
import pandas as pd
from loguru import logger
import os

INPUT_PATH = "data/processed/asrs/ASRS_clean.parquet"
OUTPUT_PATH = "data/processed/asrs/ASRS_structured.parquet"


# Extract fields using simple rule-based NLP
def extract_phase(text: str):
    phases = {
        "taxi": "Taxi",
        "takeoff": "Takeoff",
        "departure": "Departure",
        "climb": "Climb",
        "cruise": "Cruise",
        "descent": "Descent",
        "approach": "Approach",
        "landing": "Landing"
    }
    for k, v in phases.items():
        if k in text.lower():
            return v
    return None


def extract_aircraft(text: str):
    """
    Looks for known aircraft type patterns
    """
    pattern = r"\b(A3\d{2}|B7\d{2}|B73\d|B75\d|C\d{3}|E\d{3})\b"
    m = re.search(pattern, text.upper())
    if m:
        return m.group(0)
    return None


def extract_airport(text: str):
    """
    Search for ICAO / IATA airport identifiers
    """
    pattern = r"\b([A-Z]{3}|[A-Z]{4})\b"
    m = re.findall(pattern, text.upper())
    if m:
        return m[0]
    return None


def process_asrs(df: pd.DataFrame):
    logger.info("Extracting fields from ASRS narratives...")

    df["phase"] = df["narrative"].apply(extract_phase)
    df["aircraft_type"] = df["narrative"].apply(extract_aircraft)
    df["airport"] = df["narrative"].apply(extract_airport)

    logger.success("Extraction complete.")
    return df


def main():
    logger.info(f"Loading → {INPUT_PATH}")
    df = pd.read_parquet(INPUT_PATH)

    df = process_asrs(df)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)

    logger.success(f"Saved structured file → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
