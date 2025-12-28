import streamlit as st
from PIL import Image

#Write a small description of each IEM you used for a long period of time

st.markdown("<h1 style='text-align: center;'>♻️Daily Drivers</h1>", unsafe_allow_html=True)



with st.container():
    st.markdown("## Description")
    st.markdown("These are IEMs that I still actively use on a daily basis. While they might not all be the best IEMs I own, they each have a unique oddity that keeps me gravtitating back to each set.")
    st.divider()

st.write("")


st.subheader("Tanchjim Origin")
st.image("images/origin.jpg")
st.write("Despite this signature has been done to death with IEMs like the Moondrop Aria 2 and Kato, the Origin refines this mild V-Shape signature to perfection. It possess one of the best timbres I've heard from a single dynamic driver IEM, with a natural midrange and a silky smooth treble. It's truly an IEM that I can find very little fault with, and one I have used for weeks without getting bored of.")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **🟢 Pros**")
    st.markdown("""
    1. Natural timbre  
    2. Smooth treble  
    """)

with col2:
    st.markdown("#### **🔴 Cons**")
    st.markdown("""
    1. Can be shouty 
    2. Fit  
    """)
st.divider()

st.subheader("Softears Volume S")
st.image("images/volumes.jpg")
st.write("While skeptical at first, I eventually fell in love with the Softears Volume S. IT combines a warm, lush midrange with a bouncy bass to create a thick yet fun sound signature. Not to mention that it's vocal performance is amazing, with a forward presentation that makes vocals pop. It's a set I often grab whenever I want something fun yet relaxing to listen to.")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **🟢 Pros**")
    st.markdown("""
    1. Warm, lush midrange  
    2. Bass impact 
    """)

with col2:
    st.markdown("#### **🔴 Cons**")
    st.markdown("""
    1. Cramped midrange
    2. Treble can be too tamed
    """)
st.divider()

st.subheader("Moondrop Dusk")
st.image("images/dusk.jpg")
st.write("Probably the most hyped IEM of 2024, the Moondrop Dusk is the best price to performance IEMs you can buy. Despite being $400, it outperforms other IEMs because of it's multitude of tunings. Not only has it been lauded for it's natural DSP-default tuning, but all of it's other tunings (analog, bassy, V-Shape, Harman, etc.) are also fantastic. Personally, the DSP tuning may be the best IEM I have in my collection overall, blending a natural midrange, tight bass, and detailed treble into one neutral yet engaging sound signature.")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **🟢 Pros**")
    st.markdown("""
    1. Versatile
    2. Natural midrange
    """)

with col2:
    st.markdown("#### **🔴 Cons**")
    st.markdown("""
    1. Too much treble sometimes
    2. DSP Cable
    """)
st.divider()


st.subheader("Thieaudio Oracle")
st.image("images/oracle.jpg")
st.write("When I first jumped down the audiophile rabbit hole, the Thieaudio Oracle was one of the IEMs I wanted the most. Being hailed for having one of the most natural and realistic vocal presentations, it was exactly what I wanted in an IEM. After finally getting my hands on one, I was blown away. Not only was the midrange absolutely stunning, but both bass and treble were incredibly well executed. This perfect balance of all three ranges makes this IEM my favorite in my collection, and the one I reach for the most.")
st.write("")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **🟢 Pros**")
    st.markdown("""
    1. Beautfiul midrange  
    2. Good treble and bass energy
    """)

with col2:
    st.markdown("#### **🔴 Cons**")
    st.markdown("""
    1. Lacks overall excitement
    2. Needs more detail
    """)
st.divider()


st.subheader("Unique Melody Mest (Japan)")
st.image("images/mest.jpg")
st.write("Proclaimed as one of the most detailed IEMs in the world, the Unique Melody Mest almost feels like you are listening to music live. It's wide soundstage and airy presentation makes for an immersive listening experience While the tuning leans a little bright (a lot of treble), it is a joy to grab from time to time when I want to analytically listen to music.")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **🟢 Pros**")
    st.markdown("""
    1. Resolving  
    2. Fun sound signature
    """)

with col2:
    st.markdown("#### **🔴 Cons**")
    st.markdown("""
    1. Too much treble
    2. Unnatural timbre
    """)
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
