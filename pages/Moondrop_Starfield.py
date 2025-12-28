import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Moondrop Starfield </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 03/20/2023</h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the Moondrop Starfield:")
st.video("https://youtu.be/uaN7Af1hzWU")
st.markdown("## 🚩Introduction:")
st.markdown("The Moondrop Starfield is one of those few IEMs that was able to break out of the hobby and make its way into the American market. With many reviews of it already being made, it's no wonder that this set has been so celebrated and purchased. However, with Starfield being released around 3 years ago, does this still compete in today’s ever-evolving market? Let’s find out.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("Starting with what's included in the box, it includes the units themselves, a cable, a hard carrying case, filters, tweezers, and ear tips. The IEM has this beautiful metal blue shell, with the design being based on the stars or the night sky. The color palette and design remind me of my favorite V-Tuber, Hoshimachi Suisei. Back to the contents, the cable that comes with the set is pretty garbage. It feels cheap and feels like it was made with literal cents. While I love the color of the cable, everything else about it is pretty disgusting. The ear tips are also cheap and standard, so really, the units themselves are the only nice thing about this. The comfort on the Starfield is also fairly comfortable, as its shell isn’t too large and is non-fatiguing to wear. One side note is that the IEM’s paint has been reported to chip, so be careful when using this piece of gear.")

st.markdown("## 🔊Overall Sound:")
st.markdown("The Starfield is a V-Shaped IEM with a vocal emphasis. It’s a pleasing signature that I think most can enjoy, as it adds enough bass and treble to not make it a boring listen. It’s a profile that has been done by many IEMs in its price category (Aria, T3 Plus, Titan S) and takes a darker approach in comparison to the other two.")

st.markdown("## 💣Bass:")
st.markdown("There is noticeably more mid-bass than there is sub-bass. The mid-bass is fun and doesn’t hit with the most authority. The decay on the mid-bass is clear, and while not the cleanest separation from the mid-range, it still allows it to shine. The sub-bass is a bit lacking, as bass heads will feel this set to not have enough and desire more. The first few seconds of Egoist’s 'The Meaning of Love' come across with a lack of impact, making me want more while listening. ")

st.markdown("## 🎤Mids:")
st.markdown("The Mid-range on this set can be described as slightly warm. This means male vocals will come off with a bit more heft, while female vocals may not come off as clear. A good example would be 'Cinema' by Vivid Bad Squad, a track that has both Female and Male Vocals in it. I feel as if the male vocals in this track are more well done than the female’s, as their voice’s can come off with more emphasis. Not saying this set cannot do female vocals, far from it. Hoshimachi Suisei’s 'Stellar Stellar' is a perfect example of this set being able to do female vocals fine; however, I cannot help but feel as if her voice doesn’t come off as the cleanest. Instrumental on this set is good too, with 'Away' by Ichika Nito sounding solid, and other instruments like the piano or drums being serviceable too")


st.markdown("## ☁️Treble:")
st.markdown("Finally, we have treble, and this is where we run into some issues. The Starfield has just a touch of mid treble, which is how forward vocals may come off or how peaky/sibilant an IEM can be. This makes vocals come off a bit tame. I personally don’t think it's dark, but I would say this set leans in that direction. However, The Air region is probably my biggest complaint. This is Upper Treble, and what this does to an IEM is it makes cymbals sound too pronounced, guitar strings that are plucked a bit hard to listen to, and even the piano comes off a bit peaky. Bringing back 'Away' by Ichika Nito, the guitar felt hars,h and especially at 1:10, I had to lower the volume on this set because the guitar was just too sharp for my ears. This is my biggest complaint about The Starfield, and in my opinion needs a bit of work.")

st.markdown("## 🔎Details:")
st.markdown("Technical Performance time, and really, I feel like this set does one thing really well: Imaging. This set really nails it, with me being able to pinpoint most instruments and where they are located. I specifically remember listening to Hoshimachi Suisei’s Ghost, and literally being able to identify where each instrument was, which is fairly incredible. The sound stage is decently wide, and this set has a good amount of details and solid instrumental separation. However, that imaging for me is the best that this set has to offer technically.")

st.markdown("## 🆚Brief Comparisons (S12, Aria, Hexa) and 🏁Conclusion:")
st.markdown("So, what are my final thoughts? I believe that while the Starfield is a legend in this hobby and community, there are just so many options nowadays in today's market that it makes the Starfield difficult to compete with those around it. Examples could be the S12, an IEM with far better technicalities and is a fun listen, the Moondrop Aria, which is a cheaper Starfield, or the Truhears Hexa, a $80 IEM that is tuned similarly to the Blessing 2. If you are looking for an IEM with a similar sound signature, buy the Aria; the only reason to buy the Starfield is for the paint job, unfortunately. That's not to say this IEM is bad, but to say it’s still competitive in today’s market is a bit of a stretch. Despite all this, I love the Starfield because it’s the headphone that sank me into this hobby, which is why I still cherish mine to this day.")
st.write("")
st.write("")

st.markdown("<h2 style='text-align: center;'>Final Score: 2.4/5⭐️</h2>", unsafe_allow_html=True)



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