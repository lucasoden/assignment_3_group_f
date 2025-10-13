from __future__ import annotations
import json
from pathlib import Path


from joblib import dump
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


from .data import load_data
from .metrics import rmse


ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)


# Toggle here for v0.2 improvement
MODEL_KIND = "linear" # or "ridge"
MODEL_VERSION = "v0.1" # update to v0.2 in next iteration




def build_pipeline(model_kind: str = MODEL_KIND) -> Pipeline:
    # All features are numeric in this dataset
    numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    pre = ColumnTransformer(transformers=[("num", numeric_transformer, slice(0, 10))])


    if model_kind == "ridge":
        model = Ridge(alpha=1.0, random_state=42)
    else:
        model = LinearRegression()


    pipe = Pipeline(steps=[("pre", pre), ("model", model)])
    return pipe




def main():
    X_train, X_test, y_train, y_test = load_data()


    pipe = build_pipeline(MODEL_KIND)
    pipe.fit(X_train, y_train)


    y_pred = pipe.predict(X_test)
    score_rmse = rmse(y_test, y_pred)


    # Save model
    model_path = ARTIFACT_DIR / "model.pkl"
    dump(pipe, model_path)


    # Save metrics
    metrics = {
        "model_kind": MODEL_KIND,
        "model_version": MODEL_VERSION,
        "rmse": round(float(score_rmse), 4),
    }
    (ARTIFACT_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()