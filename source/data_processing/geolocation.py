from geopy.geocoders import Nominatim
import pandas as pd
import time

def geocode_single_address(address):
    if not address:
        return None, None
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    # Wait 1 second before returning the result
    time.sleep(1.5)
    return (location.latitude, location.longitude) if location else (None, None)

def geocode_addresses(df, address_column):
    df['Coords'] = df[address_column].apply(lambda x: geocode_single_address(x))
    df['Latitude'] = df['Coords'].apply(lambda x: x[0])
    df['Longitude'] = df['Coords'].apply(lambda x: x[1])
    return df


