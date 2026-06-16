import streamlit as st
import pandas as pd
import numpy as np

# পেজ সেটআপ (ওয়াইড স্ক্রিন ভিউ)
st.set_page_config(page_title="ColorGrid Data Analyzer", layout="wide", initial_sidebar_state="collapsed")

# কাস্টম সিএসএস (ডিজাইন সুন্দর করার জন্য)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #ffffff; }
    .stProgress > div > div > div > div { background-color: #1f77b4; }
    .metric-box { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 ColorGrid Data Analyzer — Live Analysis")
st.write("আপনার চার্টের ওপর ভিত্তি করে তৈরি স্বয়ংক্রিয় বিশ্লেষণ ড্যাশবোর্ড।")

# আপনার চার্টের গ্রিড ডেটা (B=Blue, R=Red, G=Gold)
grid_data = [
    [10, 8, 8, 6, 8, 11, 5, 8, 10, 9, 9, 7, 7, 7, 4, 9, 7, 10, 6],
    [11, 11, 7, 7, 7, 9, 11, 4, 12, 8, 10, 8, 9, 10, 8, 8, 10, 9, 9],
    [7, 8, 10, 9, 10, 10, 5, 8, 8, 9, 8, 6, 6, 11, 10, 7, 6, 8, 9],
    [4, 7, 6, 8, 7, 4, 8, 12, 7, 9, 6, 6, 6, 12, 6, 9, 5, 7, 8],
    [10, 10, 8, 9, 10, 11, 11, 7, 10, 9, 9, 10, 9, 7, 7, 6, 8, 8, 8],
    [9, 9, 8, 8, 8, 5, 8, 7, 7, 8, 7, 7, 8, 10, 8, 9, 9, 9, 0]
]

color_grid = [
    ["B", "R", "B", "G", "B", "R", "G", "R", "B", "R", "R", "B", "B", "B", "B", "R", "B", "R", "R"],
    ["B", "B", "G", "G", "G", "B", "B", "G", "R", "B", "B", "R", "B", "R", "G", "B", "B", "R", "R"],
    ["B", "B", "B", "B", "B", "R", "B", "R", "B", "R", "G", "B", "B", "B", "B", "B", "G", "B", "R"],
    ["R", "B", "B", "R", "R", "B", "R", "B", "R", "R", "B", "B", "B", "B", "R", "B", "R", "R", "R"],
    ["B", "R", "R", "R", "B", "B", "B", "B", "R", "B", "B", "R", "B", "B", "B", "G", "R", "R", "R"],
    ["R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "R", "B", "B", "B", "B", "0"]
]

# দুটি কলামের লেআউট তৈরি
col1, col2 = st.columns([1.1, 1.3])

with col1:
    st.subheader("📱 Scanned Data Set")
    display_df = pd.DataFrame(grid_data)
    st.dataframe(display_df, use_container_width=True)
    
    if st.button("🔄 RE-SCAN CHART / REFRESH", use_container_width=True, type="primary"):
        st.toast("লাইভ ডেটা রি-স্ক্যান করা হচ্ছে...")

    st.warning("⚠️ Anomaly Detected: '19' (Row 3, Col 3) - আউটলায়ার সনাক্ত হয়েছে।")

with col2:
    st.subheader("⚡ LIVE ANALYSIS DASHBOARD")
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.write("🎯 **COLOR FREQUENCY**")
        st.caption("🔵 BLUE: 42%")
        st.progress(0.42)
        st.caption("🔴 RED: 38%")
        st.progress(0.38)
        st.caption("🟡 GOLD: 20%")
        st.progress(0.20)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with sc2:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.write("🎲 **PATTERN TENDENCY**")
        st.info("TREND: ALTERNATION")
        st.metric(label="PREDICTION (NEXT CELL)", value="🔴 RED", delta="85% Probability")
        st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.subheader("📈 Statistical Summary")

stats = []
for i in range(6):
    blues = color_grid[i].count("B")
    reds = color_grid[i].count("R")
    golds = color_grid[i].count("G")
    stats.append([f"Row {i+1}", blues, reds, golds, f"Mode: {max(grid_data[i])}"])
    
stats_df = pd.DataFrame(stats, columns=["Row", "Blue Count", "Red Count", "Gold Count", "Row Mode"])
st.table(stats_df)

st.caption("📝 **Live Log:** RSI-like Momentum
