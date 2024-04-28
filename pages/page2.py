from openai import OpenAI
import streamlit as st
import pandas as pd
import pydeck as pdk
from st_pages import Page, show_pages

st.set_page_config(page_title="Dispose/Donate/Sell", page_icon="images/logo.png", layout="wide")

st.sidebar.image("images/furniture_reformer.png", width = 200)
st.sidebar.page_link("main_page.py", label = "Home")
st.sidebar.page_link("pages/page1.py", label = "Pick Up Furniture")
st.sidebar.page_link("pages/page2.py", label = "Dispose/Donate/Sell Furniture")
st.sidebar.page_link("pages/page3.py", label = "Determine Furniture's Condition")

st.title("Dispose/Donate/Sell Furniture")

client = OpenAI(api_key="OpenAI_API_KEY") 

# Create a wrapper function
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
    'latitude': [37.359520, 37.3221, 37.3821, 37.3351, 37.323908, 37.3201],
    'longitude': [-121.869583, -121.9269, -121.8966, -121.8956, -121.92155, -121.9175],
    'label': ['Habitat for Humanity ReStore San Jose', 'Hope Services', 'RAFT', 'Salvation Army', 'Goodwill Industries of Silicon Valley', 'HomeFirst'],
    'info': ['https://restore.habitatebsv.org/bay-area-restores/san-jose/', 'https://www.hopeservices.org/', 'https://raft.net/how-you-can-help/donate-materials/', 'https://siliconvalley.salvationarmy.org/', 'https://goodwillsv.org/', 'https://www.homefirstscc.org/how-to-support']
})

# Create our streamlit app
with st.form(key = "chat"):
    furniture_types = ["Sofa", "Table", "Chair", "Bed", "Desk", "Cabinet"]
    selected_furniture = st.multiselect("Which types of furniture would you like to get rid of?", furniture_types)
    disposal_method = st.radio("How would you like to get rid of your furniture?", ["Donate", "Sell", "Dispose"]) 
    location = st.text_input("Enter your location")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if disposal_method == "Dispose":
            st.write("You can schedule a pickup for your furniture at this website: [:orange[San Jose Pickup Service]](https://www.sanjoseca.gov/your-government/departments-offices/environmental-services/recycling-garbage/residents#:~:text=Free%20Junk%20Pickup,(408)%20535%2D3500.)")
            st.write("Phone number for the service: :orange[(408) 535-3500]")
        
        elif disposal_method == "Donate":
            places = ', '.join(data['label'])
            prompt = f"I'm looking to donate {', '.join(selected_furniture)} in {location}. Can you advise me on where I can do this? Tell about {places} and more."

            with st.spinner("Please wait..."):
                response = get_completion(prompt)
                st.write(get_completion(prompt))
            
            # Display the links as hyperlinks
            with st.expander("Locations to Donate Furniture"):
                for i in range(len(data)):
                    st.markdown(f'<a style="color: orange;" href="{data["info"][i]}">{data["label"][i]}</a>', unsafe_allow_html=True)
                    #st.markdown(f"[{data['label'][i]}]({data['info'][i]})")

            message = "Hover the cursor over the map to learn more."
            st.header(message)
            
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
        
        else:
            prompt = f"I'm looking to sell {', '.join(selected_furniture)} in {location}. Can you advise me on where I can do this?"
            with st.spinner("Please wait..."):
                st.write(get_completion(prompt))