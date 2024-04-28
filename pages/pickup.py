from openai import OpenAI
import streamlit as st
import pandas as pd
import pydeck as pdk

st.sidebar.image("images/furniture_reformer.png", width = 200)
st.sidebar.page_link("homepage.py", label = "Home")
st.sidebar.page_link("pages/pickup.py", label = "Pick Up Furniture")
st.sidebar.page_link("pages/disposewithmap.py", label = "Dispose/Donate/Sell Furniture")
st.sidebar.page_link("pages/conditionsystem.py", label = "Determine Furniture's Condition")

st.title("Pick Up Furniture")

message_1 = "Click the name to learn more."
st.header(message_1)

client = OpenAI(api_key="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") 

def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model = model,
        messages = [{
            "role": "user",
            "content": prompt
        }],
    )
   
   return completion.choices[0].message.content

# Create a dataframe with latitudes, longitudes, labels, and information
data = pd.DataFrame({
    'latitude': [37.359520, 37.376300, 37.291370, 37.292900, 37.323908],
    'longitude': [-121.869583, -121.915660, -121.879540, -121.966520, -121.92155],
    'label': ['Habitat for Humanity ReStore San Jose', 'What a Room', 'HopeThrift', 'Home Consignment Center', 'Goodwill Industries of Silicon Valley'],
    'info': ['https://restore.habitatebsv.org/bay-area-restores/san-jose/', 'https://whataroom.com/', 'https://hope-thrift.org/', 'https://thehomeconsignmentcenter.com/', 'https://goodwillsv.org/']
})

with st.form(key = "chat"):
    furniture_types = ["Sofa", "Table", "Chair", "Bed", "Desk", "Cabinet"]
    selected_furniture = st.multiselect("Which types of furniture would you like to pick up?", furniture_types)
    location = st.text_input("Enter your location")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        places = ', '.join(data['label'])
        prompt = f"I'm looking to pick up {', '.join(selected_furniture)} in {location}. Can you advise me on where I can do this? Tell about {places} and more."

        with st.spinner("Please wait..."):
            st.write(get_completion(prompt))

            #Display the links as hyperlinks
            with st.expander("Locations to Pick Up Furniture"):
                for i in range(len(data)):
                    st.markdown(f'<a style="color: orange;" href="{data["info"][i]}">{data["label"][i]}</a>', unsafe_allow_html=True)
                    #st.markdown(f"[{data['label'][i]}]({data['info'][i]})")

            message_2 = "Hover the cursor over the map to learn more."
            st.header(message_2)

            # Create a map with pydeck and streamlit
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(
                    latitude=data['latitude'][0],
                    longitude=data['longitude'][0],
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'ScatterplotLayer',
                        data=data,
                        get_position='[longitude, latitude]',
                        get_color='[200, 30, 0, 160]',
                        get_radius=200,
                        pickable=True,
                        auto_highlight=True
                    )
                ],
                tooltip={
                    'html': '<b>{label}</b>: {info}',
                    'style': {
                        'backgroundColor': 'steelblue',
                        'color': 'white'
                    }
                }
            ))