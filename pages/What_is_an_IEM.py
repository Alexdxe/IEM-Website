import streamlit as st 

#Overview of what an IEM is. 
st.markdown("<h1 style='text-align: center;'>🎧 What is an IEM?</h1>", unsafe_allow_html=True)
st.markdown("## Definition:")







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

