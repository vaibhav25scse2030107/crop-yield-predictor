# Coding Rules & Standards

## 1. Python Style Guide (PEP 8)
*   Use 4 spaces for indentation (no tabs).
*   Limit lines to 88 characters (Black formatter standard).
*   Use `snake_case` for variables and functions.
*   Use `PascalCase` for classes.

## 2. Machine Learning Standards
*   **Reproducibility:** Always set `random_state=42` (or another fixed integer) in train/test splits and model initializations to ensure consistent results during evaluation.
*   **Data Leakage:** Never fit the `StandardScaler` or `OneHotEncoder` on the entire dataset. Always use `fit_transform` on training data and strictly `transform` on testing data.
*   **Pipeline Usage:** Enforce the use of `sklearn.pipeline.Pipeline` to bundle preprocessing and model training. This prevents preprocessing mismatches during deployment.

## 3. Version Control Workflow
*   Do not commit large datasets (`*.csv`, `*.zip`) or serialized models (`*.pkl`) to GitHub if they exceed 50MB. Add `data/` and `models/` to `.gitignore`.
*   Commit messages must be descriptive (e.g., "Add GradientBoosting model to training script" instead of "update code").