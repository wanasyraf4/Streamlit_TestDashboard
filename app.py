import streamlit as st
import pandas as pd

# Load and prepare the DataFrame
df = pd.read_csv('Test_info.csv')
df = df.drop([0, 1])
df = df[['Products','Unnamed: 1', 'Unnamed: 2']]
df.reset_index(drop=True, inplace=True)
df.columns = ['Name', 'Price ($)', 'Weight (g)']

# Function to split packages based on the logic provided earlier
def split_func(df):
    # Convert data types within the function
    df['Price ($)'] = pd.to_numeric(df['Price ($)'], errors='coerce')
    df['Weight (g)'] = pd.to_numeric(df['Weight (g)'], errors='coerce')

    # Convert DataFrame to a list of lists (array-like) for processing
    data = df.to_records(index=False).tolist()

    packages = []
    remaining_items = data

    # Sort items by price to optimize package configuration
    remaining_items.sort(key=lambda x: x[1], reverse=True)

    while remaining_items:
        current_package = []
        current_package_cost = 0
        current_package_weight = 0

        # Iterate over a copy of the list for safe modification during the loop
        for item in remaining_items[:]:
            item_name, item_price, item_weight = item

            # Ensure adding this item won't exceed the $250 price limit
            if current_package_cost + item_price < 250:
                current_package.append(item_name)
                current_package_cost += item_price
                current_package_weight += item_weight
                remaining_items.remove(item)

        # Store the package details
        if current_package:
            packages.append({
                'items': current_package,
                'total_price': current_package_cost,
                'total_weight': current_package_weight
            })

    return packages

# Streamlit user interface for item selection
st.title('Order Packaging System')
st.write('Please select items for the order:')
selected_indices = []
for index, row in df.iterrows():
    if st.checkbox(f"{row['Name']} - ${row['Price ($)']} - {row['Weight (g)']}g", key=index):
        selected_indices.append(index)

if st.button('Place order'):
    # Pass the selected DataFrame slice directly to the function
    selected_df = df.iloc[selected_indices]
    packages = split_func(selected_df)
    
    st.write('This order has following packages:')
    for i, package in enumerate(packages, start=1):
        st.write(f"Package {i}")
        st.write(f"Items - {', '.join(package['items'])}")
        st.write(f"Total weight - {package['total_weight']}g")
        st.write(f"Total price - ${package['total_price']}")
        st.write(f"Courier price - $15")  # Assuming a static courier price for simplicity

# To run this app, save this script as app.py and execute: streamlit run app.py
