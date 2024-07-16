from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
import json

#  import the data models
from dataModels import Address, Cart, Category, Catalog, Checkout, Customer, Dimension, Manufacturer, Payment

load_dotenv()

# This part of the code is establishing a connection to a MongoDB database using the `pymongo` library
# in Python.
client  = MongoClient(
    os.getenv("MONGO_URI"),
    server_api = ServerApi("1")
)

try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except Exception as e:
    print("Connection error: ", e)

db = client.test

#  collection defs 

addressCollection = db.addresses
cartCollection = db.carts
categoryCollection = db.categories
customerCollection = db.customers
catalogCollection = db.catlogs
checkoutCollection = db.checkouts
dimensionCollection = db.dimensions
loginAccessCollection = db.loginaccesses
manufacturerCollection = db.manufacturers
paymentCollection = db.payments
shippingCollection = db.shippings


def fetchAll():
    addressData = addressCollection.find()
    cartData = cartCollection.find()
    categoryData = categoryCollection.find()
    customerData = customerCollection.find()
    catalogData = catalogCollection.find()
    checkoutData = checkoutCollection.find()
    dimensionData = dimensionCollection.find()
    manufacturerData = manufacturerCollection.find()
    paymentData = paymentCollection.find()
    shippingData = shippingCollection.find()

    addresses = []
    carts = []
    categories = []
    customers = []
    catalogs = []
    checkouts = []
    dimensions = []
    manufacturers = []
    payments = []
    shippings = []

    for address in addressData:
        addresses.append(address)

    for cart in cartData:
        carts.append(cart)

    for category in categoryData:
        categories.append(category)
    
    for customer in customerData:
        customers.append(customer)
    
    for catalog in catalogData:
        catalogs.append(catalog)
    
    for checkout in checkoutData:
        checkouts.append(checkout)
    
    for dimension in dimensionData:
        dimensions.append(dimension)
    
    for manufacturer in manufacturerData:
        manufacturers.append(manufacturer)
    
    for payment in paymentData:
        payments.append(payment)
    
    for shipping in shippingData:
        shippings.append(shipping)



# The code snippet you provided is creating pandas DataFrames from the lists of data fetched from
# different MongoDB collections. Each list contains documents retrieved from a specific collection in
# the database.
    addressDF = pd.DataFrame(addresses)
    cartDF = pd.DataFrame(carts)
    categoryDF = pd.DataFrame(categories)
    customerDF = pd.DataFrame(customers)
    catalogDF = pd.DataFrame(catalogs)
    checkoutDF = pd.DataFrame(checkouts)
    dimensionDF = pd.DataFrame(dimensions)
    manufacturerDF = pd.DataFrame(manufacturers)
    paymentDF = pd.DataFrame(payments)


    return addressDF, cartDF, categoryDF, customerDF, catalogDF, checkoutDF, dimensionDF, manufacturerDF, paymentDF

