import streamlit as st

# Set the page configuration
st.set_page_config(layout="wide")

# Page Title, Logo, and Version
st.title("DPD 360 Marketing")
st.image("/Users/siddu7/PycharmProjects/DPD ease/Publications-Division-removebg-preview.png", caption="Company Logo", use_column_width=True)

# Display Version
st.write("2.1.0 Alpha Version")
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottefile(filepath:str):
    with open(filepath,"r")as f:
        return json.load(f)

lottie_coding = load_lottefile("/Users/siddu7/PycharmProjects/DPD ease/Animation - 1702798340581.json")

st.title("The all in one digital marketing solution")

st_lottie(
    lottie_coding,
    reverse=False,
    loop=True,
    quality="low",

    height=None,
    width=None,
    key = None,

)
# Description
st.title("What would you like to try first?")

# Buttons
options = [
    "AI Magazine Email Generator",
    "ML Book Generator",
    "AI Optimized SEO Article Writer",
    "Book Content to Post Maker",
    "View DPD Site (Made with Atomic Design)",
    "Lead Magnet",
    "Posts Scheduler",
    "Install Employment News App"
]

# Display buttons horizontally
cols = st.columns(4)

for i, option in enumerate(options):
    cols[i % 4].button(option, key=f"button_{i}")

# Button actions (optional)
if st.button("Go"):
    st.write("You clicked the 'Go' button")
