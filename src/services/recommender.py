import json
from pathlib import Path
from typing import List, Dict, Any, Tuple

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class StaySenseRecommender:
    """
    Turns each listing into a vector (a list of numbers),
    stores them in a FAISS index, and finds the most similar ones.
    """

    def __init__(self, data_path: str = "data/listings.json", model_name: str = "all-MiniLM-L6-v2"):
        pass