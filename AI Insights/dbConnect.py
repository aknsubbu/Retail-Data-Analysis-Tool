from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
import json

#  import the data models
from .dataModels import Address, Cart, Category, Catalog, Checkout, Customer, Dimension, Manufacturer, Payment

load_dotenv()

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
catalogCollection = db.catalogs
checkoutCollection = db.checkouts
dimensionCollection = db.dimensions
loginAccessCollection = db.loginaccesses
manufacturerCollection = db.manufacturers
paymentCollection = db.payments
shippingCollection = db.shippings

