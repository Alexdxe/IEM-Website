import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Letshuoer S12 </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 03/11/2023 </h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the Letshuoer S12:")
st.video("https://youtu.be/K3-et0f3NUM")

st.markdown("## 🚩Introduction:")
st.markdown("This is the Shouer S12, a planar IEM that has shaken the ~$200 price range, with its unique tuning and amazing details. It's no wonder many have fallen in love with this set over time. So, what makes this set so special and stand out in today's oversaturated market? Let me explain.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("Starting with what's inside the box, it includes the Unit itself, a fairly well-braided cable, 2-3 sets of eartips (it's been a while, I forgot), and a hard carrying case. Honestly, the IEM is very well built, being quite hefty, while the cable is also nice and well-made. The pattern on the cable is unique and really speaks to this set as a whole. ")

st.markdown("## 🔊Overall Sound:")
st.markdown("The S12 is a V-shaped IEM that emphasizes both mid-bass and treble. This signature will be a love or hate for many, as the unique yet well-executed tuning means this IEM will be received as positively as eggnog. It has a unique party trick that I think many should at least try once.")

st.markdown("## 💣Bass:")
st.markdown("Let’s talk about the bass. The Sub-bass on this set is nice and rumbly. It hits with authority, and while the sub bass is goodamazing, the mid-bass is fantastic. There's an abundance of it here, and most likely the thing many will love the most about this set. While listening to 'Pray for Me' by Kendrick Lamar and The Weeknd, the bass is lively and really adds to the track, while not being muddy in any way, being well separated from the other frequencies.")

st.markdown("## 🎤Mids:")
st.markdown("The mids naturally take a hit due to the emphasis on both bass, and treble. Female vocals sound like they lack a bit of life, or if they are being pulled back, with some instruments having a metallic feeling to them. Listening to 'Genesis of Aquarion' by AKINO, the vocals just seem unnatural and are not allowed to sing as they should, and Ichika Nito’s 'Picturesque', where the guitar isn’t as beautiful as it really should be. When you have a sound signature like this, one thing must give, and in this case, it's vocals. I'm not saying that IEM cannot do mid-range, but there's going to be a slight recess in it.")

st.markdown("## ☁️Treble:")
st.markdown("My lord, does this set have treble. Music comes across as sometimes sharp and overall with tons of energy. It's fun and adds to the energetic signature of this IEM, with music sometimes coming across harsh for some.  Cymbals may come off a bit too pronounced, and at times are too much in your face, with vocals being peaky and sometimes hard to listen to. Personally, I don't mind it as much as others, but I feel like for many this will be too much treble, as it's in your face and ruins the Mid-Range(Which we will get to later). However, for genres like Hip-Hop, R&B, Pop, and other energetic genres, the treble adds to the overall energy of the tracks and makes them fun to listen to.")

st.markdown("## 🔎Details:")
st.markdown("In short, it does all of aspects of technicalities well. This set is very technical, having an amazing wide-soundstage, good imaging, and amazing Instrumental separation. Details are stellar as well, with it most likely competing with headphones $100-200 above its price in sheer detail level. For a more analytical listen, you’d be hard-pressed to find anything around $150 that has this many amazing technicalities (besides the Stellaris)")

st.markdown("## 🆚Comparisons(FD3, Kato):")
st.markdown("Let’s wrap up with a short comparison section. The Fiio FD3 is an IEM that also went for a V-Shape sound signature, but in comparison, came off much warmer. The bass bleeds on the FD3 quite a bit, meaning it dominates the other frequencies and masks the rest of the mix. In comparison, the S12 comes off as sharper and more defined, as while it does not have the bass amount like the FD3, it has clarity, details, and a more refined overall signature.")
st.write("")
st.markdown("The Kato is a benchmark at $200, with its tonality being one of my favorites within the space today. In comparison to the S12, it’s a battle of technicalities vs tuning. If you want a smooth, yet natural IEM, the Kato is a great pick. Otherwise, the S12 is a vibrant IEM that emphasizes fun and details. For my taste, the Kato is something I would much rather grab to listen to daily, as its tonality is spot on.")

st.markdown("## 🏁Conclusion:")
st.markdown("The S12 is just a set that hits the nail on the head. For its price, it provides lots of bass and treble, allowing certain genres shine, and for some, a bit too bright. It's a set that really needs a listen before purchasing, because of its fatiguing treble. With a signature that bright, it can be hard to listen to for long periods of time, which is why I would recommend demoing this set before buying it. With that being said, under $200, it’s very competitive and carves out its own niche in today's market.")
st.write("")
st.write("")

st.markdown("<h2 style='text-align: center;'>Final Score: 3/5⭐️</h2>", unsafe_allow_html=True)


##Hide old sidebar:
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True)


##New sidebar:
with st.sidebar:
    st.header("Navigation")
    st.page_link("home.py", label="Home")

    st.page_link("pages/Tierlist.py", label="Tier List")
    st.page_link("pages/Database.py", label="Database")
    st.page_link("pages/Reviews.py", label="Reviews")
    st.page_link("pages/Daily_Drivers.py", label="Daily Drivers")