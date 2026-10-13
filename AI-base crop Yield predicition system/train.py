import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def load_or_generate_data(file_path="data/crop_yield.csv"):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    print("Generating synthetic Kaggle-style training data...")
    np.random.seed(42)
    n = 2000
    crops = ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane"]
    seasons = ["Kharif", "Rabi", "Whole Year"]
    regions = ["North", "South", "East", "West", "Central"]

    data = {
        "Crop": np.random.choice(crops, n),
        "Season": np.random.choice(seasons, n),
        "Region": np.random.choice(regions, n),
        "Rainfall_mm": np.random.uniform(200, 1500, n),
        "Temperature_C": np.random.uniform(15, 42, n),
        "Humidity_pct": np.random.uniform(30, 95, n),
        "Nitrogen_N": np.random.uniform(20, 140, n),
        "Phosphorus_P": np.random.uniform(10, 80, n),
        "Potassium_K": np.random.uniform(15, 75, n),
        "Soil_pH": np.random.uniform(5.0, 8.5, n),
    }
    df = pd.DataFrame(data)

    base_yield = (
        0.002 * df["Rainfall_mm"]
        + 0.05 * df["Nitrogen_N"]
        + 0.03 * df["Phosphorus_P"]
        - 0.04 * np.abs(df["Temperature_C"] - 27)
        - 0.5 * np.abs(df["Soil_pH"] - 6.5)
        + np.random.normal(0, 0.4, n)
    )
    df["Yield_tons_per_ha"] = np.maximum(0.5, np.round(base_yield, 2))
    os.makedirs("data", exist_ok=True)
    df.to_csv(file_path, index=False)
    return df

def train_and_export():
    df = load_or_generate_data()

    target = "Yield_tons_per_ha"
    categorical_features = ["Crop", "Season", "Region"]
    numerical_features = [
        "Rainfall_mm", "Temperature_C", "Humidity_pct", 
        "Nitrogen_N", "Phosphorus_P", "Potassium_K", "Soil_pH"
    ]

    X = df[categorical_features + numerical_features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ]
    )

    models = {
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=120, random_state=42),
        "XGBoost Regressor": XGBRegressor(n_estimators=150, learning_rate=0.1, random_state=42)
    }

    best_score = -float("inf")
    best_pipeline = None

    for name, model in models.items():
        pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", model)])
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)
        
        r2 = r2_score(y_test, predictions)
        print(f"{name} R²: {r2:.4f}")

        if r2 > best_score:
            best_score = r2
            best_pipeline = pipeline

    # Export Model
    os.makedirs("models", exist_ok=True)
    joblib.dump(best_pipeline, "models/yield_model_pipeline.pkl")
    
    # Extract & Export Feature Importances
    preprocessor_fitted = best_pipeline.named_steps["preprocessor"]
    model_fitted = best_pipeline.named_steps["regressor"]
    
    cat_features_out = preprocessor_fitted.named_transformers_["cat"].get_feature_names_out(categorical_features)
    all_feature_names = numerical_features + list(cat_features_out)
    
    importance_df = pd.DataFrame({
        "Feature": all_feature_names,
        "Importance": model_fitted.feature_importances_
    }).sort_values(by="Importance", ascending=False)
    
    importance_df.to_csv("models/feature_importances.csv", index=False)
    print(f"\n[Success] Exported pipeline and feature importances.")

if __name__ == "__main__":
    train_and_export()