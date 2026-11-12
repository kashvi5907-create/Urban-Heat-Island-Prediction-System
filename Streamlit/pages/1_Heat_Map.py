import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import shap
import pickle

st.markdown("""
<style>

.dashboard-card{
    background-color:#1c2333;
    border-radius:18px;
    border:1px solid #2e3b55;
    box-shadow:0 0 12px rgba(0,0,0,.25);
    height:100px;
}

.card-title{
    font-size:26px;
    font-weight:700;
}
</style>
""",unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.title("🗺️ Delhi Urban Heat Map")

# Load Data 

@st.cache_data
def load_data():
    return pd.read_csv("Streamlit/final_dataset.csv")

df = load_data()

with open("Streamlit/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Sidebar 

temp_range = st.sidebar.slider(
    "Temperature Range (°C)",
    float(df["LST"].min()),
    float(df["LST"].max()),
    (float(df["LST"].min()), float(df["LST"].max()))
)

min_temp, max_temp = temp_range

filtered_df = df[
    (df["LST"] >= min_temp) &
    (df["LST"] <= max_temp)
].copy()

st.sidebar.success(f"Showing {len(filtered_df)} locations")

def get_color(lst):
    if lst < 43:
        return [0, 128, 255]          # Blue
    elif lst < 45:
        return [0, 200, 0]            # Green
    elif lst < 47:
        return [255, 255, 0]          # Yellow
    elif lst < 49:
        return [255, 165, 0]          # Orange
    else:
        return [255, 0, 0]            # Red
    
filtered_df["color"] = filtered_df["LST"].apply(get_color)

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.metric(
        "Average LST",
        f"{filtered_df['LST'].mean():.2f} °C"
    )
with col2:
    st.metric(
        "Maximum LST",
        f"{filtered_df['LST'].max():.2f} °C"
    )
with col3:
    st.metric(
        "Minimum LST",
        f"{filtered_df['LST'].min():.2f} °C"
    )
with col4:
    st.metric(
        "Locations",
        len(filtered_df)
    )

layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position='[Longitude, Latitude]',
    get_fill_color='color',
    get_radius=60,
    pickable=True,
    auto_highlight=True,
)

view_state = pdk.ViewState(
    latitude=28.61,
    longitude=77.23,
    zoom=10,
    pitch=0
)

st.pydeck_chart(
    pdk.Deck(
        map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={
            "html": """
<b>LST:</b> {LST} °C<br/>
<b>NDVI:</b> {NDVI}<br/>
<b>NDBI:</b> {NDBI}<br/>
<b>MNDWI:</b> {MNDWI}
"""
        }
    )
)

bins=["<35","35-40","40-45","45-50",">50"]

counts=[
(df.LST<35).sum(),
((df.LST>=35)&(df.LST<40)).sum(),
((df.LST>=40)&(df.LST<45)).sum(),
((df.LST>=45)&(df.LST<50)).sum(),
(df.LST>=50).sum()
]

pie=px.pie(
    names=bins,
    values=counts,
    hole=0.55,
    color_discrete_sequence=[ "#4FC3F7", "#4CAF50", "#FFD54F", "#FF9800", "#E53935"]
)

with st.container(border=True):
    st.subheader("LST Distribution")
    st.plotly_chart(pie, use_container_width=True)

importance = pd.DataFrame({
    "Feature": model.feature_names_in_,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
).head(6)

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="Turbo"
)

fig.update_layout(
    height=320,
    showlegend=False,
    margin=dict(l=10,r=10,t=20,b=10),
    yaxis=dict(categoryorder="total ascending")
)

with st.container(border=True):
    st.subheader("Feature Importance")
    st.plotly_chart(fig, use_container_width=True)