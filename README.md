# 🩺 Thyroid Intelligence Engine (TIE)
### **Clinical Decision Support System | Real-Time Pathology Screening**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://thyroid-ai-diagnostic-app.streamlit.app/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
The **Thyroid Intelligence Engine** is a specialized clinical dashboard designed to assist healthcare professionals in evaluating thyroid function. By analyzing biochemical markers (TSH, T3, TT4, FTI) against standard physiological thresholds, the system provides immediate diagnostic indicators and generates structured clinical reports.



## 🚀 Key Technical Features
* **Clinical Inference Logic:** Implemented diagnostic triggers based on TSH (>6.0 µIU/mL) and FTI (<65.0) to identify potential pathologies with high precision.
* **High-Contrast Medical UI:** Engineered using **Streamlit** with custom **CSS Injection** for a professional dark-mode, high-readability clinical interface.
* **Automated Reporting:** Features a built-in report generator that compiles patient data into a downloadable `.txt` clinical summary.
* **Real-Time Contextual Alerts:** Dynamic UI elements provide warnings based on medication status (e.g., hormone replacement therapy notes).

## 🛠️ Tech Stack
* **Frontend & Deployment:** Streamlit Cloud
* **Data Processing:** Pandas, NumPy
* **Styling:** Custom CSS, Markdown-it
* **Version Control:** Git / GitHub

## 📊 Clinical Indicators Tracked
The engine monitors these critical biomarkers to determine patient health status:

| Marker | Full Name | Standard Range |
| :--- | :--- | :--- |
| **TSH** | Thyroid Stimulating Hormone | 0.45 - 4.5 µIU/mL |
| **T3** | Triiodothyronine | 0.8 - 2.0 nmol/L |
| **FTI** | Free Thyroxine Index | 65 - 150 |
| **T4U** | T4 Uptake | 0.7 - 1.3 |

## 📥 Local Installation
If you wish to run this engine locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/thyroid-ai-diagnostic.git](https://github.com/YOUR_USERNAME/thyroid-ai-diagnostic.git)

2. **Navigate to the directory:**
   ```bash
   cd thyroid-ai-diagnostic

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt

4. **Launch the dashboard:**
   ```bash
   streamlit run app.py


## 📺 App Demo
<p align="center">
  <video src="https://github.com/user-attachments/assets/886aad09-48d2-4a52-8864-dfba056d2d87" width="100%" controls autoplay muted loop>
    Your browser does not support the video tag.
  </video>
</p>


## 📜 Disclaimer
This tool is a proof-of-concept for clinical decision support and is intended for educational and research purposes. All diagnostic outcomes should be verified by a certified medical professional.



Developed by Mani Ratan 
Project Link: https://thyroid-ai-diagnostic-app.streamlit.app/   

