import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'> Truthears Hexa </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Written on 12/26/2025 </h4>", unsafe_allow_html=True)
photo = Image.open("images/hexa.jpg") 
left, center, right = st.columns([1, 7, 1])
with center:
    st.image(photo, width=750)
st.write("")

st.markdown("## 🚩Introduction:")
st.markdown("In December 2022, Truthears would release the Hexa, a 1DD + 3BA hybrid, and it became the benchmark at ~100. The hype and mystique around this IEM was immense, with many going so far as to proclaim the Hexa as a Blessing 2 killer. Were people exaggerating this claim, or does the Hexa truly topple previous $300 benchmark IEMs? Let’s find out.")

st.markdown("## 📦Accessories/Intangables:")
st.markdown(" The Hexa has a fairly basic lineup of accessories. Starting with the cable, it’s pretty terrible. I don’t like its fairly hard/plastic feel, and while it is well behaved, I just don’t like the design. The IEM also comes with a diverse selection of tips, including narrow and wide bore silicone tips, as well as a pair of foams. It’s serviceable and will get the job done if you don’t have other tips. Truthears has also included a soft button pouch for storage. I much prefer the pouch of the Hola/Gate, but I understand where Truthears was coming from, given it came out before either. The shell has a reasonably sized nozzle with an interesting shell shape. I like its geometric design, as it stands out from the rest of the IEMs being released today. Overall, the Hexa reuses all of the accessories from the Truhear Zero, yet costs $30 more. It’s acceptable, but nothing more.")

st.markdown("## 🔊Overall Sound:")
st.markdown("The Hexa is one of the most normal-sounding IEMs I have ever heard. It really has little to fault unless you are truly looking for a more engaging signature altogether. It’s natural, with a slight treble and bass emphasis, not to make the IEM completely reference. Its signature can be described as neutral, with a treble boost.")

st.markdown("## 💣Bass:")
st.markdown("The bass on the Hexa is fairly tame. There’s not a lot of dynamics or impact, but offers a soft rumble, so the listener's experience is not completely sterile. It leans more on sub-bass than mid-bass, which is fairly understandable given the clean/natural signature Truthears was going for. If you are looking for an IEM that has a bass emphasis, look the other way.")

st.markdown("## 🎤Mids:")
st.markdown("The midrange on the Hexa sounds quite natural. The timbre is correct, and the vocals have a slight pop to them. However, I do think my biggest issue with the vocals is that they are not fully extended. This mostly has to do with how the upper midrange is tuned. Because it peaks and does not have extension in the 2-5k region, vocals feel cramped. Despite this nitpick, the Hexa’s midrange is clear with a touch of warmth, making it pleasant to listen to. ")

st.markdown("## ☁️Treble:")
st.markdown("The treble is the Hexa’s standout quality. It’s incredibly well done, with sufficient extension and enough sparkle to make certain aspects of music pop. The treble is also smooth, with little fatigue, even after long listens. I recall putting these on for the first time and just appreciating how well the treble is implemented, complementing the linear bass and natural mid-range perfectly. In summary, the Hexa’s treble is not only smooth, but the slight emphasis on the upper treble gives it some extra sparkle. One of my favorite treble representations on an IEM under $200.")

st.markdown("## 🔎Details:")
st.markdown("With a well-executed treble often comes great detail performance, and the Hexa does not disappoint. It has a fairly wide stage, alongside good instrumental separation to boot. While you are not getting end game level of micro details, you are still able to extract nuances in your music with these IEMs. The Hexa is quite the technical beast at $90, outcompeting most of its peers within its price bracket.")

st.markdown("## 🆚Comparisons(Aria, Kato, Zero/Red, Nova):")
st.markdown("#### Hexa vs Aria:")
st.markdown("Moving on to comparisons, I wanted to start with the IEM that the Hexa was most directly in competition with upon release. The Aria is a legendary IEM at $80, with a V-shaped signature that most people enjoyed. When directly comparing the two, it’s obvious that both IEMs are targeting different audiences. The Hexa offers a cleaner and more neutral recreation of music, while the Aria offers a warmer approach. However, the one quality that sets the Hexa apart from the Aria is its treble. A lot of the IEMs around this price before the Hexa always had this 10k dip, which always made the signature feel slightly incomplete. It wasn’t extended, and as a result, stifled some of the potential detail retrieval the Aria/Starfield could’ve had. However, with the Hexa not having this issue, it clearly cements itself ahead of the Aria")
st.markdown("#### Hexa vs Kato:")
st.markdown("The Kato is where the Hexa is slightly more evenly matched. Both IEMs aim for a different flavor of neutral, with the Kato going for a warmer/smoother approach, whilst the Hexa a more clinical one. Both of these sets trade blows, with the Hexa winning in treble and details, and the Kato prevailing in bass and mids. Both sets are incredible, but if I had to choose only one, I think the slightest of edges goes to the Kato.")

st.markdown("#### Hexa vs Zero/Red:")
st.markdown("Under 100, the Hexa also fights for market space with two of its siblings, the Zero and the Zero: Red. Both IEMs have spectacular qualities about them that set them apart from their peers. The Zero has one of the best bass responses I’ve heard in an IEM, utilizing its dual DD set-up to its full potential. The Zero Red is just a wonderfully tuned IEM. The IEM especially excels in the mid-range, where it is incredibly natural. Overall, each (Hexa, Red, Zero) excels in their own niche, making owning all not redundant. However, my favorite would likely be the Hexa, as its treble response is just too good for me to give up.")

st.markdown("#### Hexa vs Nova:")
st.markdown("Lastly, the Nova is Truthears most expensive model. It tuned to be as true to Harman as possible, meaning it emphasizes both vocal clarity and sub-bass. However, I think the Nova is slightly too lean for me, as the lack of sub-bass and emphasized treble makes the Nova a thin and boring listen. I prefer the Hexa in almost every way to the Nova, outside of non-turning-related aspects.")

st.markdown("## 🏁Conclusion:")
st.markdown("While there have been many IEMs that fall off after a few months of being on the market, the Truthear Hexa has stood the test of time in the hobby’s most competitive price bracket. It is my favorite IEM under 100 USD, and is something I prefer to some other more expensive sets in my collection. If you want something neutral and reference, I cannot think of a better IEM than the Hexa below $150.")
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