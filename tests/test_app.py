import os
from pathlib import Path


ARTIFACT_DIR = Path("artifacts")


def test_model_artifact_exists():
assert (ARTIFACT_DIR / "model.pkl").exists()