import os 
import pandas as pd
from llama_index.core import StorageContext, VectorStoreIndex,load_index_from_storage,SimpleDirectoryReader
from llama_index.readers.file import CSVReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface_optimum import OptimumEmbedding

from dbConnect import fetchAll
from hardDataAnalysis import analyze_address_data, analyze_cart_data, analyze_category_data, analyze_catalog_data, analyze_checkout_data, analyze_customer_data, analyze_dimension_data, analyze_manufacturer_data, analyze_payment_data


#Load the data from the DB
addressDF, cartDF, categoryDF, customerDF, catalogDF, checkoutDF, dimensionDF, manufacturerDF, paymentDF = fetchAll() 
master_raw_df_assembler = {"Address":[addressDF], "Cart":[cartDF], "Category":[categoryDF], "Customer":[customerDF], "Catalog":[catalogDF], "Checkout":[checkoutDF], "Dimension":[dimensionDF], "Manufacturer":[manufacturerDF], "Payment":[paymentDF]}
master_raw_df = pd.DataFrame(master_raw_df_assembler)

addressAnalysed = analyze_address_data(addressDF)
cartAnalysed = analyze_cart_data(cartDF)
categoryAnalysed = analyze_category_data(categoryDF)
customerAnalysed = analyze_customer_data(customerDF)
catalogAnalysed = analyze_catalog_data(catalogDF)
checkoutAnalysed = analyze_checkout_data(checkoutDF)
dimensionAnalysed = analyze_dimension_data(dimensionDF)
manufacturerAnalysed = analyze_manufacturer_data(manufacturerDF)
paymentAnalysed = analyze_payment_data(paymentDF)

master_analysed_df_assembler = {"Adress":[addressAnalysed], "Cart":[cartAnalysed], "Category":[categoryAnalysed], "Customer":[customerAnalysed], "Catalog":[catalogAnalysed], "Checkout":[checkoutAnalysed], "Dimension":[dimensionAnalysed], "Manufacturer":[manufacturerAnalysed], "Payment":[paymentAnalysed]}
master_analysed_df = pd.DataFrame(master_analysed_df_assembler)

# Overwrite the current data stores
addressDF.to_csv("data/addressData.csv",index=False)
cartDF.to_csv("data/cartData.csv",index=False)
categoryDF.to_csv("data/categoryData.csv",index=False)
customerDF.to_csv("data/customerData.csv",index=False)
catalogDF.to_csv("data/catalogData.csv",index=False)
checkoutDF.to_csv("data/checkoutData.csv",index=False)
dimensionDF.to_csv("data/dimensionData.csv",index=False)
manufacturerDF.to_csv("data/manufacturerData.csv",index=False)
paymentDF.to_csv("data/paymentData.csv",index=False)

master_raw_df.to_csv("data/masterRawData.csv",index=False)

addressAnalysed.to_csv("data/addressAnalysed.csv",index=False)
cartAnalysed.to_csv("data/cartAnalysed.csv",index=False)
categoryAnalysed.to_csv("data/categoryAnalysed.csv",index=False)
customerAnalysed.to_csv("data/customerAnalysed.csv",index=False)
catalogAnalysed.to_csv("data/catalogAnalysed.csv",index=False)
checkoutAnalysed.to_csv("data/checkoutAnalysed.csv",index=False)
dimensionAnalysed.to_csv("data/dimensionAnalysed.csv",index=False)
manufacturerAnalysed.to_csv("data/manufacturerAnalysed.csv",index=False)
paymentAnalysed.to_csv("data/paymentAnalysed.csv",index=False)

master_analysed_df.to_csv("data/masterAnalysedData.csv",index=False)


