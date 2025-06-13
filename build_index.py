
import faiss
import numpy as np

def build_hnsw_index(features):
    dim = features.shape[1]
    index = faiss.IndexHNSWFlat(dim, 32)
    index.hnsw.efConstruction = 40
    index.add(features)
    return index
