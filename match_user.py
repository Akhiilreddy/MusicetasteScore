
import numpy as np
import faiss

def match_playlists_similarity(features_a, features_b):
    if len(features_a) == 0 or len(features_b) == 0:
        raise ValueError("Empty features provided")

    dim = features_a.shape[1]
    index = faiss.IndexHNSWFlat(dim, 32)
    index.hnsw.efConstruction = 40
    index.add(features_a.astype("float32"))

    D, _ = index.search(features_b.astype("float32"), k=1)
    match_scores = 100 - D.flatten()
    return np.mean(match_scores)
