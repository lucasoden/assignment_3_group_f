from ml.train import build_pipeline


def test_build_pipeline():
pipe = build_pipeline("linear")
assert pipe is not None