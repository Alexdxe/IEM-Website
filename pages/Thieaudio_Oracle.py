import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'>Thieaudio Oracle</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Written on 03/04/2023</h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the Thieaudio Oracle.")
st.video("https://youtu.be/TIIglsY03eE")

st.markdown("## 🚩Introduction:")
st.markdown("Thieaudio is an audio brand that has exploded in the last 2-3 years,  known for its beautiful shells, brilliant tuning, and excellent cables. Some of its most successful models are the Legacy line, its tribrids (which are basically earbuds with three different drivers making the music), and its endgame flagships. One of their most popular models is the Oracle, a $540 tribrid IEM that features two ESTs, two BAs, and a dynamic driver. However, how does this IEM hold up against today's market? Let's find out.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("Starting with what is included in the box, the contents include a cleaning cloth, a hard case, 2 sets of tips (one foam and one silicone), and the headphones themselves alongside the cable. The IEM can be bought with different termination plugs, the options being 3.5, 4.4, and 2.5 with a 3.5 and 4.4 adapter. One thing that honestly surprised me was how light it is, weighing lighter than most of my IEMs. The cable quality for this set is amazing, it's lightweight, does not feel cheap, and is super clean. Finally the shell design for this set is masterful, with the resin housing being a half rock/shattered glass pattern, and the other half being a gradient pattern, with the left side being a purple to light blue, and the right a pure light blue. I love the look of almost all of Thieaudio’s products, and while this is my first purchase from them, I can confidently say they make some of the best looking In ears on the market.")

st.markdown("## 🔊Overall Sound:")
st.markdown("The Oracle is a neutral IEM with a slight emphasis on bass and upper mid-range. While listening to it, the Oracle always sounds like a flowing river. It’s smooth, clean, yet so natural in both timbre and vocals. It’s a vocal lover’s dream IEM.")

st.markdown("## 💣Bass:")
st.markdown("There is plenty of both sub-bass and midbass to go around to make genres like EDM, Pop, or R and B feel lively and energetic. The bass is punchy and well defined, while the sub-bass shakes my body with how nice and deep the notes hit. When listening to “The Meaning of Love'' by EGOIST, I could feel the sub-bass rumble in the first few seconds of the song, as it echoed through my head. While in 'Pray for Me' by the Weekend/Kendrick Lamar, the thumps and slam is present throughout the track, backing both men’s vocals, creating an incredibly fun listen. While not the most detailed and analytical bass, it's satisfying and meaty, hitting with authority but at the same time not overwhelming the other frequencies.")

st.markdown("## 🎤Mids:")
st.markdown("The mid-range, don’t even get me started on the mid-range. If you don’t know, mids is everything and anything, vocals and instrumental. This is the part where this set shines the most, and has absolutely stolen my heart. The Instrumental is clean and natural-sounding. When listening to ‘Picturesque’ by Ichika Nito, the electric guitar just sings in that track, with it sounding more angelic than ever. And the vocals, holy sh*t. This IEM does vocals alright. When listening to music with more delicate female/male vocals, my lord, do they just shine. The song ‘Genesis of Aquarion’ literally gave me goosebumps, with the energy of the chorus stealing my heart. And that's not to say this set can't do more upbeat/busy tracks. ‘The Pretender’ by the FooFighters was, while not as amazing as the other tracks listed above, worked great on these headphones. It's safe to say that, around 500 dollars, the mid-range on this set is near the top of that price bracket. ")

st.markdown("## ☁️Treble:")
st.markdown("Moving on to Treble, and honestly, it's great. There's enough sparkle to make vocals shin,e and cymbal crashes to feel present, while at the same time not being dark. It's decently well extended, and for the most part is good, but not outstanding. The upper treble is not peaky or metallic, which again adds to the overall natural-sounding presentation of this set. The treble does its job here, but is no means a set for Treble-heads.")

st.markdown("## 🔎Details:")
st.markdown("Finally, we have the technical performance. In my opinion, this is where the Oracle falls off a tiny bit. When comparing it to my Blessing 2 Dusk, I can tell almost immediately that the Blessing 2 just has better details overall. Soundstage, imaging, and instrumental separation fall short on the Oracle compared to IEMs around its price range and even below it. Especially the Instrumental separation, where I feel this set doesn't do it the best, and often in busier tracks, it feels as if everything (vocalist, guitars, bass, drums, etc.) is being blended into one. But that's not to say it's not resolving, I just wish it was better, especially for what I paid for.")

st.markdown("## 🆚Comparisons(Blessing 2 Dusk):")
st.markdown("Doing some comparisons, I feel like it's only natural that I compare this to the Blessing 2 Dusk now, a set I mentioned earlier. Starting with bass, the Oracle wins sheerly because often when getting to really busy or heavy mid-bass tracks, the driver's bass sometimes feels dry and as if the driver is hitting its limit while playing those notes, while on the Oracle, the bass is done better because the bass doesn’t have this problem and is more satisfying. The mid-range on the Oracle can be described as more natural and beautiful, while the Dusk is a step below, having a less natural-sounding mid-range; however, doing energetic tracks better than on the Oracle. Treble on both sets is fine, with again, the oracle being more tame than the dusk. And finally, as mentioned earlier, overall details and resolution are going to be better on the Dusk than the Oracle. With that being said, which do I prefer? To me, the oracle is just too beautiful, and its mid-range has stolen my heart in ways the dusk cannot. However, I believe because the dusk is cheaper and performs around 85-90% of the Oracle, it's still well worth your money and is a killer at its price range of around 300.")

st.markdown("## 🏁Conclusion:")
st.markdown("Thieaudio has seriously outdone themselves with this set, a tribrid that has ruined my ears for any new IEMs that come across my table, and swoon my heart with vocals that could take me to heaven. It’s become my favorite IEM, and rightfully so, as this is my most expensive set to date. If you are looking for an IEM that is well-tuned from bass to treble that works well with almost anything you run through it, look no further than this set.")
st.write("")
st.write("")


#Image:
photo = Image.open("images/oracle.jpg") 
left, center, right = st.columns([1, 7, 1])
with center:
    st.image(photo, width=750)
st.write("")

st.markdown("<h2 style='text-align: center;'>Final Score: 4/5⭐️</h2>", unsafe_allow_html=True)



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



