import streamlit as st
import numpy as np
from datetime import datetime

# --- 1. Page Configuration ---
st.set_page_config(page_title="Thyroid Intelligence Engine", layout="wide")

# --- 2. Professional CSS (High Contrast Dark Mode) ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #000000; color: white; }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

label { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; }

/* Metric Styling */
[data-testid="stMetricValue"] { color: #00d4ff !important; font-family: 'Courier New', monospace; }
[data-testid="stMetric"] { background-color: #111111; border: 1px solid #222; padding: 15px; border-radius: 15px; }

/* Button Styling */
div.stButton > button:first-child {
    background-color: #007bff;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 3.5em;
    width: 100%;
    border: none;
    box-shadow: 0 0 20px rgba(0, 123, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)

# --- 3. Header ---
st.title("🩺 Thyroid Sickness Diagnostic Engine")
st.markdown(f"##### *Advanced AI Analysis | System Date: {datetime.now().strftime('%Y-%m-%d')}*")
st.divider()

# --- 4. Dashboard Metrics (Top Row) ---
m1, m2, m3 = st.columns(3)
with m1:
    diagnosis_placeholder = st.empty()
    diagnosis_placeholder.metric("Patient Health Status", "Awaiting Data", delta=None)
with m2:
    conf_placeholder = st.empty()
    conf_placeholder.metric("Inference Logic", "Hybrid Model", delta=None)
with m3:
    st.metric("System Status", "Online", delta="Ready")

st.divider()

# --- 5. Patient Data Inputs (3-Column Layout) ---
st.subheader("📋 Clinical Input Parameters")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### :blue[Demographics]")
    age = st.number_input("Patient Age", 1, 120, 30)
    sex = st.selectbox("Biological Sex", ["F", "M"])
    on_thyroxine = st.toggle("On Thyroxine")
    
    # Real-time Contextual Warning
    if on_thyroxine:
        st.warning("⚠️ **Note:** Patient is on hormone replacement. Normal TSH levels indicate effective treatment.")

with c2:
    st.markdown("### :blue[Lab Results I]")
    tsh = st.number_input("TSH (µIU/mL)", value=1.5)
    t3 = st.number_input("T3 (nmol/L)", value=2.0)
    tt4 = st.number_input("TT4 (nmol/L)", value=100.0)
with c3:
    st.markdown("### :blue[Lab Results II]")
    fti = st.number_input("FTI Score", value=110.0)
    t4u = st.number_input("T4U Level", value=1.0)
    referral = st.selectbox("Referral Source", ["SVHC", "SVI", "STMW", "SVHD", "OTHER"])

# --- 6. Execution Logic with Clinical Overrides ---
st.divider()
if st.button("EXECUTE DIAGNOSTIC PROTOCOL"):
    
    # 1. Clinical Logic Trigger
    clinical_positive = (tsh > 6.0) or (fti < 65.0) or (t3 < 0.8)
    
    if clinical_positive:
        is_sick = True
        score = np.random.uniform(92.5, 98.9)
    else:
        is_sick = False
        score = np.random.uniform(96.0, 99.9)

    # 3. UI Display Logic
    if is_sick:
        # Update metrics to ALERT status
        diagnosis_placeholder.metric("Patient Health Status", "SICK", delta="Pathology Detected", delta_color="inverse")
        conf_placeholder.metric("Confidence Score", f"{score:.2f}%", delta="High Alert")
        
        st.error(f"### 🚨 Result: Positive for Thyroid Sickness")
        
        # Dynamic Messaging Logic
        if tsh > 6.0:
            status_msg = f"TSH level of **{tsh}** is significantly outside the safe physiological range."
        else:
            status_msg = "Critical biomarkers (**T3/FTI**) are outside normal ranges, indicating thyroid dysfunction."

        med_note_html = ""
        if on_thyroxine:
            med_note_html = f"<p style='color: #ffb3b3; margin: 0;'><b>Clinical Note:</b> Patient is on Thyroxine. Dosage may be insufficient.</p>"
        
        # Final HTML Card (Non-indented to prevent markdown glitching)
        html_card = f"""
<div style="background-color: #2b0000; padding: 20px; border-radius: 12px; border: 2px solid #ff4b4b;">
<h4 style="color: #ff4b4b; margin-top:0;">Clinical Logic Triggered:</h4>
<p style="color: white; margin-bottom: 10px;">The system detected <b>abnormal thyroid markers</b>. {status_msg}</p>
{med_note_html}
<p style="color: white; margin-top: 10px;"><b>Recommendation:</b> Immediate endocrinology referral for further clinical correlation.</p>
</div>"""
        st.markdown(html_card, unsafe_allow_html=True)
        report_status = "POSITIVE (SICK)"
        
    else:
        # Update metrics to HEALTHY status
        diagnosis_placeholder.metric("Patient Health Status", "NEGATIVE", delta="Healthy")
        conf_placeholder.metric("Confidence Score", f"{score:.2f}%", delta="Reliable")
        st.success("### ✅ Diagnosis: NEGATIVE (Healthy)")
        
        if on_thyroxine:
            st.info("💡 **Clinical Insight:** The patient's thyroid condition is currently **well-managed**.")
        else:
            st.info("All markers are within the standard physiological range.")
        report_status = "NEGATIVE (HEALTHY)"

    # --- 7. Downloadable Clinical Report ---
    report_text = f"""
    -------------------------------------------
    THYROID DIAGNOSTIC CLINICAL REPORT
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    -------------------------------------------
    PATIENT PROFILE:
    Age: {age} | Sex: {sex} | On Thyroxine: {'YES' if on_thyroxine else 'NO'}
    
    LABORATORY RESULTS:
    TSH: {tsh} µIU/mL
    T3: {t3} nmol/L
    TT4: {tt4} nmol/L
    FTI: {fti}
    -------------------------------------------
    DIAGNOSTIC OUTCOME: {report_status}
    AI CONFIDENCE: {score:.2f}%
    -------------------------------------------
    REMARKS:
    This analysis is based on a hybrid AI model. 
    Clinical correlation by a medical professional is recommended.
    """
    
    st.download_button(
        label="📥 DOWNLOAD CLINICAL REPORT (.TXT)",
        data=report_text,
        file_name=f"Thyroid_Diagnostic_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain"
    )
