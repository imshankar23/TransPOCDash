
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transition Success Dashboard", layout="wide")

st.title("📊 Transition Success Dashboard")

st.sidebar.header("Upload Your Trackers")
sow_file = st.sidebar.file_uploader("Upload SOW Tracker (Excel)", type=["xlsx"])
kt_file = st.sidebar.file_uploader("Upload KT Tracker (Excel)", type=["xlsx"])
hiring_file = st.sidebar.file_uploader("Upload Hiring Tracker (Excel)", type=["xlsx"])
access_file = st.sidebar.file_uploader("Upload Access Tracker (Excel)", type=["xlsx"])

def load_data(uploaded_file):
    if uploaded_file:
        return pd.read_excel(uploaded_file)
    return pd.DataFrame()

sow_df = load_data(sow_file)
kt_df = load_data(kt_file)
hiring_df = load_data(hiring_file)
access_df = load_data(access_file)

st.markdown("### 📄 SOW Tracker")
if not sow_df.empty:
    st.dataframe(sow_df, use_container_width=True)
else:
    st.info("Upload an SOW Tracker Excel file to view data.")

st.markdown("### 📘 KT Tracker")
if not kt_df.empty:
    st.dataframe(kt_df, use_container_width=True)
else:
    st.info("Upload a KT Tracker Excel file to view data.")

st.markdown("### 👥 Hiring Tracker")
if not hiring_df.empty:
    st.dataframe(hiring_df, use_container_width=True)
else:
    st.info("Upload a Hiring Tracker Excel file to view data.")

st.markdown("### 🔑 Access Provisioning Tracker")
if not access_df.empty:
    st.dataframe(access_df, use_container_width=True)
else:
    st.info("Upload an Access Tracker Excel file to view data.")

st.markdown("### 🚦 Status Summary (Optional RAG View)")
if not kt_df.empty and "Confidence Score (1-5)" in kt_df.columns:
    rag_summary = kt_df.copy()
    def classify_rag(score):
        if score >= 4:
            return "🟢 Green"
        elif score >= 3:
            return "🟡 Amber"
        else:
            return "🔴 Red"
    rag_summary["RAG Status"] = rag_summary["Confidence Score (1-5)"].apply(classify_rag)
    st.dataframe(rag_summary[["Module Name", "BAU Owner", "Confidence Score (1-5)", "RAG Status"]], use_container_width=True)
else:
    st.info("To see RAG view, KT Tracker must include 'Confidence Score (1-5)' column.")
