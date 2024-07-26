"""
XINYI WANG
CS 5001, Fall 2023
Function for Page product_page
"""
import streamlit as st
from models.product import Product

def filter_products_by_rating_and_category(products, rating_option, category):
    """Filter products by rating and category."""
    filtered_products = []

    # Filter by rating
    for product in products:
        if rating_option != 'All':
            rating_threshold = float(rating_option.split(' ')[1])
            if ('Below' in rating_option and product['rating']['rate'] < rating_threshold) or \
               ('Below' not in rating_option and product['rating']['rate'] >= rating_threshold):
                filtered_products.append(product)
        else:
            filtered_products.append(product)

    if category != 'All':
        filtered_products = [product for product in filtered_products if product['category'] == category]
    
    return filtered_products

# Page content
def show_products_page():
    product_model = Product()
    product_model.fetch_products()
    product_model.fetch_categories()

    # User selects rating and category
    rating = st.selectbox('Select rating:', ['All', 'Above 4.0', 'Above 3.5', 'Above 3.0', 'Above 2.5', 'Below 2.5'])
    category = st.selectbox('Select a category:', ['All'] + product_model.categories)

    # Apply filters
    filtered_products = filter_products_by_rating_and_category(product_model.products, rating, category)

    # Display products
    if filtered_products:
        for product in filtered_products:
            st.subheader(product['title'])
            st.write(f"Category: {product['category']}")
            st.write(f"Rating: {product['rating']['rate']}")
            st.write(f"Price: ${product['price']}")
            st.write(product['description'])
            st.image(product['image'], width=200)
            st.write("---")  # Separator line between products
    else:
        st.error('No products to display for the selected criteria.')

def main():
    """
    Main function 
    It calls the function to display the product page.
    """
    st.title("E-Commerce Product Viewer")
    st.write("Welcome to the interactive product viewing platform. Select filters to view different products.")
    show_products_page()

if __name__ == '__main__':
    main()

