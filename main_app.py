
import streamlit as st
from modules.shot_detection import detect_shot_type
from modules.ball_tracking import track_ball
from modules.player_stats import PlayerStats
from helpers.export import export_dashboard
import os

st.set_page_config(page_title="PadelVision Pro", layout="wide", page_icon="🎾")
st.title("🎾 PadelVision Pro")
st.caption("AI-powered padel game analysis. Upload a video to get started.")

video_file = st.file_uploader("Upload your padel match video", type=["mp4", "mov"])

if video_file:
    st.video(video_file)
    st.info("Analyzing... (mocked analysis)")

    stats = PlayerStats()
    for _ in range(150):  # Simulate 150 frames
        stats.update(detect_shot_type())

    shot_summary = stats.summary()
    ball_data = track_ball()

    st.subheader("📊 Player Statistics")
    for k, v in shot_summary.items():
        st.metric(label=k, value=v)

    st.subheader("🎯 Ball Tracking Data")
    st.json(ball_data)

    if st.button("📤 Export Dashboard Report"):
        pdf_path = export_dashboard(shot_summary)
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF Report", f, file_name="PadelVision_Report.pdf")
        os.remove(pdf_path)
else:
    st.warning("Please upload a video to begin analysis.")
