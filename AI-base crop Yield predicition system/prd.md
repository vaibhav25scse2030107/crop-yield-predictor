# Product Requirements Document (PRD)
**Project Name:** AI-base crop Yield predicition system
**Version:** 1.0

## 1. Problem Statement
Farmers and agricultural stakeholders often lack accessible, data-driven tools to accurately forecast crop yields. Unpredictable environmental conditions and soil variations make traditional estimation methods unreliable, leading to financial risks and inefficient resource allocation.

## 2. Target Audience
*   **Farmers & Agronomists:** To optimize crop selection and resource planning based on soil and weather.
*   **Agricultural Planners/Government Agencies:** To forecast regional food production.
*   **University Panel/Evaluators:** To assess the technical execution of this final-year academic project.

## 3. Core Features
*   **Input Interface:** A web-based form to accept categorical (Crop, Season, Region) and numerical (Rainfall, Temperature, Humidity, N-P-K levels, pH) inputs.
*   **ML Prediction Engine:** A trained regression model capable of predicting yield in tons/hectare based on the provided inputs.
*   **Data Processing Pipeline:** Automated scaling and encoding of user inputs to match the model's training schema.
*   **Results Dashboard:** Visual display of the predicted yield with context (e.g., optimal pH deviations).

## 4. Success Metrics
*   **Model Accuracy:** Achieve an R-squared ($R^2$) score of > 0.85 on the test dataset.
*   **Latency:** Model inference and UI update must occur within < 2 seconds.
*   **Usability:** End-users should be able to generate a prediction in under 3 clicks without technical knowledge.