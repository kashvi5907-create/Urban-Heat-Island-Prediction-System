import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
st.set_page_config(
    page_title="Predict LST",
    page_icon="🌡️",
    layout="wide"
)

# LOAD MODEL
with open("Streamlit/best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("Streamlit/shap_explainer.pkl", "rb") as f:
    explainer = pickle.load(f)

# CUSTOM CSS
st.markdown("""
<style>
.main{
    background-color:#0E1117;
}
.block-container{
    padding-top:2rem;
}
h1,h2,h3,h4{
    color:white;
}
.metric-card{
    background:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #30363d;
}
div[data-testid="stMetric"]{
    background-color:#161B22;
    padding:18px;
    border-radius:12px;
    border:1px solid #30363d;
}
div[data-testid="stMetric"]:hover{
    border:1px solid #58A6FF;
}
.stButton>button{
    width:100%;
    height:60px;
    font-size:22px;
    font-weight:bold;
    border-radius:12px;
    background:#238636;
    color:white;
}
.stButton>button:hover{
    background:#2ea043;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.title("🌡️ Urban Heat Island Prediction System")
st.markdown("""
Predict **Land Surface Temperature (LST)** using an optimized **XGBoost Regression Model**
trained on satellite-derived environmental variables.
""")
st.divider()

# INPUT SECTION
st.header("📍 Location")
col1,col2 = st.columns(2)
with col1:
    latitude = st.number_input(
        "Latitude",
        value=28.61,
        format="%.6f"
    )
with col2:
    longitude = st.number_input(
        "Longitude",
        value=77.23,
        format="%.6f"
    )
st.divider()

# VEGETATION
st.header("🌿 Vegetation & Water Indices")
col1,col2,col3 = st.columns(3)
with col1:
    ndvi = st.slider(
        "NDVI",
        -0.20,
        1.00,
        0.10
    )
with col2:
    ndbi = st.slider(
        "NDBI",
        -0.20,
        0.50,
        0.05
    )
with col3:
    mndwi = st.slider(
        "MNDWI",
        -1.00,
        1.00,
        -0.10
    )
st.divider()

# WEATHER
st.header("🌦 Weather Conditions")
col1,col2 = st.columns(2)
with col1:
    airtemp = st.slider(
        "Air Temperature (°C)",
        20.0,
        45.0,
        32.5
    )
    humidity = st.slider(
        "Humidity (%)",
        0.0,
        100.0,
        30.0
    )
with col2:
    wind = st.slider(
        "Wind Speed (m/s)",
        0.0,
        10.0,
        2.0
    )
st.divider()

# TERRAIN
st.header("🏔 Terrain Characteristics")
col1,col2,col3 = st.columns(3)
with col1:
    elevation = st.number_input(
        "Elevation (m)",
        value=220
    )
with col2:
    slope = st.number_input(
        "Slope (in degree/⁰)",
        value=1.5
    )
with col3:
    distance = st.number_input(
        "Distance To Water (m)",
        value=1500
    )
st.divider()

# HUMAN FACTORS
st.header("🏙 Urban Characteristics")
population = st.number_input(
    "Population Density (people/km²)",
    value=5000
)
st.divider()
# ¹²³⁴⁵⁶⁷⁸⁹⁰
# ₀₁₂₃₄₅₆₇₈₉

# LULC
st.header("🛰 Land Use / Land Cover")
lulc = st.selectbox(
    "Select Land Cover",
    [  "Built Area",
        "Crops",
        "Flooded Vegetation",
        "Grass",
        "Shrub",
        "Trees",
        "Water"
    ]
)

# One Hot Encoding
built = 0
crops = 0
flooded = 0
grass = 0
shrub = 0
trees = 0
water = 0

if lulc == "Built Area":
    built = 1
elif lulc == "Crops":
    crops = 1
elif lulc == "Flooded Vegetation":
    flooded = 1
elif lulc == "Grass":
    grass = 1
elif lulc == "Shrub":
    shrub = 1
elif lulc == "Trees":
    trees = 1
elif lulc == "Water":
    water = 1
st.divider()

# PREDICT BUTTON
predict_button = st.button(
    "🚀 Predict Land Surface Temperature"
)

# MAKE PREDICTION
if predict_button:
    sample = pd.DataFrame({
        "Latitude":[latitude],
        "Longitude":[longitude],
        "AirTemp":[airtemp],
        "DistanceToWater":[distance],
        "Elevation":[elevation],
        "Humidity":[humidity],
        "MNDWI":[mndwi],
        "NDBI":[ndbi],
        "NDVI":[ndvi],
        "Population":[population],
        "Slope":[slope],
        "WindSpeed":[wind],
        "LULC_Name_Built Area":[built],
        "LULC_Name_Crops":[crops],
        "LULC_Name_Flooded Vegetation":[flooded],
        "LULC_Name_Grass":[grass],
        "LULC_Name_Shrub":[shrub],
        "LULC_Name_Trees":[trees],
        "LULC_Name_Water":[water]
    })
    prediction = model.predict(sample)[0]
    shap_values = explainer(sample)
    st.header("📈 Prediction Results")
    st.metric(
        label="🌡 Predicted LST",
        value=f"{prediction:.2f} °C"
    )

    st.session_state["prediction"] = prediction
    st.session_state["sample"] = sample.copy()
    st.session_state["latitude"] = latitude
    st.session_state["longitude"] = longitude
    st.session_state["ndvi"] = ndvi
    st.session_state["ndbi"] = ndbi
    st.session_state["mndwi"] = mndwi
    st.session_state["elevation"] = elevation
    st.session_state["distance"] = distance
    st.session_state["population"] = population
    st.session_state["slope"] = slope
    st.session_state["humidity"] = humidity
    st.session_state["wind"] = wind
    st.session_state["airtemp"] = airtemp
    st.session_state["built"] = built
    st.session_state["crops"] = crops
    st.session_state["flooded"] = flooded
    st.session_state["grass"] = grass
    st.session_state["shrub"] = shrub
    st.session_state["trees"] = trees
    st.session_state["water"] = water

    # HEAT RISK LEVEL
    if prediction < 40:
        risk = "🟢 LOW"
        st.success("""
### 🟢 Low Heat Risk

The predicted land surface temperature is within a relatively comfortable range.
""")

    elif prediction < 45:
        risk = "🟡 MODERATE"
        st.warning("""
### 🟡 Moderate Heat Risk

Some localized warming is present.
""")
    elif prediction < 50:
        risk = "🟠 HIGH"
        st.error("""
### 🟠 High Heat Risk

Urban Heat Island effects are significant.
Mitigation strategies are recommended.
""")

    else:
        risk = "🔴 EXTREME"
        st.error("""
### 🔴 Extreme Heat Risk

This location is highly vulnerable to Urban Heat Island effects.
Immediate cooling strategies are recommended.
""")

    # ANALYSE ENVIRONMENTAL CONDITIONS
    # BUILT-UP AREA
    causes = []
    recommendations=[]

    if ndbi >= 0.15:
        causes.append("🏢 Very High Built-up Density")

        recommendations.append({
            "title":"Reduce Impervious Surfaces",
            "description":"Increase permeable pavements, cool roofs and reflective materials to reduce heat absorption.",
            "priority":"High"
        })

    elif ndbi >= 0.05:
        causes.append("🏙 Moderate Built-up Density")

        recommendations.append({
            "title":"Promote Cool Infrastructure",
            "description":"Use reflective pavements and encourage rooftop gardens.",
            "priority":"Medium"
        })

    # VEGETATION
    if ndvi < 0.15:
        causes.append("🌳 Very Low Vegetation Cover")

        recommendations.append({
            "title":"Increase Green Cover",
            "description":"Plant native trees, create green corridors and develop urban parks.",
            "priority":"High"
        })

    elif ndvi < 0.30:
        causes.append("🌿 Moderate Vegetation Cover")

        recommendations.append({
            "title":"Improve Green Spaces",
            "description":"Increase roadside plantation and maintain existing vegetation.",
            "priority":"Medium"
        })

    # WATER
    if mndwi < -0.20:
        causes.append("💧 Severe Lack of Water Bodies")

        recommendations.append({
            "title":"Increase Water Availability",
            "description":"Develop urban lakes, ponds and rainwater harvesting systems.",
            "priority":"High"
        })

    elif mndwi < 0:
        causes.append("💦 Limited Water Availability")

        recommendations.append({
            "title":"Preserve Existing Water Bodies",
            "description":"Improve nearby ponds and introduce fountains where feasible.",
            "priority":"Medium"
        })

    # POPULATION
    if population > 6000:
        causes.append("👥 Very High Population Density")

        recommendations.append({
            "title":"Reduce Urban Congestion",
            "description":"Increase public green spaces and improve ventilation corridors.",
            "priority":"Medium"
        })

    elif population > 3500:
        causes.append("🏘 Dense Urban Population")

        recommendations.append({
            "title":"Improve Urban Planning",
            "description":"Encourage vertical greening and additional public parks.",
            "priority":"Low"
        })

    # AIR TEMPERATURE
    if airtemp > 38:
        causes.append("🌞 High Air Temperature")

        recommendations.append({
            "title":"Heatwave Preparedness",
            "description":"Increase shaded areas and cooling shelters during extreme heat.",
            "priority":"High"
        })

    # LAND COVER
    if built == 1:
        causes.append("🏗 Built Area Dominates Land Cover")

        recommendations.append({
            "title":"Increase Green Roof Coverage",
            "description":"Encourage rooftop vegetation and wall gardens for commercial and residential buildings.",
            "priority":"Medium"
        })

    # DISPLAY IDENTIFIED CAUSES
    if len(causes) == 0:
        st.success("✅ No significant environmental stress factors detected.")
    else:
        for cause in causes:
            st.write("•", cause)
    st.divider()

    # MITIGATION STRATEGIES
    if(len(causes)!=0):
        st.header("🌱 Recommended Mitigation Strategies")
        priority_color = {
            "High":"🔴",
            "Medium":"🟠",
            "Low":"🟢"
        }
        for rec in recommendations:
            with st.container(border=True):
                st.subheader(
                    f"{priority_color[rec['priority']]} {rec['title']}"
                )
                st.write(rec["description"])
                st.caption(
                    f"Priority : {rec['priority']}"
                )
        st.divider()

    # INPUT SUMMARY
    st.header("📋 Input Summary")
    summary = pd.DataFrame({
        "Feature":[
            "Latitude",
            "Longitude",
            "Air Temperature",
            "Humidity",
            "Wind Speed",
            "NDVI",
            "NDBI",
            "MNDWI",
            "Elevation",
            "Slope",
            "Distance To Water",
            "Population",
            "Land Cover"
        ],

        "Value":[
            latitude,
            longitude,
            airtemp,
            humidity,
            wind,
            ndvi,
            ndbi,
            mndwi,
            elevation,
            slope,
            distance,
            population,
            lulc
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
        height=493
    )
    st.divider()

# ABOUT THIS PAGE
with st.expander("ℹ️ About this Prediction Tool"):

    st.write("""
This AI-powered tool predicts **Land Surface Temperature (LST)** using an
optimized **XGBoost Regression Model** trained on satellite-derived
environmental features.

The prediction is based on multiple factors including:

- Latitude & Longitude
- Air Temperature
- NDVI
- NDBI
- MNDWI
- Humidity
- Wind Speed
- Elevation
- Distance to Water
- Population Density
- Land Use / Land Cover

The generated prediction helps identify potential Urban Heat Island
hotspots and supports sustainable urban planning.
""")

# DISCLAIMER
with st.expander("⚠️ Disclaimer"):

    st.write("""
The predictions generated by this dashboard are based on the trained
machine learning model and should be considered **decision-support
information** rather than exact measurements.

Actual land surface temperature may vary depending on
meteorological conditions, seasonal changes and satellite acquisition time.
""")