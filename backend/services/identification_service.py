import numpy as np
from backend.services.face_service import extract_embedding
from backend.services.similarity_service import cosine_similarity
from backend.database.db_connection import users_collection, logs_collection
from backend.config.settings import SIMILARITY_THRESHOLD


def identify_user(image_path: str):
    captured_embedding = extract_embedding(image_path)

    best_score = 0
    best_user = None

    users = users_collection.find()

    for user in users:
        if "embedding" not in user:
            continue

        db_embedding = np.array(user["embedding"])
        score = cosine_similarity(captured_embedding, db_embedding)

        if score > best_score:
            best_score = score
            best_user = user["name"]

    if best_score > SIMILARITY_THRESHOLD:
        status = "Access Granted"
    else:
        best_user = "Unknown"
        status = "Access Denied"

    logs_collection.insert_one({
        "user_name": best_user,
        "similarity_score": float(best_score),
        "status": status
    })

    return {
        "name": best_user,
        "similarity_score": float(best_score),
        "status": status
    }
