from openai import OpenAI
import streamlit as st
import pandas as pd
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
    furniture_types = ["Sofa", "Table", "Chair", "Bed", "Desk", "Cabinet"]
    selected_furniture = st.multiselect("Which types of furniture do you want to dispose of?", furniture_types)
    disposal_method = st.radio("How would you like to get rid of your furniture?", ["Donate", "Sell", "Pickup"]) 
    location = st.text_input("Enter your location")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if disposal_method == "Pickup":
            st.write("You can schedule a pickup for your furniture at this website: [San Jose Pickup Service](https://www.sanjoseca.gov/your-government/departments-offices/environmental-services/recycling-garbage/residents#:~:text=Free%20Junk%20Pickup,(408)%20535%2D3500.)")
            st.write("Phone number for the service: (408) 535-3500")
        else:
            prompt = f"{disposal_method} {selected_furniture} in {location}"
            response = get_completion(prompt)
            st.write(get_completion(prompt))

# Create a dataframe with latitudes, longitudes, labels, and information
            data = pd.DataFrame({
            'lat': [37.359520, 37.3221, 37.3821, 37.3351, 37.323908, 37.3201],
            'lon': [-121.869583, -121.9269, -121.8966, -121.8956, -121.92155, -121.9175],
            'label': ['Habitat for Humanity ReStore San Jose', 'Hope Services', 'RAFT', 'Salvation Army', 'Goodwill Industries of Silicon Valley', 'HomeFirst'],
            'info': ['https://restore.habitatebsv.org/bay-area-restores/san-jose/', 'https://www.hopeservices.org/', 'https://raft.net/how-you-can-help/donate-materials/', 'https://siliconvalley.salvationarmy.org/', 'https://goodwillsv.org/', 'https://www.homefirstscc.org/how-to-support']
})

# Create a map with pydeck and streamlit
            st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
            latitude=data['lat'][0],
            longitude=data['lon'][0],
            zoom=11,
            pitch=50,
            ),
            layers=[
            pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
            pickable=True,
            auto_highlight=True
            ),
            ],
            tooltip={
            'html': '<b>{label}</b>: {info}',
            'style': {
            'backgroundColor': 'steelblue',
            'color': 'white'
        }
    }
))
