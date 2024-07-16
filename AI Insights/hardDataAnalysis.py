import pandas as pd
import numpy as np


# Example functions for data analysis

def analyze_address_data(df_address):
    # Count by State
    state_counts = df_address['State'].value_counts()
    
    # Average length of Line1
    df_address['Line1_Length'] = df_address['Line1'].apply(len)
    avg_line1_length = df_address['Line1_Length'].mean()
    
    return {
        'State_Counts': state_counts,
        'Average_Line1_Length': avg_line1_length
    }

def analyze_cart_data(df_cart):
    # Total sub-total by User_id
    total_subtotal_by_user = df_cart.groupby('User_id')['sub_total'].sum()
    
    return {
        'Total_Subtotal_by_User': total_subtotal_by_user
    }

def analyze_category_data(df_category):
    # Count by Name
    category_counts = df_category['Name'].value_counts()
    
    return {
        'Category_Counts': category_counts
    }

def analyze_catalog_data(df_catalog):
    # Average price by Category_id
    avg_price_by_category = df_catalog.groupby('Category_id')['price'].mean()
    
    return {
        'Average_Price_by_Category': avg_price_by_category
    }

def analyze_checkout_data(df_checkout):
    # Calculate average Total_Paid
    avg_total_paid = df_checkout['Total_Paid'].mean()
    
    return {
        'Average_Total_Paid': avg_total_paid
    }

def analyze_customer_data(df_customer):
    df_customer['age'] = pd.to_numeric(df_customer['age'], errors='coerce')
    
    df_customer = df_customer.dropna(subset=['age'])
    
    age_distribution = df_customer['age'].value_counts().sort_index()
    
    return {
        'Age_Distribution': age_distribution
    }

def analyze_dimension_data(df_dimension):
    # Calculate volume (Length * Breadth * Height)
    df_dimension['Volume'] = df_dimension['Length'] * df_dimension['Breadth'] * df_dimension['Height']
    avg_volume = df_dimension['Volume'].mean()
    
    return {
        'Average_Volume': avg_volume
    }

def analyze_manufacturer_data(df_manufacturer):
    # Count by Location
    location_counts = df_manufacturer['Location'].value_counts()
    
    return {
        'Location_Counts': location_counts
    }

def analyze_payment_data(df_payment):

    df_payment['Amount'] = pd.to_numeric(df_payment['Amount'], errors='coerce')
    

    df_payment = df_payment.dropna(subset=['Amount'])
    

    total_amount_by_method = df_payment.groupby('Method_Payment')['Amount'].sum()
    
    return {
        'Total_Amount_by_Method_Payment': total_amount_by_method
    }


"""
The above functions are designed to analyze different aspects of data related to addresses, carts,
categories, catalogs, checkouts, customers, dimensions, manufacturers, and payments.

:param df_address: The `df_address` parameter represents a DataFrame containing address data with
columns like 'State' and 'Line1'. The `analyze_address_data` function processes this DataFrame to
provide insights such as the count of addresses by state and the average length of the 'Line1'
column. If you have a
:return: The functions are returning dictionaries containing the results of the data analysis
operations. Each dictionary contains specific key-value pairs based on the analysis performed in the
respective functions. Here are the keys for each function:
"""