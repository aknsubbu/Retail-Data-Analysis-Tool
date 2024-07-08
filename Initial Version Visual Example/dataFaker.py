from faker import Faker
from datetime import datetime
import random

# Create Faker instance
fake = Faker()

# List of tags
tag_list = ['electronics', 'fashion', 'food', 'travel', 'health']

def generate_fake_data():
    common_user_id = fake.uuid4()
    common_item_id = fake.uuid4()

    # Generate fake data for each schema
    cart_data = {
        'Cart_id': fake.uuid4(),
        'User_id': str(common_user_id),
        'Item_id': str(common_item_id),
        'Quantity': random.randint(1, 10),
        'Added_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Updated_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Deleted_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Active': fake.boolean(),
        'sub_total': random.uniform(10.0, 100.0)
    }

    catalog_data = {
        'item_id': str(common_item_id),
        'item_name': fake.word(),
        'price': random.uniform(10.0, 100.0),
        'manufacturer_id': str(fake.uuid4()),
        'Category_id': str(fake.uuid4()),
        'Quantity': random.randint(1, 100),
        'Added_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Updated_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Deleted_data': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Discount': random.uniform(0.0, 50.0),
        'Description': fake.text(),
        'Weight': random.uniform(0.1, 10.0),
        'Dimension_id': str(fake.uuid4()),
        'image_url': fake.image_url(),
        'Rating': [random.randint(1, 5) for _ in range(5)],
        'Reviews': [fake.paragraph() for _ in range(3)],
        'Tags': random.sample(tag_list, random.randint(1, len(tag_list)))  # Pick random tags from the list
    }

    checkout_data = {
        'User_ID': str(common_user_id),
        'Cart_ID': str(fake.uuid4()),
        'Payment_ID': str(fake.uuid4()),
        'Added_date': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Shipping_ID': str(fake.uuid4()),
        'Shipping_Cost': random.uniform(5.0, 20.0),
        'Total_Paid': random.uniform(50.0, 200.0),
        'Complete': fake.boolean()
    }

    customer_data = {
        'name': fake.name(),
        'age': random.randint(18, 80),
        'phone_number': fake.phone_number(),
        'email': fake.email(),
        'gender': fake.random_element(elements=('Male', 'Female')),
        'date_of_birth': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'account_creation_date': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'address_id': str(fake.uuid4()),
        'total_purchase_cost': random.uniform(100.0, 1000.0)
    }

    login_access_data = {
        'Login_id': str(fake.uuid4()),
        'User_id': str(common_user_id),
        'Login_time': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Logout_time': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'IP_address': fake.ipv4(),
        'Device_type': fake.user_agent()
    }

    address_data = {
        'Address_ID': str(fake.uuid4()),
        'Line1': fake.street_address(),
        'Line2': fake.secondary_address(),
        'City': fake.city(),
        'State': fake.state(),
        'Country': fake.country(),
        'PinCode': fake.zipcode()
    }

    manufacturer_data = {
        'Manufacturer_ID': str(fake.uuid4()),
        'Manufacturer_Name': fake.company(),
        'Location': fake.country(),
        'GSTIN': fake.ean8()
    }

    category_data = {
        'Category_ID': str(fake.uuid4()),
        'Name': fake.word()
    }

    dimension_data = {
        'Dimension_ID': str(fake.uuid4()),
        'Length': random.uniform(10.0, 100.0),
        'Breadth': random.uniform(10.0, 100.0),
        'Height': random.uniform(10.0, 100.0)
    }

    payment_data = {
        'User_ID': str(common_user_id),
        'Amount': random.uniform(10.0, 100.0),
        'Method_Payment': fake.credit_card_provider(),
        'Date_of_txn': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Transaction_Status': fake.word(),
        'Payment_Status': fake.word(),
        'Confirmation_Number': fake.uuid4()
    }

    shipping_data = {
        'User_ID': str(common_user_id),
        'Amount': random.uniform(10.0, 100.0),
        'Method_Payment': fake.credit_card_provider(),
        'Date_of_txn': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'Transaction_Status': fake.word(),
        'Payment_Status': fake.word(),
        'Confirmation_Number': fake.uuid4()
    }

    return cart_data, catalog_data, checkout_data, customer_data, login_access_data, address_data, manufacturer_data, category_data, dimension_data, payment_data, shipping_data

# if __name__ == "__main__":
#     cart_record, catalog_record, checkout_record, customer_record, login_access_record, address_record, manufacturer_record, category_record, dimension_record, payment_record, shipping_record = generate_fake_data()
#     print("Records created successfully!")
#     print("cart_record: ", cart_record)
#     print("catalog_record: ", catalog_record)
#     print("checkout_record: ", checkout_record)
#     print("customer_record: ", customer_record)
#     print("login_access_record: ", login_access_record)
#     print("address_record: ", address_record)
#     print("manufacturer_record: ", manufacturer_record)
#     print("category_record: ", category_record)
#     print("dimension_record: ", dimension_record)
#     print("payment_record: ", payment_record)
#     print("shipping_record: ", shipping_record)
