# 🌍 Machine Learning-Based Urban Heat Island Prediction Using Multi-Source Geospatial and Remote Sensing Data

### A Case Study of Delhi

## 📌 Overview

Urban Heat Island (UHI) is an environmental phenomenon in which urban areas experience higher temperatures than their surrounding rural regions due to urbanization, infrastructure development, reduced vegetation, and human activities.

This project presents a **machine learning-based framework for predicting Urban Heat Island intensity across Delhi, India**, using multi-source satellite imagery, geospatial information, and meteorological data.

The system integrates remote sensing indices, geographical parameters, and weather variables to predict Land Surface Temperature (LST). An interactive **Streamlit dashboard** enables users to explore predictions and visualize factors contributing to urban heat patterns.

## 🎥 Project Demo

[▶️ Watch the Project Demo on YouTube]([https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://www.youtube.com/watch?v=9SK6O2fuL5Q))

## 🎯 Objectives

- Analyze the Urban Heat Island phenomenon across Delhi.
- Integrate satellite-derived, geospatial, and meteorological datasets.
- Identify environmental and geographical factors influencing Land Surface Temperature.
- Develop and compare multiple machine learning regression models.
- Build an interactive dashboard for visualizing and predicting UHI-related parameters.

## 🛰️ Data Sources

The study focuses on **NCT Delhi, India**, using data collected for the period **April–June 2024**.

| Data source | Description |
|---|---|
| Landsat 8 Collection 2 Level-2 | Satellite imagery at 30 m resolution |
| Google Earth Engine | Satellite data processing and extraction |
| Meteorological data | Air temperature, humidity, and wind speed |
| Geospatial datasets | Elevation, slope, population density, and distance to water |

## 🔍 Features Used

The following features were incorporated into the prediction dataset:

| Feature | Description |
|---|---|
| NDVI | Normalized Difference Vegetation Index |
| NDBI | Normalized Difference Built-up Index |
| MNDWI | Modified Normalized Difference Water Index |
| LULC | Land Use and Land Cover |
| Elevation | Height above sea level |
| Slope | Terrain inclination |
| Population Density | Population concentration |
| Air Temperature | Ambient atmospheric temperature |
| Humidity | Atmospheric moisture level |
| Wind Speed | Wind movement |
| Distance to Water | Proximity to nearby water bodies |
| Latitude & Longitude | Geographic coordinates |

## ⚙️ Methodology

The project follows a structured machine learning workflow:

1. **Data Collection:** Acquired satellite imagery and supporting geospatial and meteorological datasets.
2. **Data Preprocessing:** Processed satellite imagery, extracted relevant indices, and prepared the prediction dataset.
3. **Feature Engineering:** Integrated environmental, geographical, and meteorological parameters.
4. **Exploratory Data Analysis:** Examined feature distributions, relationships, and spatial patterns.
5. **Model Development:** Trained multiple regression algorithms to predict Land Surface Temperature.
6. **Model Evaluation:** Compared models using R², RMSE, and MAE.
7. **Hyperparameter Tuning:** Improved model performance through parameter optimization.
8. **Deployment:** Developed an interactive Streamlit application for prediction and visualization.

## 🤖 Machine Learning Models

Three regression models were implemented and evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

### Model Performance

| Model | R² Score | RMSE (°C) | MAE (°C) |
|---|---:|---:|---:|
| Linear Regression | 0.74 | 1.72 | 1.33 |
| Random Forest | 0.83 | 1.35 | 1.02 |
| XGBoost | **0.85** | **1.27** | **0.96** |

**XGBoost achieved the best performance** among the evaluated models, with an R² score of 0.85, RMSE of 1.27°C, and MAE of 0.96°C.

## 📊 Explainable AI

SHAP (SHapley Additive exPlanations) was used to understand the contribution of individual features to model predictions.

The important features identified included:

- NDBI
- Longitude
- Latitude
- MNDWI
- NDVI

This analysis helps interpret how built-up areas, vegetation, water-related indices, and geographical location contribute to predicted temperature patterns.

*Note: Feature importance indicates model associations and does not establish causation.*

## 🖥️ Interactive Streamlit Dashboard

An interactive web application was developed using Streamlit to make the prediction system accessible and user-friendly.

The application provides an interface for exploring UHI-related parameters and generating machine learning-based predictions.

### Key capabilities

- Interactive dashboard for exploring project results.
- Visual representation of environmental and geospatial parameters.
- Land Surface Temperature prediction.
- Model-driven analysis of urban heat patterns.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Explainable AI | SHAP |
| Satellite Data Processing | Google Earth Engine |
| Geospatial Analysis | Geospatial and remote sensing datasets |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Web Application | Streamlit |

## 📁 Project Structure

```text
Urban-Heat-Island-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── exploratory_data_analysis.ipynb
│   └── model_training.ipynb
│
├── models/
│   ├── linear_regression.pkl
│   ├── random_forest.pkl
│   └── xgboost_model.pkl
│
└── assets/
    └── dashboard_screenshots/
```

*The structure above is a suggested layout. Adjust filenames and folders to match the actual GitHub repository.*

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd Urban-Heat-Island-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

*Replace `app.py` with the actual Streamlit entry-point filename if it differs.*

## 📈 Results and Impact

The proposed framework demonstrates how machine learning and multi-source geospatial data can be combined to analyze and predict urban heat patterns.

The project can support:

- Identification of areas experiencing elevated land surface temperatures.
- Understanding relationships between urbanization, vegetation, and temperature.
- Data-driven urban planning.
- Environmental monitoring and climate-resilient development.

## 🔮 Future Scope

Potential future enhancements include:

- Interactive GIS-based heat-risk mapping.
- Heatwave monitoring and alert systems.
- Explainable AI-based prediction insights.
- What-if simulations for urban greening and cool-roof interventions.
- Population-aware heat vulnerability assessment.
- AI-driven urban heat mitigation recommendations.
- Integration of real-time meteorological data.

## 👩‍💻 Author

**Kashvi Virmani**

Machine Learning | Geospatial Analysis | Remote Sensing | Python

## 📄 License

This project is intended for educational and research purposes. Add an appropriate open-source license to the repository before distributing the project for reuse.
