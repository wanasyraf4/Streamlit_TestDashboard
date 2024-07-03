import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df = df.drop([0, 1])
    df = df[['Products', 'Unnamed: 1', 'Unnamed: 2']]
    df.reset_index(drop=True, inplace=True)
    df.columns = ['Name', 'Price ($)', 'Weight (g)']
    return df

def calculate_courier_charge(weight):
    if weight <= 200:
        return 5
    elif weight <= 500:
        return 10
    elif weight <= 1000:
        return 15
    else:
        return 20

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
        for item in remaining_items[:]:
            item_name, item_price, item_weight = item
            if current_package_cost + item_price < 250:
                current_package.append(item_name)
                current_package_cost += item_price
                current_package_weight += item_weight
                remaining_items.remove(item)
        if current_package:
            courier_charge = calculate_courier_charge(current_package_weight)
            packages.append({
                'items': current_package,
                'total_price': current_package_cost,
                'total_weight': current_package_weight,
                'courier_price': courier_charge
            })
    return packages
