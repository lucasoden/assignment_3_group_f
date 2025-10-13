from sklearn.datasets import load_diabetes

def test_load_and_print():
    Xy = load_diabetes(as_frame=True)
    X = Xy.frame.drop(columns=["target"])
    y = Xy.frame["target"]

    print(X)
    print(y)
    assert len(X) > 0  # just a simple assertion for the test to pass