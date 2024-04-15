import streamlit as st 
from openai import OpenAI
import pydeck as pdk

client = OpenAI(api_key='my-api-key-here')

def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
         {
      "role": "user",
      "content": "Write a lesson plan for ways a person can modify or clean up their old furniture as a way for them to donate for someone else to use. The lesson plan should cover cleaning, rebuilding, and getting it ready for another person to use."
    }
  ],
    )
   return completion.choices[0].message.content

# create our streamlit app
def streamlit_app():
    furniture_type = st.selectbox("Please select the type of furniture:", ["Bed", "Table", "Chair", "Sofa", "Desk"])
    prompt = f"Write a lesson plan for ways a person can modify or clean up their old {furniture_type} as a way for them to donate for someone else to use. The lesson plan should cover cleaning, rebuilding, and getting it ready for another person to use. Provide the list in bullet point format."
    response = get_completion(prompt)
    st.write(response)

if __name__ == "__main__":
    streamlit_app()