import pandas as pd
import numpy as np


# Example functions for data analysis

def analyze_address_data(df_address):
    # Count by State
    state_counts = df_address['State'].value_counts()
    
    # Average length of Line1
    df_address['Line1_Length'] = df_address['Line1'].apply(len)
    avg_line1_length = df_address['Line1_Length'].mean()
    
    return pd.DataFrame({
        'State_Counts': state_counts,
        'Average_Line1_Length': avg_line1_length
    })

def analyze_cart_data(df_cart):
    # Total sub-total by User_id
    total_subtotal_by_user = df_cart.groupby('User_id')['sub_total'].sum()
    
    return pd.DataFrame({
        'Total_Subtotal_by_User': total_subtotal_by_user
    })

def analyze_category_data(df_category):
    # Count by Name
    category_counts = df_category['Name'].value_counts()
    
    return pd.DataFrame({
        'Category_Counts': category_counts
    })

def analyze_catalog_data(df_catalog):
    # Average price by Category_id
    avg_price_by_category = df_catalog.groupby('Category_id')['price'].mean()
    
    return pd.DataFrame({
        'Average_Price_by_Category': avg_price_by_category
    })

def analyze_checkout_data(df_checkout):
    # Calculate average Total_Paid
    avg_total_paid = df_checkout['Total_Paid'].mean()
    
    return pd.DataFrame({
        'Average_Total_Paid': avg_total_paid
    })

def analyze_customer_data(df_customer):
    df_customer['age'] = pd.to_numeric(df_customer['age'], errors='coerce')
    
    df_customer = df_customer.dropna(subset=['age'])
    
    age_distribution = df_customer['age'].value_counts().sort_index()
    
    return pd.DataFrame({
        'Age_Distribution': age_distribution
    })

def analyze_dimension_data(df_dimension):
    # Calculate volume (Length * Breadth * Height)
    df_dimension['Volume'] = df_dimension['Length'] * df_dimension['Breadth'] * df_dimension['Height']
    avg_volume = df_dimension['Volume'].mean()
    
    return pd.DataFrame({
        'Average_Volume': avg_volume
    })

def analyze_manufacturer_data(df_manufacturer):
    # Count by Location
    location_counts = df_manufacturer['Location'].value_counts()
    
    return pd.DataFrame({
        'Location_Counts': location_counts
    })

def analyze_payment_data(df_payment):

    df_payment['Amount'] = pd.to_numeric(df_payment['Amount'], errors='coerce')
    

    df_payment = df_payment.dropna(subset=['Amount'])
    

    total_amount_by_method = df_payment.groupby('Method_Payment')['Amount'].sum()
    
    return pd.DataFrame({
        'Total_Amount_by_Method_Payment': total_amount_by_method
    })

# cross attribute analysis functions -- mathematical

def calculate_aov(df_checkout: pd.DataFrame) -> pd.DataFrame:
    total_paid = df_checkout['Total_Paid'].sum()
    number_of_orders = df_checkout.shape[0]
    aov = pd.DataFrame({'Average_Order_Value': [total_paid / number_of_orders]})
    return aov

def calculate_conversion_rate(df_cart: pd.DataFrame, df_checkout: pd.DataFrame) -> pd.DataFrame:
    number_of_carts = df_cart.shape[0]
    number_of_completed_checkouts = df_checkout.shape[0]
    conversion_rate = pd.DataFrame({'Conversion_Rate': [(number_of_completed_checkouts / number_of_carts) * 100]})
    return conversion_rate

def calculate_cart_abandonment_rate(df_cart: pd.DataFrame, df_checkout: pd.DataFrame) -> pd.DataFrame:
    number_of_carts = df_cart.shape[0]
    number_of_completed_checkouts = df_checkout.shape[0]
    abandonment_rate = pd.DataFrame({'Cart_Abandonment_Rate': [((number_of_carts - number_of_completed_checkouts) / number_of_carts) * 100]})
    return abandonment_rate

def calculate_category_performance(df_catalog: pd.DataFrame, df_checkout: pd.DataFrame) -> pd.DataFrame:
    df_checkout = df_checkout.merge(df_catalog[['item_id', 'Category_id']], left_on='Cart_ID', right_on='item_id')
    sales_by_category = df_checkout.groupby('Category_id')['Total_Paid'].sum().reset_index()
    sales_by_category.columns = ['Category_ID', 'Total_Sales']
    return sales_by_category

