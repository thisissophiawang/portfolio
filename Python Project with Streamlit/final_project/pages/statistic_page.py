"""
XINYI WANG
CS 5001, Fall 2023
Function for Page statistic_page
"""
import streamlit as st
import pandas as pd
import altair as alt
from models.product import Product

def statistic_product():
    """
    function for the statistic page
    """
    product_model= Product()
    product_model.fetch_products()
    product_model.fetch_categories()

    #convert the list of products to a Pandas DataFrame
    product_df = pd.DataFrame(product_model.products)
    product_df['rating_value'] = product_df['rating'].apply(lambda x: x['rate'])


    # Create an Altair chart(Scatter Plot)
    #Citation: https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    chart = (
        alt.Chart(product_df)
        .mark_circle()
        .encode(
        y=alt.Y('category', axis=alt.Axis(title='Category', labels=True)),
        x=alt.X('rating_value', axis=alt.Axis(title='Rating')),
        tooltip=['title', 'rating_value']
    )
)
    #Normaluze the data for the parallel coordinates plot
    product_df['normalized_price']=product_df['price']/product_df['price'].max()
    product_df['normalized_rating']=product_df['rating_value']/product_df['rating_value'].max()

    # Create an Altair chart(Parallel Coordinates Plot)
    #Citation: https://altair-viz.github.io/gallery/normed_parallel_coordinates.html
    parallel_coordinates = (
        alt.Chart(product_df)
        .mark_line()
        .encode(
        x=alt.X('normalized_price:Q', title='Price'),
        y=alt.Y('normalized_rating:Q', title='Rating'),
        color='category:N',
        tooltip=['title', 'rating_value']
    )
)
    


    # Display the chart using Altair & title
    st.title("Statistic of  Product")
    st.write("")
    st.subheader("Horizontal Scatter Plot using Product's Rating & Category")
    st.write("")
    st.altair_chart(chart, use_container_width=True)       # Display the DataFrame

    #additional text
    st.write("🔎 Remark: The data is fetched from the Fake Store API.")
    st.write("The horizontal scatter plot efficiently summarizes product ratings across different categories, providing a clear visual representation of customer satisfaction. Each dot corresponds to a product's rating within its category, allowing for immediate identification of high-performing areas as well as those needing improvement. This analytical tool aids businesses in understanding the breadth of customer feedback, highlighting both the range and concentration of ratings, which is crucial for informed decision-making regarding product offerings and quality enhancements.")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("Parallel Coordinates Plot using Product's Price and Rating")
    st.write("")
    st.altair_chart(parallel_coordinates, use_container_width=True)   # Display the Parallel Coordinates Plot
    st.write("The Parallel Coordinates Plot deftly maps out an array of product categories, with each category delineated by a distinct line traversing through the normalized price and rating axes. This method of data representation—where the price values are scaled between 0 and 1—facilitates a direct and equitable comparison across diverse price ranges. Intriguingly, the plot underscores a certain dissociation between price and customer satisfaction, as seen in the consistent ratings across varied price points, particularly in the electronics and jewelry sectors. Moreover, the emergence of clusters where higher ratings align with specific price levels could be indicative of an optimal pricing model that maximizes consumer contentment.")
    st.write("This page is an integral part of my project, and I extend my gratitude to Altair-viz for providing coding and analytical reference support. [Gallery Available](https://altair-viz.github.io/gallery/index.html#example-gallery).")

def main():
    """
    Main function
    It calls the function to display the statistic page.
    """
    statistic_product()


if __name__ == '__main__':
    main()

