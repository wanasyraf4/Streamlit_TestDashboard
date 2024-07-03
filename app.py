import streamlit as st
from backend import load_data, split_func

# Load data using the backend function
df = load_data('Test_info.csv')

# Streamlit user interface for item selection
st.title('Order Packaging System')
st.write('Please select items for the order:')
selected_indices = []
for index, row in df.iterrows():
    if st.checkbox(f"{row['Name']} - ${row['Price ($)']} - {row['Weight (g)']}g", key=index):
        selected_indices.append(index)

if st.button('Place order'):
    selected_df = df.iloc[selected_indices]
    packages = split_func(selected_df)
    
    st.write('This order has following packages:')
    for i, package in enumerate(packages, start=1):
        st.write(f"Package {i}")
        st.write(f"Items - {', '.join(package['items'])}")
        st.write(f"Total weight - {package['total_weight']}g")
        st.write(f"Total price - ${package['total_price']}")
    st.write(f"Courier price - $15")  # Assuming a static courier price for simplicity

