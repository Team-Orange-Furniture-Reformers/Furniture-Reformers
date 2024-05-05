import streamlit as st

st.set_page_config(page_title="Furniture Reformer", page_icon="images/logo.png", layout="wide")

st.sidebar.image("images/furniture_reformer.png", width = 200)
#st.sidebar.page_link("Home.py", label = "Home")
#st.sidebar.page_link("pages/Free_or_Buy.py", label = "Free or Buy Furniture")
#st.sidebar.page_link("pages/Dispose,_Donate,_or_Sell.py", label = "Dispose, Donate, or Sell Furniture")
#st.sidebar.page_link("pages/Determine_Condition.py", label = "Determine Furniture's Condition")

st.image("images/furniture_reformer.png", width = 525)

st.title("Welcome!")
message = "What would you like to do today?"
st.header(message)

st.divider()  # Add a horizontal line for separation

feature_1 = "Pick Up Furniture"
st.title(feature_1)
description_1 = "Advises you where you can get free or buy furnitures."
st.header(description_1)
st.page_link("pages/Free_or_Buy.py", label = ":orange[Click here to find out more]")

st.divider()  # Add a horizontal line for separation

feature_2 = "Dispose/Donate/Sell Furniture"
st.title(feature_2)
description_2 = "Advises you how to donate, sell, or dispose furnitures."
st.header(description_2)
st.page_link("pages/Dispose,_Donate,_or_Sell.py", label = ":orange[Click here to find out more]")

st.divider()  # Add a horizontal line for separation

feature_3 = "Determine Furniture's Condition"
st.title(feature_3)
description_3 = "Determines the condition of furniture and advises you how to maintain, repair, or dismantle it depending on the condition."
st.header(description_3)
st.page_link("pages/Determine_Condition.py", label = ":orange[Click here to find out more]")