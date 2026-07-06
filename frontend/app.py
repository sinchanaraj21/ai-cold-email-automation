import streamlit as st
from db import (
    get_total_emails,
    get_total_companies,
    get_total_recruiters,
    get_success_rate,
    get_campaign_history
)

st.set_page_config(
    page_title="ColdMail Automation",
    page_icon="📧",
    layout="wide"
)

st.title("📧 ColdMail Automation Dashboard")

st.success("Dashboard is running successfully!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📧 Emails Sent", get_total_emails())

with col2:
    st.metric("🏢 Companies", get_total_companies())

with col3:
    st.metric("👤 Recruiters", get_total_recruiters())

with col4:
    st.metric("✅ Success Rate", f"{get_success_rate()}%")

st.divider()

st.subheader("📋 Campaign History")

history = get_campaign_history()

st.dataframe(
    history,
    use_container_width=True,
    hide_index=True
)