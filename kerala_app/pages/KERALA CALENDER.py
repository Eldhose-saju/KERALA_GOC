import streamlit as st
import datetime

# Malayalam months and important festivals
kerala_calendar = {
    "Chingam": ["Onam - Aug/Sep"],
    "Kanni": ["Mahanavami - Sep/Oct", "Vijayadashami - Sep/Oct"],
    "Thulam": ["Deepavali - Oct/Nov"],
    "Vrischikam": ["Mandala Pooja Begins - Nov/Dec"],
    "Dhanu": ["Christmas - Dec 25"],
    "Makaram": ["Makaravilakku - Jan 14"],
    "Kumbham": ["Shivaratri - Feb/Mar"],
    "Meenam": ["Attukal Pongala - Feb/Mar", "Vishu - Apr 14"],
    "Medam": ["Thrissur Pooram - Apr/May"],
    "Edavam": ["Vaikasi Vishakam - May/Jun"],
    "Midhunam": ["Ramzan - Varies"],
    "Karkidakam": ["Karkidaka Vavu - Jul/Aug"]
}

# Get current Malayalam month
current_month_index = datetime.datetime.now().month - 1
malayalam_months = list(kerala_calendar.keys())
current_malayalam_month = malayalam_months[current_month_index % 12]

st.title("📅 Kerala Calendar 2025")

# Dropdown to select month
selected_month = st.selectbox("Select a Malayalam Month", malayalam_months, index=current_month_index % 12)

# Display festivals of selected month
st.subheader(f"Festivals in {selected_month}")
festivals = kerala_calendar.get(selected_month, [])
if festivals:
    for festival in festivals:
        st.write(f"- {festival}")
else:
    st.write("No major festivals this month.")
