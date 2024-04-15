import streamlit as st 
from openai import OpenAI

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
    furniture_types = ["Sofa", "Table", "Chair", "Bed", "Desk", "Cabinet"]
    selected_furniture = st.multiselect("Which types of furniture do you want to dispose of?", furniture_types)
    disposal_method = st.radio("How would you like to get rid of your furniture?", ["Donate", "Sell"]) 
    location = st.text_input("Enter your location")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        prompt = f"{disposal_method} {selected_furniture} in {location}"
        response = get_completion(prompt)
        st.write(get_completion(prompt))
