from deepface import DeepFace
import numpy as np


def extract_embedding(image_path: str):
    embedding = DeepFace.represent(
        img_path=image_path,
        model_name="ArcFace",
        detector_backend="retinaface",
        enforce_detection=True
    )[0]["embedding"]

    return np.array(embedding)
