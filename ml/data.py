from __future__ import annotations
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split


def load_data(test_size: float = 0.2, random_state: int = 42):
Xy = load_diabetes(as_frame=True)
X = Xy.frame.drop(columns=["target"]) # features
y = Xy.frame["target"] # progression index
return train_test_split(X, y, test_size=test_size, random_state=random_state)