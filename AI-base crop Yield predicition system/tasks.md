# Project Task Tracker

## 1. Setup & Data 
- [x] Define project scope and core requirements.
- [x] Locate and download historical crop yield dataset schema (N-P-K, Weather).
- [x] Initialize Git repository and project folder structure.
- [x] Setup `requirements.txt` and virtual environment.

## 2. Exploratory Data Analysis & Preprocessing
- [x] Handle missing values and baseline data generation.
- [x] Implement `OneHotEncoder` for categorical strings (Crop, Season, Region).
- [x] Implement `StandardScaler` for continuous numerical features.

## 3. Model Development
- [x] Split data into 80% training / 20% testing.
- [x] Train baseline and ensemble models (Random Forest, Gradient Boosting).
- [x] **[NEW] Train advanced XGBoost Regressor.**
- [x] Integrate preprocessing and best model into a Scikit-Learn `Pipeline`.
- [x] **[NEW] Extract feature importance weights to a CSV file.**
- [x] Export final pipeline to `models/yield_model_pipeline.pkl`.

## 4. UI Development & Deployment
- [x] Build basic Streamlit layout (Input columns).
- [x] Connect `app.py` to the serialized `.pkl` model.
- [x] Implement prediction logic and result formatting.
- [x] **[NEW] Integrate Model Interpretability (Feature Importance Bar Chart).**
- [ ] Deploy application to Streamlit Community Cloud or Render.

## 5. Documentation & Final Delivery
- [ ] Complete final university project report.
- [ ] Create system architecture diagrams for presentation.
- [ ] Prepare live demo script for the evaluation panel.