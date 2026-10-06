import streamlit as st

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 California House Price Predictor")

st.write("Welcome to the House Price Prediction System.")

st.divider()

st.header("📊 Property Details")

col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input("Median Income", value=3.5)
    house_age = st.number_input("House Age", value=25.0)
    ave_rooms = st.number_input("Average Rooms", value=5.0)
    ave_bedrms = st.number_input("Average Bedrooms", value=1.0)

with col2:
    population = st.number_input("Population", value=1000.0)
    ave_occup = st.number_input("Average Occupancy", value=3.0)
    latitude = st.number_input("Latitude", value=35.0)
    longitude = st.number_input("Longitude", value=-119.0)

st.divider()

if st.button("🔮 PREDICT HOUSE PRICE", type="primary"):
    st.success("✅ The frontend is working!")
    st.write("Median Income:", med_inc)
    st.write("House Age:", house_age)
    st.write("Average Rooms:", ave_rooms)
    st.write("Average Bedrooms:", ave_bedrms)
    st.write("Population:", population)
    st.write("Average Occupancy:", ave_occup)
    st.write("Latitude:", latitude)
    st.write("Longitude:", longitude)

st.sidebar.title("🏠 House Predictor")
st.sidebar.write("California Housing Price Prediction")
