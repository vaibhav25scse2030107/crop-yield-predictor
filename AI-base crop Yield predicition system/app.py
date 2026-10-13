import os
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Crop Yield Predictor", layout="wide")

MODEL_PATH = "models/yield_model_pipeline.pkl"
IMPORTANCE_PATH = "models/feature_importances.csv"

@st.cache_resource
def load_assets():
    model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
    importances = pd.read_csv(IMPORTANCE_PATH) if os.path.exists(IMPORTANCE_PATH) else None
    return model, importances

pipeline, importance_df = load_assets()

st.title("🌾 AI-Based Crop Yield Prediction System")
st.markdown("Estimate agricultural crop production using environmental parameters, soil nutrients, and regional variables.")

if pipeline is None:
    st.error("Model file not found. Run `python train.py` first to train and export the model.")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Field & Season")
    crop = st.selectbox("Crop Type", ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane"])
    season = st.selectbox("Season", ["Kharif", "Rabi", "Whole Year"])
    region = st.selectbox("Region", ["North", "South", "East", "West", "Central"])

with col2:
    st.subheader("Weather Conditions")
    rainfall = st.slider("Rainfall (mm)", 100.0, 2500.0, 850.0)
    temperature = st.slider("Temperature (°C)", 10.0, 50.0, 28.0)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 65.0)

with col3:
    st.subheader("Soil Chemistry")
    n = st.number_input("Nitrogen (N) kg/ha", 0.0, 200.0, 80.0)
    p = st.number_input("Phosphorus (P) kg/ha", 0.0, 150.0, 40.0)
    k = st.number_input("Potassium (K) kg/ha", 0.0, 150.0, 40.0)
    ph = st.slider("Soil pH", 4.0, 9.5, 6.8, step=0.1)

st.write("---")

# Prediction Execution
if st.button("Calculate Yield Prediction", use_container_width=True):
    input_df = pd.DataFrame([{
        "Crop": crop, "Season": season, "Region": region,
        "Rainfall_mm": rainfall, "Temperature_C": temperature, "Humidity_pct": humidity,
        "Nitrogen_N": n, "Phosphorus_P": p, "Potassium_K": k, "Soil_pH": ph
    }])

    predicted_yield = pipeline.predict(input_df)[0]
    
    st.success(f"### Predicted Crop Yield: **{predicted_yield:.2f} tons / hectare**")

# Visual Analytics Section
if importance_df is not None:
    st.write("---")
    st.subheader("📊 Model Feature Interpretability")
    st.markdown("This chart indicates which environmental and soil factors the AI weighs most heavily when calculating the yield.")
    
    # Format dataframe for Streamlit bar chart
    top_features = importance_df.head(10).set_index("Feature")
    st.bar_chart(top_features)