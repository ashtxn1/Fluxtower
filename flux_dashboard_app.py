
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from io import StringIO

st.set_page_config(page_title="PVAMU Flux Tower Dashboard", layout="wide")

st.markdown(
    "<h1 style='color:#582C83;'>Welcome to PVAMU’s Live Flux Tower Dashboard – Powered by AITC</h1>",
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload new CSV data", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
else:
    # Simulate default dataset
    timestamps = pd.date_range(end=datetime.datetime.now(), periods=60, freq='T')
    data = pd.DataFrame({
        "Timestamp": timestamps,
        "CO2_flux": np.random.normal(15, 3, 60),
        "Net_radiation": np.random.normal(400, 50, 60),
        "Soil_moisture": np.random.uniform(10, 40, 60),
        "Air_temperature": np.random.normal(25, 2, 60),
        "Wind_speed": np.random.uniform(0.5, 5, 60),
        "N2O_flux": np.random.normal(0.5, 0.1, 60),
        "Methane_flux": np.random.normal(1.2, 0.2, 60),
    })

st.download_button("Download Current Data", data.to_csv(index=False), file_name="flux_data.csv", mime="text/csv")

# Display graphs
st.line_chart(data.set_index("Timestamp")[["CO2_flux", "N2O_flux", "Methane_flux"]])
st.line_chart(data.set_index("Timestamp")[["Net_radiation", "Soil_moisture", "Air_temperature", "Wind_speed"]])
