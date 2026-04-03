import streamlit as st
from fraud_logic import rule_based_detection
from ml_model import get_model_prediction
from decision_engine import final_decision
from weather_service import get_weather

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🚨 Fake Driver Detection System")
st.write("Detect GPS spoofing using Rule-Based + ML Model")

# -------------------------------
# Input Section
# -------------------------------
st.header("Enter Driver Details")

user_id = st.text_input("User ID")

latitude = st.number_input("Latitude", value=28.61)
longitude = st.number_input("Longitude", value=77.23)

speed = st.number_input("Speed (km/h)", min_value=0.0, value=0.0)

distance = st.number_input("Distance moved in last 10 min (km)", min_value=0.0, value=0.0)

weather = st.selectbox("Weather Condition", ["clear", "rain", "storm"])

# -------------------------------
# Button Action
# -------------------------------
if st.button("Check Fraud"):

    # 🌧️ Get REAL weather
    real_weather = get_weather(latitude, longitude)

    # Rule-based detection (UPDATED)
    rule_score, reasons = rule_based_detection(speed, distance, weather, real_weather)

    # ML prediction
    ml_pred = get_model_prediction(speed, distance)

    if ml_pred == -1:
        reasons.append("Anomaly detected by ML model")

    # Final decision
    status, risk = final_decision(rule_score, ml_pred)

    # -------------------------------
    # Output
    # -------------------------------
    st.subheader("📊 Result")

    st.write(f"**User ID:** {user_id}")

    # Show both weather values
    st.write(f"**User Weather:** {weather}")
    st.write(f"**Actual Weather (API):** {real_weather}")

    if "Fraud" in status:
        st.error(f"Status: {status}")
    elif "Suspicious" in status:
        st.warning(f"Status: {status}")
    else:
        st.success(f"Status: {status}")

    st.write(f"**Risk Score:** {risk}")

    st.write("### 🔍 Reasons:")
    for r in reasons:
        st.write(f"- {r}")