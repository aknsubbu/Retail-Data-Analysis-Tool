import requests 

from dataFaker import generate_fake_data

base_url= 'https://dbms-ap.onrender.com/api'

endpoints = [
    "/dimension",
    "/manufacturer",
    "/category",
    "/customer",
    "/login-access",
    "/address",
    "/catlog",
    "/payment",
    "/cart",
    "/checkout",
    "/shipping",
]

numRecords =1

for i in range(numRecords):
    customer_data, catlog_data, checkout_data, customer_data, login_access_data, address_data, manufacturer_data, category_data, dimension_data, payment_data, shipping_data = generate_fake_data()

    response = requests.post(base_url + endpoints[0], json=dimension_data)
    response = requests.post(base_url + endpoints[1], json=manufacturer_data)
    response = requests.post(base_url + endpoints[2], json=category_data)
    response = requests.post(base_url + endpoints[3], json=customer_data)
    response = requests.post(base_url + endpoints[4], json=login_access_data)
    response = requests.post(base_url + endpoints[5], json=address_data)
    response = requests.post(base_url + endpoints[6], json=catlog_data)
    response = requests.post(base_url + endpoints[7], json=payment_data)
    response = requests.post(base_url + endpoints[9], json=checkout_data)
    response = requests.post(base_url + endpoints[10], json=shipping_data)


    # response = requests.post(url, json=customer_data)
    # response = requests.post(url, json=catlog_data)
    # response = requests.post(url, json=checkout_data)
    # response = requests.post(url, json=customer_data)
    # response = requests.post(url, json=login_access_data)
    # response = requests.post(url, json=address_data)
    # response = requests.post(url, json=manufacturer_data)
    # response = requests.post(url, json=category_data)
    # response = requests.post(url, json=dimension_data)
    # response = requests.post(url, json=payment_data)
    # response = requests.post(url, json=shipping_data)
    if response.status_code == 200:
        print(f"Successfully added data to ")
    else:
        print(f"Failed to add data to")