import os
import pandas as pd
from loguru import logger
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT_PATH = "data/processed/asrs/ASRS_clustered.parquet"
OUTPUT_PATH = "data/processed/asrs/ASRS_keywords.parquet"
SUMMARY_PATH = "data/processed/asrs/ASRS_cluster_summary.csv"


def extract_top_keywords(df, top_n=12):
    logger.info("Extracting TF-IDF keywords per cluster...")

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=5000
    )

    df["narrative"] = df["narrative"].fillna("")
    X = vectorizer.fit_transform(df["narrative"])
    feature_names = vectorizer.get_feature_names_out()

    clusters = sorted(df["cluster"].unique())
    summary = []

    for c in clusters:
        row_ids = (df["cluster"] == c).values
        sub = X[row_ids]

        # Sum TF-IDF vocab weights for this cluster
        tfidf_sum = sub.sum(axis=0).A1

        top_idx = tfidf_sum.argsort()[::-1][:top_n]
        top_words = [feature_names[i] for i in top_idx]

        summary.append({
            "cluster": c,
            "keywords": ", ".join(top_words)
        })

    summary_df = pd.DataFrame(summary)
    return summary_df



def main():
    logger.info(f"Loading → {INPUT_PATH}")
    df = pd.read_parquet(INPUT_PATH)

    summary_df = extract_top_keywords(df, top_n=12)

    os.makedirs(os.path.dirname(SUMMARY_PATH), exist_ok=True)
    summary_df.to_csv(SUMMARY_PATH, index=False)

    logger.success(f"Saved → {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