def calculate_average_discount(df_catalog: pd.DataFrame) -> pd.DataFrame:
    df_catalog['Discount'] = pd.to_numeric(df_catalog['Discount'], errors='coerce')
    avg_discount = pd.DataFrame({'Average_Discount': [df_catalog['Discount'].mean()]})
    return avg_discount

def calculate_clv(df_checkout: pd.DataFrame, df_customer: pd.DataFrame) -> pd.DataFrame:
    total_purchase_value = df_checkout.groupby('User_ID')['Total_Paid'].sum()
    number_of_purchases = df_checkout.groupby('User_ID').size()
    customer_lifespan = pd.to_datetime('today') - pd.to_datetime(df_customer['account_creation_date'])
    avg_purchase_value = total_purchase_value.mean()
    clv = pd.DataFrame({'Customer_Lifetime_Value': [avg_purchase_value * number_of_purchases.mean() * customer_lifespan.mean().days / 365]})
    return clv

def calculate_repeat_purchase_rate(df_checkout: pd.DataFrame) -> pd.DataFrame:
    repeat_customers = df_checkout.groupby('User_ID').size()
    repeat_purchase_rate = pd.DataFrame({'Repeat_Purchase_Rate': [(repeat_customers[repeat_customers > 1].count() / df_checkout['User_ID'].nunique()) * 100]})
    return repeat_purchase_rate

def calculate_average_age(df_customer: pd.DataFrame) -> pd.DataFrame:
    avg_age = pd.DataFrame({'Average_Age': [df_customer['age'].mean()]})
    return avg_age

def calculate_inventory_turnover_ratio(df_catalog: pd.DataFrame) -> pd.DataFrame:
    cost_of_goods_sold = df_catalog['price'].sum()  # Placeholder, replace with actual COGS
    average_inventory = df_catalog['Quantity'].mean()  # Placeholder, replace with actual average inventory
    turnover_ratio = pd.DataFrame({'Inventory_Turnover_Ratio': [cost_of_goods_sold / average_inventory]})
    return turnover_ratio

def calculate_product_return_rate(df_checkout: pd.DataFrame) -> pd.DataFrame:
    total_items_sold = df_checkout.shape[0]  # Placeholder for actual number of items sold
    returned_items = df_checkout[df_checkout['Complete'] == False].shape[0]  # Placeholder for returned items
    return_rate = pd.DataFrame({'Product_Return_Rate': [(returned_items / total_items_sold) * 100]})
    return return_rate

def calculate_rsi(df_checkout: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    df_checkout['Change'] = df_checkout['Total_Paid'].diff()
    df_checkout['Gain'] = df_checkout['Change'].apply(lambda x: x if x > 0 else 0)
    df_checkout['Loss'] = df_checkout['Change'].apply(lambda x: -x if x < 0 else 0)
    avg_gain = df_checkout['Gain'].rolling(window=period).mean()
    avg_loss = df_checkout['Loss'].rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = pd.DataFrame({'RSI': [100 - (100 / (1 + rs.iloc[-1]))]})
    return rsi

def calculate_moving_average(df: pd.DataFrame, column: str, window: int) -> pd.DataFrame:
    df[f'Moving_Avg_{window}'] = df[column].rolling(window=window).mean()
    return df[[f'Moving_Avg_{window}']]

def calculate_sales_by_state(df_checkout: pd.DataFrame, df_address: pd.DataFrame) -> pd.DataFrame:
    df_checkout = df_checkout.merge(df_address[['Address_ID', 'State']], left_on='Cart_ID', right_on='Address_ID')
    sales_by_state = df_checkout.groupby('State')['Total_Paid'].sum().reset_index()
    sales_by_state.columns = ['State', 'Total_Sales']
    return sales_by_state

def calculate_population_density(df_customer: pd.DataFrame) -> pd.DataFrame:
    population_density = df_customer['City'].value_counts().reset_index()
    population_density.columns = ['City', 'Population_Count']
    return population_density




"""
The above functions provide various data analysis and calculation operations on different datasets
related to e-commerce, such as analyzing address data, cart data, category data, checkout data,
customer data, dimension data, manufacturer data, payment data, and performing cross-attribute
mathematical analysis.

:param df_address: The `df_address` parameter refers to a DataFrame containing address data. This
data could include information such as street addresses, cities, states, postal codes, etc., for
customers or locations. The functions provided in the code snippet are designed to analyze different
aspects of the address data, such as counting by
:return: The functions provided in the code return various data analysis results based on the input
dataframes. Here is a summary of what each function returns:
"""