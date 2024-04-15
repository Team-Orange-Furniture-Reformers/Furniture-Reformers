import streamlit as st 
from openai import OpenAI
import pydeck as pdk

client = OpenAI(api_key="My API Key") 

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
         {
      "role": "user",
      "content": prompt
    }
  ],
    )
   return completion.choices[0].message.content

# create our streamlit app
with st.form(key = "chat"):
    location = st.text_input("Please enter your location:")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        prompt = f"Pretend you work for the city and need to give a college student information on where to find used furniture based on their needs, provide a website link for the locations. The student is in {location}."
        response = get_completion(prompt)
        st.write(response)

        