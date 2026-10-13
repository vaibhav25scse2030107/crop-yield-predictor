# UI/UX Design Guidelines

## 1. Design Philosophy
The interface must be clean, highly accessible, and agricultural-themed. It should minimize cognitive load for non-technical users by organizing inputs logically.

## 2. Layout Structure (Streamlit)
*   **Header:** Bold title with an emoji (🌾) and a brief subtitle explaining the tool's purpose.
*   **Input Section (3 Columns):**
    *   *Column 1 (Agronomic):* Dropdowns for Crop Type, Season, and Region.
    *   *Column 2 (Weather):* Sliders for Rainfall (mm), Temperature (°C), and Humidity (%). Sliders provide natural bounds to prevent impossible inputs (e.g., -500 mm rainfall).
    *   *Column 3 (Soil):* Number inputs for N, P, K, and a slider for soil pH.
*   **Action Area:** A prominent, full-width "Calculate Yield Prediction" button.
*   **Output Section:** A clearly highlighted success box displaying the predicted yield in bold, followed by contextual metrics (e.g., rainfall levels compared to baseline).

## 3. Color & Theme
*   Leverage Streamlit's default light theme for high readability.
*   Use semantic colors for outputs: Green (`st.success`) for successful predictions, Red (`st.error`) for missing models or invalid inputs.