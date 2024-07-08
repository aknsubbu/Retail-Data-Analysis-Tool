from pydantic import BaseModel,Field
from typing import Optional

class Address(BaseModel):
    _id: dict
    Address_ID: str
    Line1: str
    Line2: Optional[str]
    City: str
    State: str
    Country: str
    PinCode: str
    __v: int

class Cart(BaseModel):
    _id: str
    Cart_id: str
    User_id: str
    Item_id: str
    Quantity: int
    Added_date: str
    Updated_date: str
    Deleted_date: Optional[str]
    Active: int
    sub_total: int

class Category(BaseModel):
    _id: str
    Category_ID: str
    Name: str
    __v: int

class Catalog(BaseModel):
    _id: str
    item_id: str
    item_name: str
    price: int
    manufacturer_id: str
    Category_id: str
    Quantity: int
    Added_data: str
    Updated_data: str
    Deleted_data: Optional[str]
    Discount: str
    Description: str
    Weight: str
    Dimension_id: str
    image_url: str
    Rating: int
    Reviews: int
    Tags: str

class Checkout(BaseModel):
    id: str
    User_ID: str
    Cart_ID: str
    Payment_ID: str
    Added_date: str
    Shipping_ID: str
    Shipping_Cost: float
    Total_Paid: float
    Complete: bool
    __v: int

class Customer(BaseModel):
    _id: str
    name: str
    age: int
    phone_number: str
    email: str
    gender: str
    date_of_birth: str
    account_creation_date: str
    address_id: str
    total_purchase_cost: float

class Dimension(BaseModel):
    _id: str
    Dimension_ID: str
    Length: float
    Breadth: float
    Height: float
    __v: int

class Manufacturer(BaseModel):
    _id: str
    Manufacturer_ID: str
    Manufacturer_Name: str
    Location: str
    GSTIN: str
    __v: int

class Payment(BaseModel):
    _id: str
    User_ID: str
    Amount: int
    Method_Payment: str
    Date_of_txn: str
    Transaction_Status: str
    Payment_Status: int
    Confirmation_Number: str

