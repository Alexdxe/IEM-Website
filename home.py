import streamlit as st
from PIL import Image


#Background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://moondroplab.com/en/drawing?4c8143ce_page=1");
        background-attachment: fixed;
        background-size: cover
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Title: 
st.markdown("<h1 style='text-align: center;'>🏡Home Page</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Alexander Cai's IEM Page</h5>", unsafe_allow_html=True)

#Profile Photo:
photo = Image.open("images/mest.jpg")

#Centering: 
left, center, right = st.columns([1, 5, 1])
with center:
    st.image(photo, width=500)

#Description:
st.subheader("Description")
st.write("When Dankpods said in his The DankPods Headphone Starter Guide video that IEMs were “bang for the buck”, I knew I needed to try a set for myself. " \
"Ever since putting on my first pair of KZs, I have fallen deeper and deeper into the IEM rabbit hole, until today, I have tried over 50+ sets of IEMs. From 5-1300 dollars, " \
"I have been able to try some of the worst and best IEMs. This page is dedicated to giving my opinion on IEMs, and why I like what I like, and other general information on the hobby.")
st.write("")

#Purpose:
st.subheader("Purpose")
st.write("After years of being an audiophile, I’ve always wanted an outlet to express my interest and love for audio. I’ve spent hours listening to various IEMs, " \
"expanding my knowledge of audio terms, sound signatures, and investing over $ 100 in eartips alone. This hobby has consumed a significant amount of both my time and money, " \
"making it a shame not to share my experiences. By creating this website, I hope to not only express my passion for audio but also learn how to code a website on Streamlit, a platform " \
"widely adopted by Data Scientists for web development.")
st.write("")
st.write("")

#Music Taste:
st.subheader("Music Taste")
st.write("My music taste mostly consist of Jpop, Kpop, Cpop, Rock, and Indie. I’ve gravitated towards Asian genres because of the media I’ve consumed growing up (Anime, Chinese cartoons, K-pop music videos). There’s also a level of comfort knowing that you can somewhat relate to the artist who is singing. ")
st.page_link("https://open.spotify.com/user/alexdxe64?si=d59e739999fe4512", label="🎶Click here to view my Spotify Profile")

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












# from Pages import daily_drivers, database, tierlist, what_is_an_iem 

# #Sidebar for navigation
# with st.sidebar:
#     data = option_menu("Main Menu",["Database", "Tierlist"],
#                        icons=['database','list-task'], menu_icon="cast", default_index=0,)

# #Router for pages:
# if data == "Database":
#     database.show()

# elif data == "Tierlist":
#     tierlist.show()