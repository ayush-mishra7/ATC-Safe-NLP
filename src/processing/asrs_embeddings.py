import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from loguru import logger

INPUT_PATH = "data/processed/asrs/ASRS_structured.parquet"
OUTPUT_PATH = "data/processed/asrs/ASRS_embeddings.parquet"


def compute_embeddings(texts):
    logger.info("Loading embedding model...")
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    logger.info("Computing embeddings...")
    emb = model.encode(texts, show_progress_bar=True)
    return emb


def main():
    logger.info(f"Loading structured file → {INPUT_PATH}")
    df = pd.read_parquet(INPUT_PATH)

    narratives = df["narrative"].tolist()

    emb = compute_embeddings(narratives)

    logger.success("Embeddings complete. Adding to dataframe.")

    df["embedding"] = emb.tolist()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)

    logger.success(f"Saved embeddings → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
