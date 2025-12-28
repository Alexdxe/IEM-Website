import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Tangzu Wan'er </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 04/06/2023</h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the Tangzu Wan'er:")
st.video("https://youtu.be/nMaCaXWrZK4")

st.markdown("## 🚩Introduction:")
st.markdown("Tangzu has been a brand that has absolutely taken over the market as of late, with releases like the Wu Zeitan, Heyday, the new Shimli encounter, and the IEM we will be taking a look at, the Wan’er. An IEM that’s priced at $20, and faces tons of stiff competition in today's market, so how good is it actually? Let’s find out.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("The Wan’er comes with a small selection of small, medium, and large silicone tips, alongside a graphic cleaning cloth to help clean your IEM. The cable is quite gross, as it’s thin, tangles, and feels incredibly cheap. But the IEM is 20 USD, so I will let it slide. The shells themselves are great, with a pattern to the face plate, alongside a metal nozzle, which is a great addition. Overall, good enough for a $20 set.")

st.markdown("## 🔊Overall Sound")
st.markdown("The wan’er can be described as a neutral + bass boost. It’s impressively natural-sounding at the price, and even more so when you realize it’s only $20. It’s clean, vocal-forward, and somewhat relaxing all at the same time.")

st.markdown("## 💣Bass:")
st.markdown("Mid-bass is thumpy but has very little decay to it. It's not full body, but there is enough to give many tracks life. I feel like I would like a little more personality in my music, but I can’t really complain too much because I’m not the biggest bass head. The sub-bass also feels like it’s lacking a bit, with rumbles and growls missing a little bit of authority. While not a bassy IEM, the Wan’er does have enough bass to make most genres fun.")

st.markdown("## 🎤Mids:")
st.markdown("I’m just going to say it, I love the mid-range with this set. Vocals come off so naturally, with any track I throw at the Wan’er able to do vocal recreation just fabulously. Genesis of Aquarion sounds downright gorgeous, with her voice absolutely just singing. 'Shinunoga E-Wa' (Live ver. at Budokan) just melts my ears, with Fuji Kaze’s voice sounding ever so buttery smooth. Instrumental sounds clean as well, while listening to 'Zankyousanka' (Instrumental ver.), all instruments were natural sounding and just came off with so much life. Easily, the best thing about this set. One thing I do want to note is that vocals often don’t feel like they are front and center. With this IEM, it often feels like they are behind the instrumental; whether that is the drums or guitar, they are not the center of attention here. For example, in The Foo Fighter's 'Pretender', the guitar is more emphasized than Dave Grohl's voice, having his voice pushed just a bit back. However, they are still able to sing effortlessly and still sound absolutely amazing.")

st.markdown("## ☁️Treble:")
st.markdown("Treble time, and surprisingly, this IEM does treble really well for an IEM around this price. I would say this set leans more towards the relaxed side, with the overall energy of this set being lower than most IEMs I’ve heard. Everything just comes off more intimate in this set because of this, and it really helps vocals feel just so much nicer. The treble also rolls off at around 10k, making this set non-fatiguing to listen to. Cymbal hits and vocals aren’t overpronounced, which makes this a great IEM to listen to for long periods of time.")

st.markdown("## 🔎Details:")
st.markdown("Finally, we move on to the details. With the Wan’er only costing $20, that means it's most likely not made with the most expensive parts, meaning that the technical performance is naturally lacking. Everything takes a hit here; however, it's basically a given at this price.")

st.markdown("## 🆚Comparisons(Chu and Aria):")
st.markdown("When comparing it to the Moondrop Chu, the Wan’er comes off as much more natural. The Wan’er is noticeably less hot in the treble and has more bass than the Chu. If you want a brighter listening experience, the Chu is still a great option, but if you want something more vocal-forward and correct-sounding, the Wan’er is an excellent pick.")
st.write("")
st.markdown("This may come as a shocker, but I much prefer the Wan’er over the Aria. While the Aria is the better IEM overall, having a better bass and detail retrieval, Wan’er’s tuning is more to my taste. It’s presentation of mids is just so good at this price range, and for 4x less, the Wan’er is just a steal.")

st.markdown("## 🏁Conclusion:")
st.markdown("The Tangzu Wan’er is truly amazing. At its price, I genuinely think it's one of the best IEMs on the market in its price range. For 20 dollars, it beats out most sets 5x its price in tuning, which is crazy. I love my Wan’er so much, I listen to it alongside my Oracle, Blessing 2 Dusk, Kato, and S12. All IEMs leagues are more expensive than it, yet I have this urge to pull it out to listen so often. When it comes to budget IEMs, you really aren’t going to find anything better than this. Just buy the Wan’er.")
st.write("")
st.write("")



st.markdown("<h2 style='text-align: center;'>Final Score: 2.6/5⭐️</h2>", unsafe_allow_html=True)



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
