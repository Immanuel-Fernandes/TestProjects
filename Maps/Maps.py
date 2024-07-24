import streamlit as st
import pydeck as pdk
import requests

# Set your OpenCage API key here: https://opencagedata.com/users/sign_up
OPENCAGE_API_KEY = '48ba99fd1e6c4748abde2487b195327d'

# Function to get latitude and longitude from location using OpenCage
def get_coordinates(location):
    try:
        response = requests.get(
            'https://api.opencagedata.com/geocode/v1/json',
            params={'q': location, 'key': OPENCAGE_API_KEY}
        )
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        if data['results']:
            coordinates = data['results'][0]['geometry']
            return coordinates['lat'], coordinates['lng']  # return as (latitude, longitude)
        else:
            return None, None
    except requests.RequestException as e:
        st.error(f"Error fetching data from OpenCage API: {e}")
        return None, None

def main():
    st.title('Map Visualization with Streamlit and Pydeck')

    # Get location input from the user
    location = st.text_input("Enter a location", "New Delhi, India")

    # Get coordinates for the location
    latitude, longitude = get_coordinates(location)

    if latitude is not None and longitude is not None:
        # Set view state based on user input location
        INITIAL_VIEW_STATE = pdk.ViewState(
            latitude=latitude,
            longitude=longitude,
            zoom=10,
            bearing=0,
            pitch=0,
        )

        # Display Map using pydeck's Deck
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=INITIAL_VIEW_STATE,
            layers=[],
        ))
    else:
        st.error("Location not found. Please enter a valid location.")

if __name__ == '__main__':
    main()
