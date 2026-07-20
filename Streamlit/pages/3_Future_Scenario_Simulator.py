import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

# PAGE CONFIG
st.set_page_config(
    page_title="Future Scenario Simulator",
    page_icon="🔮",
    layout="wide"
)

# LOAD MODEL
with open("Streamlit/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# CUSTOM CSS
st.markdown("""
<style>
.main{
    background:#0E1117;
}
.block-container{
    padding-top:2rem;
}
.big-title{
    font-size:40px;
    font-weight:bold;
    color:white;
}
.subtitle{
    font-size:18px;
    color:#BBBBBB;
}
.sim-card{
    background:#161B22;
    padding:20px;
    border-radius:15px;
    border:1px solid #30363d;
}
</style>
""", unsafe_allow_html=True)

# PAGE TITLE
st.markdown("""
<div class="big-title">

🔮 Future Scenario Simulator

</div>

<div class="subtitle">

Simulate environmental improvements and estimate
their impact on Land Surface Temperature.

</div>

""", unsafe_allow_html=True)

st.divider()

# CHECK SESSION
if "prediction" not in st.session_state:

    st.warning("""
Please visit **Predict LST** first.
Generate a prediction before using the
Future Scenario Simulator.
""")

    st.stop()

# LOAD VALUES
prediction = st.session_state["prediction"]
sample = st.session_state["sample"].copy()
ndvi = st.session_state["ndvi"]
ndbi = st.session_state["ndbi"]
mndwi = st.session_state["mndwi"]
latitude = st.session_state["latitude"]
longitude = st.session_state["longitude"]
airtemp = st.session_state["airtemp"]
humidity = st.session_state["humidity"]
wind = st.session_state["wind"]
population = st.session_state["population"]
distance = st.session_state["distance"]
elevation = st.session_state["elevation"]
slope = st.session_state["slope"]
built = st.session_state["built"]
crops = st.session_state["crops"]
flooded = st.session_state["flooded"]
grass = st.session_state["grass"]
shrub = st.session_state["shrub"]
trees = st.session_state["trees"]
water = st.session_state["water"]

# CURRENT CONDITION
st.header("🌍 Current Scenario")

col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Current Predicted LST",
        f"{prediction:.2f} °C"
    )
with col2:
    if prediction < 35:
        st.success("🟢 Low Heat Risk")
    elif prediction < 40:
        st.warning("🟡 Moderate Heat Risk")
    elif prediction < 45:
        st.warning("🟠 High Heat Risk")
    else:
        st.error("🔴 Very High Heat Risk")
st.divider()

# SIMULATION CONTROLS
st.header("⚙️ Modify Future Environment")
st.write(
"""
Adjust the environmental parameters below to
estimate how future interventions may influence
Land Surface Temperature.
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    future_ndvi = st.slider(
        "🌳 Increase Vegetation (NDVI)",
        min_value=float(ndvi),
        max_value=1.0,
        value=float(ndvi),
        step=0.01
    )
with col2:
    future_ndbi = st.slider(
        "🏢 Reduce Built-up (NDBI)",
        min_value=-0.20,
        max_value=float(ndbi),
        value=float(ndbi),
        step=0.01
    )
with col3:
    future_mndwi = st.slider(
        "💧 Improve Water Index (MNDWI)",
        min_value=float(mndwi),
        max_value=1.0,
        value=float(mndwi),
        step=0.01
    )
st.divider()
simulate = st.button(
    "🚀 Simulate Future Scenario"
)

if simulate:
    future_sample = sample.copy()
    future_sample["NDVI"] = future_ndvi
    future_sample["NDBI"] = future_ndbi
    future_sample["MNDWI"] = future_mndwi
    future_prediction = model.predict(future_sample)[0]
    cooling = prediction - future_prediction
    st.divider()
    st.header("📊 Simulation Results")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="🌡️ Current LST",
            value=f"{prediction:.2f} °C"
        )
    with col2:
        st.metric(
            label="🌍 Future LST",
            value=f"{future_prediction:.2f} °C",
            delta=f"{cooling:.2f} °C"
        )
    with col3:
        st.metric(
            label="❄️ Estimated Cooling",
            value=f"{cooling:.2f} °C"
        )
    st.divider()

    st.subheader("🌿 Environmental Changes")
    summary = pd.DataFrame({
        "Parameter":["NDVI","NDBI","MNDWI"],
        "Current":[ndvi,ndbi,mndwi],
        "Future":[future_ndvi,future_ndbi,future_mndwi]
    })

    st.dataframe(
        summary,
        hide_index=True,
        use_container_width=True
    )
    st.divider()

    #TEMPERATURE COMPARISON CHART
    st.subheader("📈 Temperature Comparison")
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="Current",
            x=["Current"],
            y=[prediction],
            text=[f"{prediction:.2f}°C"],
            textposition="outside"
        )
    )

    fig.add_trace(
        go.Bar(
            name="Future",
            x=["Future"],
            y=[future_prediction],
            text=[f"{future_prediction:.2f}°C"],
            textposition="outside"
        )
    )

    fig.update_layout(
        height=450,
        barmode="group",
        yaxis_title="Land Surface Temperature (°C)",
        xaxis_title="Scenario",
        legend_title="",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.divider()

    st.header("🧠 AI Interpretation")
    if cooling >= 3:
        st.success("""
    ### 🌍 Excellent Improvement

    The proposed environmental changes are predicted to reduce
    Land Surface Temperature significantly.

    This indicates that increasing vegetation, reducing built-up
    surfaces and improving water availability together can greatly
    mitigate Urban Heat Island effects.
    """)
    elif cooling >= 1:
        st.info("""
    ### 🌱 Good Improvement

    The simulation predicts a noticeable reduction in
    Land Surface Temperature.

    These interventions would contribute to a cooler
    and more sustainable urban environment.
    """)
    elif cooling >= 0.1:
        st.warning("""
    ### 🌿 Moderate Improvement

    The selected interventions provide only limited cooling.

    Further improvements in vegetation or reduction in
    built-up density may produce better results.
    """)
    else:
        st.error("""
    ### ⚠ Minimal Improvement

    The selected changes are not sufficient to produce
    meaningful cooling.

    Consider increasing vegetation further and reducing
    built-up intensity.
    """)