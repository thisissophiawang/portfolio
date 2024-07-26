"""
XINYI WANG
CS 5001, Fall 2023
Function for Page user_page
"""
import streamlit as st
from models.users import Users
import pandas as pd

def show_user_map_and_locations():
    users_model = Users()
    users_model.fetch_users()

    # Display the map with user locations
    # citation: https://docs.streamlit.io/library/api-reference/charts/st.map
    if users_model.users:
        # Create a DataFrame with the correct column names for Streamlit's map
        df = pd.DataFrame({
            'lat': [float(user['address']['geolocation']['lat']) for user in users_model.users],
            'lon': [float(user['address']['geolocation']['long']) for user in users_model.users],
            'Customers': [f"{user['name']['firstname']} {user['name']['lastname']}" for user in users_model.users],
            'City': [user['address']['city'].upper() for user in users_model.users]
        })

         # Header for the map
        st.header("📍 Customer Location Map")

        # explain the location inaccuracy
        st.markdown(":warning: Customer's geolocation is created by the Fakestore API, resulting in inaccuracies in location. ")

        # Display the map with user locations
        st.map(df[['lat', 'lon']])  # Pass only latitude and longitude to st.map

        # Display the DataFrame with user details
        st.write("")
        st.markdown(" 🏠 Customers Details:")
        st.write("")
        st.markdown(" The table will showcase details of customers, including their latitude, longitude, full names, and the cities of their locations.")
        st.dataframe(df)
    else:
        st.error("No user data available to display.")


def main():
        '''
        Main function of the user page
        '''
        show_user_map_and_locations()


if __name__ == '__main__':
    main()





