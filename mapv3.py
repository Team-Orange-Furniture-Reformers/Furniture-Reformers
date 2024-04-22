import streamlit as st
import pandas as pd
import pydeck as pdk

# Create a dataframe with latitudes, longitudes, labels, and information
data = pd.DataFrame({
    'lat': [37.359520, 37.376300, 37.291370, 37.292900, 37.323908],
    'lon': [-121.869583, -121.915660, -121.879540, -121.966520, -121.92155],
    'label': ['Habitat for Humanity ReStore San Jose', 'What a Room', 'HopeThrift', 'Home Consignment Center', 'Goodwill Industries of Silicon Valley'],
    'info': ['https://restore.habitatebsv.org/bay-area-restores/san-jose/', 'https://whataroom.com/', 'https://hope-thrift.org/', 'https://thehomeconsignmentcenter.com/', 'https://goodwillsv.org/']
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