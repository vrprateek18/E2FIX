import streamlit as st
import folium
import requests

from streamlit_folium import st_folium


# ==========================================================
# REVERSE GEOCODING
# ==========================================================

def reverse_geocode(lat, lon):

    try:

        url = (
            f"https://nominatim.openstreetmap.org/reverse"
            f"?lat={lat}&lon={lon}&format=json"
        )

        response = requests.get(

            url,

            headers={

                "User-Agent":"E2FIX"

            },

            timeout=10

        )

        data = response.json()

        address = data.get("address", {})

        return (

            address.get("city")

            or address.get("town")

            or address.get("village")

            or address.get("county")

            or address.get("state")

            or "Unknown"

        )

    except:

        return "Unknown"

# ==========================================================
# SEARCH CITY
# ==========================================================

def search_city(city):

    try:

        url = (

            "https://nominatim.openstreetmap.org/search"

            f"?q={city}"

            "&format=json"

            "&limit=5"

            "&addressdetails=1"

        )

        response = requests.get(

            url,

            headers={

                "User-Agent":"E2FIX"

            },

            timeout=10

        )

        return response.json()

    except:

        return []

# ==========================================================
# INTERACTIVE MAP
# ==========================================================

def map_selector():

    m = folium.Map(

        location=[28.6139,77.2090],

        zoom_start=5,

        control_scale=True

    )

    return st_folium(

        m,

        height=500,

        use_container_width=True

    )

# ==========================================================
# LOCATION SELECTOR
# ==========================================================

def select_location():

    st.subheader("📍 Select Location")

    mode = st.radio(

        "",

        [

            "🗺 Interactive Map",

            "🏙 Search City"

        ],

        horizontal=True

    )

    latitude = None
    longitude = None
    location_name = None

    if mode == "🗺 Interactive Map":

        map_data = map_selector()

        if map_data:

            if map_data.get("last_clicked"):

                latitude = map_data["last_clicked"]["lat"]

                longitude = map_data["last_clicked"]["lng"]

                location_name = reverse_geocode(

                    latitude,

                    longitude

                )

    else:

        city = st.text_input(

            "Enter City Name"

        )

        if city:

            cities = search_city(city)

            if cities:

                options = [

                    c["display_name"]

                    for c in cities

                ]

                selected = st.selectbox(

                    "Select Location",

                    options

                )

                if selected:

                    selected_city = next(

                        x

                        for x in cities

                        if x["display_name"] == selected

                    )

                    latitude = float(

                        selected_city["lat"]

                    )

                    longitude = float(

                        selected_city["lon"]

                    )

                    location_name = selected

    if location_name:

        st.success(

            f"📍 {location_name}"

        )

        c1,c2 = st.columns(2)

        c1.metric(

            "Latitude",

            round(latitude,4)

        )

        c2.metric(

            "Longitude",

            round(longitude,4)

        )

    return {

        "latitude": latitude,

        "longitude": longitude,

        "location": location_name

    }

