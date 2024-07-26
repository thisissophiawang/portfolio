import streamlit as st
from models.product import Product
from streamlit_option_menu import option_menu
#streamlit run app.py


# Sider Bar
#with st.sidebar:
    #selected = option_menu(
        #menu_title="Main Menu",
        #options=["Home", "Product","Search","Statistic","Contact"],
        #icons=["🏠","📦","🔍","📊","📞"],
   # )

# Text/ Title
st.title(' Decoding E-Commerce Insights 🛍️')

# header/ subheader
st.subheader('''
    :red[A] :orange[data-driven] :green[approach] :blue[to] :violet[understanding] :gray[the] :rainbow[e-commerce] :rainbow[industry].''')

# Text
st.write("")

st.write('''Crafted with Care by Sophia Wang''')
st.markdown('[Learn More About Me >](https://www.linkedin.com/in/xinyiwangsophia/)')
st.markdown('[Discover Data API Details >](https://fakestoreapi.com/)')
st.write("")

# insert image
# URL of the online image
image_url = 'https://images.unsplash.com/photo-1528698827591-e19ccd7bc23d?q=80&w=2076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
# Display the image
st.image(image_url, caption='Credit: Unsplash', use_column_width=True)


