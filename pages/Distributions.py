import streamlit as st
import pandas as pd

##Data Cleaning and Loading
def load_file():
    return pd.read_csv("data/tierlist.csv")

def count_scores(df):
    return df["Score"].value_counts().reset_index()

def price_bins(df):
    bins = [0, 25, 50, 100, 200, 500, 1000, float("inf")]
    labels = [
        "$0–25",
        "$25–50",
        "$50–100",
        "$100–200",
        "$200–500",
        "$500–1000",
        "$1000+"
    ]
    df['Price Range'] = pd.cut(df['Price'], bins=bins, labels=labels, right=False)
    return df['Price Range'].value_counts().reset_index()


#Initialize Data
df = load_file()
counts = count_scores(df)
price_ranges = price_bins(df) 


##Header
st.markdown("<h1 style='text-align: center;'> 📈Statistics</h1>", unsafe_allow_html=True)
st.markdown("## Summary:")
st.markdown("This is a small collection of graphs in relation to various statistics from my tierlist. The goal is to display any trends in the scores I give IEMs.")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)


##Graph 1: Distribution of Scores
st.markdown("<h2 style='text-align: center;'> Distribution of Scores</h2>", unsafe_allow_html=True)
st.write("")
counts.columns = ["Score", "Count"]
st.bar_chart(counts, x = "Score", y = "Count")
st.markdown("Score distributions are fairly varied, with slight **right skewness**, showing that I tend to give higher scores more often. This could also be because I enjoy what I end up purchasing, as if I knew I wouldn't like it, I wouldn't buy it.")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)


##Graph 2: Distrubution of Prices
st.markdown("<h2 style='text-align: center;'> Distribution of Prices</h2>", unsafe_allow_html=True)
st.write("")
price_ranges.columns = ["Price Range", "Count"]
st.bar_chart(price_ranges, x = "Price Range", y = "Count")
st.markdown("The majority of the IEMs I tried fell within the $100-200 range, which was surprising to me. I figured most of the IEMs I would have tried would be in the lower price ranges, but it seems I gravitated towards mid-tier IEMs more.")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)


##Graph 3: Price vs Score Scatterplot
st.markdown("<h2 style='text-align: center;'> Price vs Score Scatterplot</h2>", unsafe_allow_html=True)
st.write("")
st.scatter_chart(df, x = "Price", y = "Score")
st.markdown("There seems to be a positive correlation between price and score, meaning the more expensive an IEM is, the higher score it tends to receive. This is expected because higher-priced IEMs tend to have better accesories, high quality components, and a more refined sound signature.")
st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)

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




