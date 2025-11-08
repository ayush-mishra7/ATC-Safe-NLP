import os
import pandas as pd
from loguru import logger
from sklearn.cluster import KMeans
import umap

INPUT_PATH = "data/processed/asrs/ASRS_embeddings.parquet"
OUTPUT_PATH = "data/processed/asrs/ASRS_clustered.parquet"


def reduce_dim(embeddings):
    logger.info("UMAP: reducing embedding dimensions...")
    reducer = umap.UMAP(n_neighbors=20, min_dist=0.3, metric='cosine')
    emb_2d = reducer.fit_transform(embeddings)
    return emb_2d


def cluster(emb_2d, k=12):
    logger.info(f"KMeans clustering → k={k}")
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(emb_2d)
    return labels


def main():
    logger.info(f"Loading → {INPUT_PATH}")
    df = pd.read_parquet(INPUT_PATH)

    embeddings = df["embedding"].tolist()

    # UMAP reduction
    emb_2d = reduce_dim(embeddings)
    df["umap_x"] = [x[0] for x in emb_2d]
    df["umap_y"] = [x[1] for x in emb_2d]

    # KMeans clustering
    labels = cluster(emb_2d, k=12)
    df["cluster"] = labels

    # Save
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)

    logger.success(f"Saved clustered file → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
