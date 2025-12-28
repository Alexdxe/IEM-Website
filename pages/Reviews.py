import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("<h1 style='text-align: center;'>📰Reviews</h1>", unsafe_allow_html=True)
photo = Image.open("images/collection.jpg")

#Centering: 
left, center, right = st.columns([1, 5, 1])
with center:
    st.image(photo, width=500)

#Description
st.markdown("## Description:")
st.markdown("This is a hub for all of the IEM reviews I have written and recorded over the years. Each review contains the following: ")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)
st.write("")

#Criteria Breakdown
st.markdown("## Breakdown:")
st.markdown("**🚩Introduction**: A brief overview of the IEM.")
st.markdown("**📦Accessories/Intangables**: The accessories, build, and fit. Factors that affect user experience.")
st.markdown("**🔊Overall Sound**: The sound signature the IEM was going for.")
st.markdown("**💣Bass**: The quality/quantity of the bass. This includes bass guitars and bass drops")
st.markdown("**🎤Mids**: The natural recreation of the mids. This includes vocals and most instruments.")
st.markdown("**☁️Treble**: The amount and smoothness in the treble. This determines clarity and fatigue.")
st.markdown("**🔎Details**: How well the IEM resolves (sound stage, imaging, seperation, microdetails)")
st.markdown("**🆚Comparisons**: How the IEM compares to other IEMs in a similar price range or signature.")
st.markdown("**🏁Conclusion**: My final thoughts on the IEM and whether I recommend it or not.")

#Page Links:
st.markdown("## Reviews:")

###links for buttons:
col1, col2, col3 = st.columns(3)

# Add buttons inside the columns
with col1:
    st.page_link("pages/Truthears_Hexa.py", label="⭐Truthears Hexa")
    st.write("")
    st.page_link("pages/Tangzu_Wan'er.py", label="Tangzu Wan'er")
    st.write("")
    st.page_link("pages/Moondrop_Starfield.py", label="Moondrop Starfield")
    st.write("")


with col2:
    st.page_link("pages/Moondrop_Variations.py", label="⭐Moondrop Variations")
    st.write("")
    st.page_link("pages/Moondrop_Blessing_2_Dusk.py", label="Moondrop Blessing 2 Dusk")
    st.write("")
    st.page_link("pages/Letshuoer_S12.py", label="Letshuoer S12")
    
    
    

with col3:
    st.page_link("pages/Softears_Volume_&_Volume_S.py", label="⭐Softears Volume/S")
    st.write("")
    st.page_link("pages/Truthears_Zero_Red.py", label="Truthears Zero: Red")
    st.write("")
    st.page_link("pages/Thieaudio_Oracle.py", label="Thieaudio Oracle")
    st.write("")
    
    






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
