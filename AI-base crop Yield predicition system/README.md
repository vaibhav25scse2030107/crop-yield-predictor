# AI-Based Crop Yield Prediction System

An interactive Streamlit application that estimates crop yield from crop,
season, region, weather, and soil nutrient inputs. The preprocessing steps and
trained regressor are exported together as a scikit-learn pipeline.

The exported model was trained with scikit-learn 1.9.1, which is pinned in
`requirements.txt` to keep the deployed pipeline compatible.

## Run locally

Use a Python environment compatible with the installed scikit-learn and
XGBoost dependencies:

```bash
python -m pip install -r requirements.txt
python train.py
streamlit run app.py
```

`train.py` reads `data/crop_yield.csv` when present and exports the fitted
pipeline and feature importances to `models/`.

## Automated validation

Install the development dependencies and run the pipeline tests:

```bash
python -m pip install -r requirements-dev.txt
pytest test_pipeline.py
```

The tests verify a normal positive prediction, handling of categories not seen
during training, and finite predictions for negative rainfall and an extreme
soil pH value. The edge-case tests check pipeline resilience; they do not mean
those out-of-range values are agronomically valid.

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository and push this project. If initializing Git for
   the first time, run these commands from the project directory:

   ```bash
   git init
   git add .
   git commit -m "feat: complete crop yield prediction system"
   git branch -M main
   git remote add origin https://github.com/<your-username>/crop-yield-predictor.git
   git push -u origin main
   ```

   The app loads `models/yield_model_pipeline.pkl` at startup, so ensure the
   trained model is present and included in the repository. `.gitignore`
   excludes other pickle files but explicitly permits this deployment artifact.
   The source dataset `data/crop_yield.csv` is also allowlisted.

2. In [Streamlit Community Cloud](https://share.streamlit.io/), select **Create
   app**, authorize GitHub if needed, and choose the repository, `main` branch,
   and `app.py` as the main file.
3. Deploy the app. Community Cloud installs the packages listed in
   `requirements.txt`; keep the Python environment compatible with those used
   to create the committed serialized model. If ML dependencies change,
   retrain the model and rerun the validation suite before deploying.
4. After deployment, open the app URL and verify that a prediction and the
   feature-importance chart load successfully.
