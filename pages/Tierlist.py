import pandas as pd
import streamlit as st

def load_file():
    return pd.read_csv("data/tierlist.csv")


st.markdown("<h1 style='text-align: center;'>📊 Tierlist</h1>", unsafe_allow_html=True)

st.markdown("## 🛑 Disclaimer:")
st.markdown("**This tierlist is highly subjective.** These are decisions based on my own ears, and should not be taken as fact.")
st.page_link("pages/Distributions.py", label="📁Click here to see some statistics regarding my tierlist!")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)

with st.container():
    st.markdown("## Legend:")
    st.markdown("⭐ **Score**: This is the average score determined by Bass to Other.")
    st.markdown("💸 **Price**: The cost of the IEM (USD)")
    st.markdown("📰 **Name**: IEM's brand and model name")
    st.markdown("🔊 **Signature**: The overall sound of the IEM.")
    st.markdown("💣 **Bass**: The quality/quantity of the bass. This includes bass guitars and bass drops")
    st.markdown("🎤 **Mids**: The natural recreation of the mids. This includes vocals and most instruments.")
    st.markdown("☁️ **Treble**: The amount and smoothness in the treble. This determines clarity and fatigue.")
    st.markdown("🔎 **Details**: How well the IEM resolves (sound stage, imaging, seperation, microdetails)")
    st.markdown("📦 **Other**: The accessories, build, and fit. Factors that affect user experience.")
    st.markdown("🟢 **Likes**: My favorite aspect of the IEM.")
    st.markdown("🔴 **Dislikes**: My least favorite aspect of the IEM.")
    st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)



load_file()
df = load_file()
st.dataframe(df, use_container_width=True, height=800, hide_index=True)


#Sidebar for navigation

##Hide old sidebar:
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

##New sidebar:
with st.sidebar:
    st.header("Navigation")

    st.page_link("home.py", label="Home")

    st.page_link("pages/Tierlist.py", label="Tier List")
    st.page_link("pages/Database.py", label="Database")
    st.page_link("pages/Reviews.py", label="Reviews")
    st.page_link("pages/Daily_Drivers.py", label="Daily Drivers")
