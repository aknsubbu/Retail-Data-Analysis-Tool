import requests
import pandas as pd


def get_data():
    # Define base URL for your API
    base_url = "https://dbms-ap.onrender.com/api"  

    # Define a dictionary to store data from each route
    data_dict = {}

    # Define a list of endpoints to fetch data from
    endpoints = [
        "/dimensions",
        "/manufacturers",
        "/categories",
        "/customers",
        "/login-accesses",
        "/addresses",
        "/catlogs",
        "/payments",
        "/carts",
        "/checkouts",
        "/shippings",
        "/items",


    ]

    # Loop through each endpoint and fetch data
    for endpoint in endpoints:
        url = base_url + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            # Assuming the response contains JSON data
            df= pd.DataFrame(response.json())
            data_dict[endpoint.replace("/", "")] = df
            print(response.json())
        else:
            print(f"Failed to fetch data from {url}")

       

    return data_dict


