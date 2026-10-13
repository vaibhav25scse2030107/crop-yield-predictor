from pathlib import Path

import joblib
import pandas as pd
import pytest


MODEL_PATH = Path(__file__).resolve().parent / "models" / "yield_model_pipeline.pkl"


@pytest.fixture
def model():
    assert MODEL_PATH.exists(), "Model file missing. Run train.py first."
    return joblib.load(MODEL_PATH)


def make_sample(**overrides):
    sample = {
        "Crop": "Wheat",
        "Season": "Rabi",
        "Region": "North",
        "Rainfall_mm": 500.0,
        "Temperature_C": 22.0,
        "Humidity_pct": 55.0,
        "Nitrogen_N": 80.0,
        "Phosphorus_P": 40.0,
        "Potassium_K": 35.0,
        "Soil_pH": 6.8,
    }
    sample.update(overrides)
    return pd.DataFrame([sample])


def test_pipeline_prediction_shape_and_positive_yield(model):
    prediction = model.predict(make_sample())

    assert len(prediction) == 1
    assert isinstance(float(prediction[0]), float)
    assert prediction[0] > 0, "Predicted yield must be strictly positive."


def test_pipeline_unseen_category(model):
    sample = make_sample(
        Crop="UnknownCrop",
        Season="UnknownSeason",
        Region="UnknownRegion",
        Rainfall_mm=600.0,
        Temperature_C=25.0,
        Humidity_pct=60.0,
        Nitrogen_N=50.0,
        Phosphorus_P=30.0,
        Potassium_K=30.0,
        Soil_pH=7.0,
    )

    prediction = model.predict(sample)

    assert len(prediction) == 1


@pytest.mark.parametrize(
    "overrides",
    [
        {"Rainfall_mm": -500.0},
        {"Soil_pH": 14.0},
    ],
    ids=["negative-rainfall", "extreme-soil-ph"],
)
def test_pipeline_extreme_numeric_inputs_produce_finite_prediction(model, overrides):
    prediction = model.predict(make_sample(**overrides))

    assert len(prediction) == 1
    assert pd.notna(prediction[0])
    assert float("-inf") < prediction[0] < float("inf")
