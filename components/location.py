import streamlit as st
import folium
import requests

from streamlit_folium import st_folium


# ==========================================================
# REVERSE GEOCODING
# ==========================================================

def reverse_geocode(lat, lon):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"

        params = {
            "lat": lat,
            "lon": lon,
            "format": "jsonv2",
            "addressdetails": 1
        }

        headers = {
            "User-Agent": "E2FIX/1.0 (https://github.com/vrprateek18/E2FIX)"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        st.write(response.status_code)
        st.write(response.text)

        response.raise_for_status()

        data = response.json()

        address = data.get("address", {})

        location = (
            address.get("city")
            or address.get("town")
            or address.get("village")
            or address.get("municipality")
            or address.get("suburb")
            or address.get("county")
            or address.get("state_district")
            or address.get("state")
        )

        if location:
            return location

        # Final fallback
        display_name = data.get("display_name")

        if display_name:
            return display_name.split(",")[0]

        return "Unknown"

    except Exception as e:
        print("Reverse Geocode Error:", e)
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

