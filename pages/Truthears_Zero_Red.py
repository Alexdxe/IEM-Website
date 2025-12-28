import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Truthears Zero Red </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 09/20/2023</h4>", unsafe_allow_html=True)

st.markdown("## Video Review:")
st.markdown("Hate reading? Check out my video review of the Truthears Zero Red")
st.video("https://youtu.be/KXR_10Pr_EY")

st.markdown("## 🚩Introduction:")
st.markdown("Every so once in a while, in this hobby, we get a unicorn-like IEM in the hobby that redefines the price-value proposition. For example, The Chu, Starfield, Blessing 2 Dusk, or Variations. But all of those are from the brand Moondrop, a household name in the chifi industry. They’ve helped establish this hobby in ushering in the mainstream audience, and connecting weebs with its anime-like aesthetic. However, I feel like Truthears recently been making a similar impact on the hobby ever since their first drop. They’ve always been an innovator in this space. However, can they keep up with this momentum with the Zero Red? Let’s find out.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown("The IEM comes with a pretty sparse collection of accessories. You get your standard narrow and wide bore tips, a pair of foams, an acceptable cable, and a soft pouch. It’s nothing fancy, but what is notable is the 10 ohm bass adapter. Using this will give you an extra 5 db of bass, which honestly is an incredible add-on at this price. If it weren’t for the bass adapter, the Truhears Zero: Red would have a decent accessory selection, but with the inclusion of it, it boosts the overall value of the package even more. The shells of the IEMs are quite nice too, with a red fabric/sand-looking texture that is eye-catching upon first glance. However, I do have a problem with the fit of the IEMs, as they do have a rather large nozzle. I’d suggest considering this before buying them.")

st.markdown("## 🔊Overall Sound:")
st.markdown("The Truthears Zero: Red can be described as a neutral with a bass boost. It’s a smooth response with few peaks present. It’s something I would recommend if they seriously did not know what they wanted to listen to in this hobby, but wanted a good IEM nonetheless. It's just everything good to great, making it an easy recommendation.")

st.markdown("## 💣Bass:")
st.markdown("While some may feel like there isn’t enough bass on the reds, the quality of bass is amazing. The Dynamic Driver that is handling bass is amazing, with the bass being thumpy but by no means muddy. Personally, this is more than enough bass for me, as when I first listened to these, I was thoroughly surprised by the bass they produced.  Songs like ‘Starboy’ or ‘Humble’ were so fun to listen to, as they had lively and punchy bass, which by no means bled into the vocals. I would go as far as to say these have some of the best bass I’ve heard on any IEM south of 200, which is incredibly impressive considering these only cost 55.")

st.markdown("## 🎤Mids:")
st.markdown("By far the best part of the Reds is the vocals. Vocals come off so clean and natural; it’s just so beautiful. Not shouty or in your face, but rather neutral. It’s for this main reason that I love this IEM so much, because to get tuning this beautiful at this price is incredible. This set almost feels like a budget oracle in a sense, and while not completely the same, I do feel some slight similarities when listening to both. Listening to ‘Seisyun Complex’ by Kessoku Band was so fun on this track, as everything was just done to perfection. From the Drums, Bass, Guitars, and vocals, man, I loved EVERYTHING while listening to the Reds. However, if you enjoy listening to Female vocals with a lot of energy like Ariana Grande, I feel like these IEMs may not have enough energy to really make her voice pop.")

st.markdown("## ☁️Treble:")
st.markdown("The treble only helps the overall naturalness of these IEMs. It’s smooth and doesn't really take away from the mid-range or bass at all. By no means wowing or incredible, I still really like the way it’s done on the Red. Personally, I would like a little more to make certain genres like Jpop and Kpop pop that much more.")

st.markdown("## 🔎Details:")
st.markdown("This IEM has similar technical chops as IEMs in its price tag. It has a pretty wide soundstage, good detail retrieval, and great instrumental separation. The red plays in the same realm as the Aria or Zero, good technicalities, but nothing out of the ordinary.")

st.markdown("## 🆚Comparisons(Zero):")
st.markdown("Compared to the Zero, it’s a lot more natural than its harman tuned counterpart. If you enjoy a cleaner and fun signature, I would recommend the Truthears Zero, as it plays better with more energetic and upbeat genres like K-pop or J-pop. However, if you like a more natural and fuller vocal experience, I recommend the Reds, as vocals come off just so amazing. Personally, if I were given 100 dollars to purchase an IEM, I would just buy both of these and leave the hobby. Both offer something different to the table and are unique enough to warrant having both. I personally prefer the natural tonality of the Red more than the Zero.")

st.markdown("## 🏁Conclusion:")
st.markdown("There isn’t an IEM I’ve heard besides the Wan’er that has made me really reconsider spending money on this hobby, and this is just one of those few one-in-a-million IEMs that everyone should at least listen to once. It’s amazing to achieve tuning like this at the sub-50-dollar price point, and it shocks me with how natural it does both bass and mid-range. Just buy the Reds.")
st.write("")
st.write("")


st.write("")

st.markdown("<h2 style='text-align: center;'>Final Score: 3.2/5⭐️</h2>", unsafe_allow_html=True)



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