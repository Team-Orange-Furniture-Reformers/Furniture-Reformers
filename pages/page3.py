from openai import OpenAI
import os
import base64
import streamlit as st
from st_pages import Page, show_pages

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

st.set_page_config(page_title="Determine Condition", page_icon="images/logo.png", layout="wide")

st.sidebar.image("images/furniture_reformer.png", width = 200)
st.sidebar.page_link("main_page.py", label = "Home")
st.sidebar.page_link("pages/page1.py", label = "Pick Up Furniture")
st.sidebar.page_link("pages/page2.py", label = "Dispose/Donate/Sell Furniture")
st.sidebar.page_link("pages/page3.py", label = "Determine Furniture's Condition")

st.title("Determine Furniture's Condition")

uploaded_file = st.file_uploader("",type=["png", "jpg", "jpeg"])

client = OpenAI(api_key="OpenAI_API_KEY")

image_path = "images/"

def photo_rec(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": """What is the furniture's condition in this image?
             If the furniture cannot be repaired, advise the user how to dismantle it.
             If the furniture can be repaired, advise the user on how to repair it.
             If the furniture is in good condition, advise the user on how to maintain it.
             Answer in a short and detailed manner and under 300 words/tokens."""},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
            },
        ],
        }
    ],
    #max_tokens=300, # Maybe get rid of
    )
    return response.choices[0].message.content


if uploaded_file is not None:
    with open(os.path.join('images',uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success("Saved File:{} to images".format(uploaded_file.name))
    image_path = os.path.join('images',uploaded_file.name)
    st.image(image_path)
    content = photo_rec(image_path)
    with st.spinner("Please wait..."):
       st.write(content)