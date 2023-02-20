from pathlib import Path


class Config:
    # Data paths
    RAW_PATH = Path("data/raw")
    PREPROCESSED_PATH = Path("data/preprocessed")

    RAW_INTERACTIONS_PATH = RAW_PATH / "interactions.csv"
    RAW_ITEMS_PATH = RAW_PATH / "items.csv"
    RAW_USERS_PATH = RAW_PATH / "users.csv"

    PREPROCESSED_INTERACTIONS_PATH = PREPROCESSED_PATH / "interactions.pickle"
    PREPROCESSED_ITEMS_PATH = PREPROCESSED_PATH / "items.pickle"
    PREPROCESSED_USERS_PATH = PREPROCESSED_PATH / "users.pickle"

    # Model paths
    MODEL_PATH = Path("models")
    BASELINE_PATH = MODEL_PATH / "baseline.pickle"
    IMPLICIT_PATH = MODEL_PATH / "als.pickle"

    # Business parameters
    K = 10
    BASE_RECS_COUNT = 30
    TEST_DAYS = 7