import streamlit as st
import pandas as pd

#Database of all thwe IEMs you tried
def load_file():
    return pd.read_csv("data/database.csv")

st.markdown("<h1 style='text-align: center;'>💾 Database</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("## Legend:")
    st.markdown("💸 Price: The cost of the IEM (USD)")
    st.markdown("🖨️ Brand: IEM's brand")
    st.markdown("📰 Name: IEM's Name")
    st.markdown("🔊 Signature: The overall sound of the IEM.")
    st.markdown("🎧 Drivers: The Configuration of the IEM.")
    st.markdown("🔢 Release Year: When the IEM was released.")
    st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)

df = load_file()
st.dataframe(df, use_container_width=True, height=800)



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
