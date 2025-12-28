import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Moondrop Blessing 2 Dusk </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 09/19/2023</h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the")
st.video("https://youtu.be/hxl1AMb_X84")

st.markdown("## 🚩Introduction:")
st.markdown("This week, we will be discussing the Moondrop Blessing 2 Dusk, an absolute behemoth at ~$300. This IEM has made waves in the community and has sat atop the hobby for the last few years for its incredible performance at its price range. However, with 3 years since its initial release, does the B2 Dusk still destroy everything in its price range? ")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("Starting off with the design of the IEM, it’s amazingly constructed, with the IEM’s face plate being stainless steel, and you could actually get an engraving on the IEM. The overall shell is also of high quality, but also rather large. For many, I think the size of the headphone will be a problem for many. While it is large, I don’t think it's a problem for me, but I think this is definitely something many should keep in mind before purchasing the Dusk. Two problems I have with the presentation of the IEM are the cable and the eartips. With a purchase at ~300 USD, you would expect the IEM to at least have a nice cable and good eartips. However, this set comes with the same cable and eartips that the Moondrop Starfield comes with, which is a $110 set. The eartips, while not terrible, are cheap and something you’d usually get for around 20 dollars, while the cable is fine, there are plenty of IEMs around or under this price point with much better cables. For example, the Letshouer S12’s cable is very nice, and leagues better than on the Blessing 2 Dusk. Moondrop really cheaped out with these parts, but they are more than forgiven with the sound of this set.")

st.markdown("## 🔊Overall Sound:")
st.markdown("The Blessing 2 Dusk can be described as A Neutral with a bass boost. It emphasizes the upper mid-range, sub-bass, and treble, making for a slightly engaging listen. Overall, the Blessing 2 Dusk is an all-rounder that does little wrong and a lot right.")

st.markdown("## 💣Bass:")
st.markdown("This may be the IEM’s weakest point. While not bad bass by any means, the quality of the bass can sometimes be a bit underwhelming.  The IEM seems to struggle to push out certain bass notes, with it often coming off as dry or as if the driver is reaching its absolute limit. This IEM has plenty of both mid and sub-bass, giving life to many genres like K-pop or J-pop. While listening to ‘Number One Bankai’ by Shiro Sagisu, both the sub-bass and mid-bass have a strong presence in the mix, with the quantity of bass making the track very lively and upbeat, sometimes even feeling like the bass is overpowering the vocals, but not in a way where it smears the vocals.")

st.markdown("## 🎤Mids:")
st.markdown("The mids, in my opinion, are probably where this IEM shines the brightest. The set has great female and male vocals, with female vocals taking a slight edge. Genres like Jpop, Kpop, and instrumental music come off so clean and lively. The overall timbre quality is so amazing, and it easily competes with IEMs around $500 just for vocals alone. Songs like ‘Lilac’ by IU are breathtaking, with IU’s voice sounding almost like an angel, with her voice having so much energy. Male vocals are rich and have color to them as well, with Fuji Kaze’s live rendition of ‘Shinunoga E-Wa’ giving Fuji Kaze’s deep and emotional voice the heft it needs. Ichika Nito’s ‘Awakening’ is so clean, with the guitar just effortlessly singing, it just sounds so good. If I were nitpicking, I feel like this IEM could use a bit more lower-mids, as sometimes vocals can feel a bit thin.")

st.markdown("## ☁️Treble:")
st.markdown("Lastly, the treble. For my personal taste, it is a bit bright. While not painful like the Stellaris, the Blessing 2 Dusk is a bit hot for me. Its lively signature can sometimes make vocals sound too bright. While listening to IU’s ‘Palette’, gives her voice an extra bite to it, with there sometimes being too much energy given the song's lax nature. Nonetheless, the treble is good, with it being a part of why this IEM has such good detail retrieval.")

st.markdown("## 🔎Details:")
st.markdown("For being around $300, this set is quite technical. Everything on this set is great: a wide soundstage, instrumental separation, amazing details, and great note weight. This IEM is probably one of my most resonant that I own, probably around or behind the Stellaris, and on par or better than the S12. Aside from planar IEMs, the Dusk has incredible technical capabilities and fights in the realm with IEMs above its price bracket.")

st.markdown("## 🆚Comparisons(Oracle) and 🏁Conclusion:")
st.markdown("Overall, the Moondrop Blessing 2 Dusk is still a killer IEM for the price. Good bass, stunning vocals, great treble, and stellar details are all reasons this set is still one of the best, if not the best, in its price. However, with the release of the Moondrop Blessing 3, I think that the B3 may replace the Dusk as the best, with its treble being more extended and with better details. Nonetheless, that doesn’t mean that it completely replaces the Dusk, as the Dusk has more bass and a more relaxed signature compared to the Blessing 3. Even when comparing it to my Oracle (the set I spent $500 on) it competes very well with it, with the Dusk having better details than the Oracle, and the Oracle just being better tuned. The fact that this set fights with IEMs almost double its price should tell you more than enough that the Blessing 2 Dusk is an absolute steal. With the creation of the Blessing 3, it may be a little less valuable, but that's not to say this set is still not great. A set that helped to continue to put Moondrop on the map, this IEM helped shape the market and defined its price bracket")
st.write("")
st.write("")



st.markdown("<h2 style='text-align: center;'>Final Score: 3.4/5⭐️</h2>", unsafe_allow_html=True)



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