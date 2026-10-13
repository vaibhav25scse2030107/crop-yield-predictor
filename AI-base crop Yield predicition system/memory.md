# Project Context & Memory

## Project Overview
This repository contains the codebase for an AI-base crop Yield predicition system, designed as a final-year university project. The goal is to build an end-to-end machine learning lifecycle, from data ingestion to a deployed web interface.

## Key Decisions & Rationale
*   **Model Upgrade:** Transitioned from basic estimators to an XGBoost Regressor inside a Scikit-Learn Pipeline. XGBoost handles tabular agricultural anomalies (like unexpected rainfall spikes) much better than standard Random Forests.
*   **Model Transparency (Explainability):** Added a feature importance extraction step in `train.py` that dumps weights to a CSV. The UI now reads this and renders a chart. This proves to the university panel that the model isn't a "black box" and relies logically on soil nutrients and rainfall rather than arbitrary data.

## Current State
*   Machine learning pipeline and web UI are fully built and connected.
*   Interactive visualizations are implemented on the frontend.
*   *Next Immediate Action:* Test the application locally by running the new `train.py` and `app.py`, then proceed to Cloud Deployment.