import numpy as np
from backend.services.face_service import extract_embedding
from backend.database.db_connection import users_collection


def enroll_user(name: str, image_paths: list):
    embeddings = []

    for path in image_paths:
        emb = extract_embedding(path)
        embeddings.append(emb)

    avg_embedding = np.mean(embeddings, axis=0)

    users_collection.insert_one({
        "name": name,
        "embedding": avg_embedding.tolist()
    })

    return True
