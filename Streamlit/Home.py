import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Urban Heat Island Prediction System",
    page_icon="thermometer.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Title
st.markdown("""
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:25px;">

    <img src="https://cdn-icons-png.flaticon.com/512/2784/2784487.png"
    width="85">

    <div>
        <div style="
            font-size:50px;
            font-weight:700;
            color:white;
            line-height:1.1;">
            Urban Heat Island
        </div>
        <div style="
            font-size:30px;
            color:#C8D0E0;">
            Prediction System
        </div>
    </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### AI-powered Land Surface Temperature Prediction

This dashboard predicts **Land Surface Temperature (LST)** using an optimized **XGBoost Regressor**
trained on satellite-derived environmental variables.

---
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Model", "XGBoost")
col2.metric("Test R²", "0.856")
col3.metric("RMSE", "1.27°C")
col4.metric("Samples", "9989")

st.markdown("---")

c1, c2 = st.columns([2,1])
with c1:
    st.subheader("Project Overview")
    st.write("""
The Urban Heat Island Prediction System estimates Land Surface Temperature
across Delhi using satellite-derived environmental variables.

The model was trained using:

- NDVI
- NDBI
- MNDWI
- Elevation
- Population
- Distance to Water
- Air Temperature
- Humidity
- Wind Speed
- Slope
- Land Use/Land Cover
""")

with c2:
    st.subheader("Dataset")
    st.info("""
Study Area : Delhi

Time Period : April–June 2024

Model : XGBoost

Features : 19

Target : Land Surface Temperature
""")
    
st.markdown("---")

st.subheader("Model Performance")

st.success("""
✔ Test R² = 0.856

✔ RMSE = 1.27°C

✔ Optimized using Hyperparameter Tuning
""")

st.subheader("Top Influential Variables")
st.image("Streamlit/image.png", width=500)
    
st.markdown("---")

st.caption(
    "Developed using Streamlit • XGBoost • SHAP • Google Earth Engine • Landsat 8"
)

with st.sidebar:
    st.markdown("""

    <div style="
    background:#15233B;
    padding:22px;
    border-radius:18px;
    border:1px solid #30476A;
    ">

    <div style="display:flex;align-items:center;gap:12px;">

    <div>

    <div style="
    font-size:20px;
    font-weight:700;
    color:white;">
    🌡️ Urban Heat Island
    </div>

    <div style="
    margin-top:10px;
    font-size:15px;
    line-height:1.6;
    color:#C8D0E0;">

    Urban areas become significantly warmer than
    their rural surroundings because concrete,
    asphalt and buildings absorb and retain heat,
    while vegetation and water bodies are limited.

    </div>

    </div>

    </div>

    </div>

    """, unsafe_allow_html=True)