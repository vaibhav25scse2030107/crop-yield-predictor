# System Architecture

## 1. High-Level Architecture
The system follows a localized client-server architecture built entirely in Python. The Streamlit framework serves as both the frontend UI and the backend controller, bridging user inputs with the serialized machine learning model.

## 2. Data Flow
1.  **User Input:** The user enters environmental and soil data via the Streamlit web UI.
2.  **Data Structuring:** Streamlit captures the inputs and structures them into a Pandas DataFrame.
3.  **Preprocessing Pipeline:** The DataFrame is passed through the `ColumnTransformer` (loaded via Joblib).
    *   *Numerical Features:* Scaled using `StandardScaler`.
    *   *Categorical Features:* Transformed using `OneHotEncoder`.
4.  **Model Inference:** The preprocessed data array is passed to the trained `RandomForestRegressor` / `GradientBoostingRegressor`.
5.  **Output Display:** The model returns a float value (Yield in tons/hectare), which Streamlit renders on the UI.

## 3. Technology Stack
*   **Language:** Python 3.8+
*   **Data Processing:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (Pipelines, Transformers, Ensembles)
*   **Model Serialization:** Joblib
*   **Web Framework:** Streamlit
*   **Version Control:** Git / GitHub