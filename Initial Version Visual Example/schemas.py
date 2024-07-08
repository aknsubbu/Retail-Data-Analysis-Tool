from mongoengine import Document, StringField, DateTimeField, BooleanField, FloatField, ListField, ReferenceField

class Cart(Document):
    Cart_id = StringField(required=True)
    User_id = StringField(required=True)
    Item_id = StringField(required=True)
    Quantity = FloatField(required=True)
    Added_data = DateTimeField(required=True)
    Updated_data = DateTimeField(required=True)
    Deleted_data = DateTimeField(required=True)
    Active = BooleanField(required=True)
    sub_total = FloatField(required=True)

class Catlog(Document):
    item_id = StringField(required=True)
    item_name = StringField(required=True)
    price = FloatField(required=True)
    manufacturer_id = StringField(required=True)
    Category_id = StringField(required=True)
    Quantity = FloatField(required=True)
    Added_data = DateTimeField(required=True)
    Updated_data = DateTimeField(required=True)
    Deleted_data = DateTimeField(required=True)
    Discount = FloatField(required=True)
    Description = StringField(required=True)
    Weight = FloatField(required=True)
    Dimension_id = StringField(required=True)
    image_url = StringField(required=True)
    Rating = ListField(FloatField(), required=True)
    Reviews = ListField(StringField(), required=True)
    Tags = ListField(StringField(), required=True)

class Checkout(Document):
    User_ID = StringField(required=True)
    Cart_ID = StringField()
    Payment_ID = StringField()
    Added_date = DateTimeField()
    Shipping_ID = StringField()
    Shipping_Cost = FloatField()
    Total_Paid = FloatField()
    Complete = BooleanField(default=False)

class Customer(Document):
    name = StringField(required=True)
    age = FloatField(required=True)
    phone_number = StringField(required=True)
    email = StringField(required=True)
    gender = StringField(required=True)
    date_of_birth = DateTimeField(required=True)
    account_creation_date = DateTimeField(required=True)
    address_id = StringField(required=True)
    total_purchase_cost = FloatField(required=True)

class LoginAccess(Document):
    Login_id = StringField(required=True)
    User_id = StringField(required=True)
    Login_time = DateTimeField(required=True)
    Logout_time = DateTimeField(required=True)
    IP_address = StringField(required=True)
    Device_type = StringField(required=True)

class Address(Document):
    Address_ID = StringField(required=True)
    Line1 = StringField(required=True)
    Line2 = StringField()
    City = StringField(required=True)
    State = StringField(required=True)
    Country = StringField(required=True)
    PinCode = StringField(required=True)

class Manufacturer(Document):
    Manufacturer_ID = StringField(required=True)
    Manufacturer_Name = StringField(required=True)
    Location = StringField(required=True)
    GSTIN = StringField(required=True)

class Category(Document):
    Category_ID = StringField(required=True)
    Name = StringField(required=True)

class Dimension(Document):
    Dimension_ID = StringField(required=True)
    Length = FloatField(required=True)
    Breadth = FloatField(required=True)
    Height = FloatField(required=True)

class Payment(Document):
    User_ID = StringField(required=True)
    Amount = FloatField(required=True)
    Method_Payment = StringField(required=True)
    Date_of_txn = DateTimeField(required=True)
    Transaction_Status = StringField(required=True)
    Payment_Status = StringField(required=True)
    Confirmation_Number = StringField(required=True)

class Shipping(Document):
    User_ID = StringField(required=True)
    Amount = FloatField(required=True)
    Method_Payment = StringField(required=True)
    Date_of_txn = DateTimeField(required=True)
    Transaction_Status = StringField(required=True)
    Payment_Status = StringField(required=True)
    Confirmation_Number = StringField(required=True)
