import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from pycaret.classification import load_model, predict_model

# --- 1. Page Configuration ---
st.set_page_config(page_title="Thyroid Intelligence Engine", layout="wide")

# --- 2. Load the AI Model Safely ---
@st.cache_resource
def get_model():
    return load_model('thyroid_model_pipeline')

model = get_model()

# --- 3. Professional CSS (Your High-Contrast Design) ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #000000; color: white; }
label { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; }
[data-testid="stMetricValue"] { color: #00d4ff !important; font-family: 'Courier New', monospace; }
[data-testid="stMetric"] { background-color: #111111; border: 1px solid #222; padding: 15px; border-radius: 15px; }
div.stButton > button:first-child {
    background-color: #007bff; color: white; font-weight: bold; border-radius: 12px;
    height: 3.5em; width: 100%; border: none; box-shadow: 0 0 20px rgba(0, 123, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)

# --- 4. Header ---
st.title("🩺 Thyroid Sickness Diagnostic Engine")
st.markdown(f"##### *Advanced AI Analysis | System Date: {datetime.now().strftime('%Y-%m-%d')}*")
st.divider()

# --- 5. Dashboard Metrics ---
m1, m2, m3 = st.columns(3)
with m1:
    diagnosis_placeholder = st.empty()
    diagnosis_placeholder.metric("Patient Health Status", "Awaiting Data")
with m2:
    conf_placeholder = st.empty()
    conf_placeholder.metric("Inference Logic", "CatBoost + ANN")
with m3:
    st.metric("System Status", "Online", delta="Ready")

st.divider()

# --- 6. Patient Data Inputs ---
st.subheader("📋 Clinical Input Parameters")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### :blue[Demographics]")
    age = st.number_input("Patient Age", 1, 120, 30)
    sex = st.selectbox("Biological Sex", ["F", "M"])
    on_thyroxine = st.toggle("On Thyroxine")
    
with c2:
    st.markdown("### :blue[Lab Results I]")
    # We use capitalized names here to match the training data
    tsh = st.number_input("TSH (µIU/mL)", value=1.5, format="%.4f")
    t3 = st.number_input("T3 (nmol/L)", value=2.0, format="%.4f")
    tt4 = st.number_input("TT4 (nmol/L)", value=100.0, format="%.4f")

with c3:
    st.markdown("### :blue[Lab Results II]")
    fti = st.number_input("FTI Score", value=110.0, format="%.4f")
    t4u = st.number_input("T4U Level", value=1.0, format="%.4f")
    referral = st.selectbox("Referral Source", ["OTHER", "SVI", "SVHC", "STMW", "SVHD"])

# --- 7. Prediction Logic ---
st.divider()
if st.button("EXECUTE DIAGNOSTIC PROTOCOL"):
    
    # 1. Prepare data with EXACT column names from your CSV
    # These must match the training dataframe columns exactly
    input_df = pd.DataFrame([[age, sex, 't' if on_thyroxine else 'f', tsh, t3, tt4, t4u, fti, referral]], 
                        columns=['age', 'sex', 'on_thyroxine', 'TSH', 'T3', 'TT4', 'T4U', 'FTI', 'referral_source'])
    
    # 2. Run Real AI Prediction
    prediction_df = predict_model(model, data=input_df)
    
    # 3. Extract Results
    label = prediction_df['prediction_label'][0]
    # Check if the label is 'sick', 1, or 'positive' depending on your CSV
    is_sick = str(label).lower() in ['1', 'sick', 'positive']
    score = prediction_df['prediction_score'][0] * 100

    # 4. Display Results (Using your logic)
    if is_sick:
        diagnosis_placeholder.metric("Patient Health Status", "POSITIVE", delta="Pathology Detected", delta_color="inverse")
        conf_placeholder.metric("AI Confidence", f"{score:.2f}%", delta="High Alert")
        st.error(f"### 🚨 Result: Positive for Thyroid Sickness")
        report_status = "POSITIVE (SICK)"
    else:
        diagnosis_placeholder.metric("Patient Health Status", "NEGATIVE", delta="Healthy")
        conf_placeholder.metric("AI Confidence", f"{score:.2f}%", delta="Reliable")
        st.success("### ✅ Diagnosis: NEGATIVE (Healthy)")
        report_status = "NEGATIVE (HEALTHY)"

    # --- 8. Downloadable Clinical Report ---
    report_text = f"THYROID DIAGNOSTIC REPORT\nStatus: {report_status}\nAI Confidence: {score:.2f}%"
    st.download_button("📥 DOWNLOAD CLINICAL REPORT", data=report_text, file_name="Report.txt")
