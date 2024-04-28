import streamlit as st

st.set_page_config(page_title="Furniture Reformer", page_icon="images/logo.png", layout="wide")

st.sidebar.image("images/furniture_reformer.png", width = 200)
st.sidebar.page_link("homepage.py", label = "Home")
st.sidebar.page_link("pages/pickup.py", label = "Pick Up Furniture")
st.sidebar.page_link("pages/disposewithmap.py", label = "Dispose/Donate/Sell Furniture")
st.sidebar.page_link("pages/conditionsystem.py", label = "Determine Furniture's Condition")

st.image("images/furniture_reformer.png", width = 525)

st.title("Welcome!")
message = "What would you like to do today?"
st.header(message)

st.divider()  # Add a horizontal line for separation

feature_1 = "Pick Up Furniture"
st.title(feature_1)
description_1 = "Advises you where you can pick up furnitures."
st.header(description_1)
st.page_link("pages/pickup.py", label = ":orange[Click here to find out more]")

st.divider()  # Add a horizontal line for separation

feature_2 = "Dispose/Donate/Sell Furniture"
st.title(feature_2)
description_2 = "Advises you how to donate, sell, or dispose furnitures."
st.header(description_2)
st.page_link("pages/disposewithmap.py", label = ":orange[Click here to find out more]")

st.divider()  # Add a horizontal line for separation

feature_3 = "Determine Furniture's Condition"
st.title(feature_3)
description_3 = "Determines the condition of furniture and advises you how to maintain, repair, or dismantle it depending on the condition."
st.header(description_3)
st.page_link("pages/conditionsystem.py", label = ":orange[Click here to find out more]")