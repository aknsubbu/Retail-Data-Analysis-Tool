import time 

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import QueryEngineTool,ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.callbacks import CallbackManager
from llama_index.core.memory.chat_memory_buffer import ChatMemoryBuffer

import pandas as pd
import numpy as np


from dbConnect import fetchAll
from tools import tools
from prompts import context,instruction_str,address_prompt,cart_prompt,category_prompt,catalog_prompt,checkout_prompt,customer_prompt,dimension_prompt,manufacturer_prompt,payment_prompt
from hardDataAnalysis import analyze_address_data, analyze_cart_data, analyze_category_data, analyze_catalog_data, analyze_checkout_data, analyze_customer_data, analyze_dimension_data, analyze_manufacturer_data, analyze_payment_data

# The line `Settings.llm = Ollama(model='llama3:8b', request_timeout=600.0)` is setting the `llm`
# attribute of the `Settings` class to an instance of the `Ollama` class. Here's a breakdown of what
# each part of this line is doing:
Settings.llm = Ollama(model = 'llama3:8b',request_timeout=600.0)

llm = Settings.llm

memory = ChatMemoryBuffer.from_defaults()



# The `agent = ReActAgent(...)` line of code is creating an instance of the `ReActAgent` class with
# specific parameters. Here is a breakdown of what each parameter is doing:
agent = ReActAgent(
    tools=tools,
    memory=memory,
    llm=llm,
    verbose=True,
    context=context,
    callback_manager=CallbackManager(),
)

class AnalysisNode:
    def __init__(self, name, data):
        self.name = name
        addressDF, cartDF, categoryDF, customerDF, catalogDF, checkoutDF, dimensionDF, manufacturerDF, paymentDF = fetchAll() 
        self.raw_data = {
            'Address': addressDF,
            'Cart': cartDF,
            'Category': categoryDF,
            'Catalog': catalogDF,
            'Checkout': checkoutDF,
            'Customer': customerDF,
            'Dimension': dimensionDF,
            'Manufacturer': manufacturerDF,
            'Payment': paymentDF
        }  
        print("Data fetched successfully")
        # hard data analysis values
        address_data = analyze_address_data(addressDF)
        print("Address data analyzed")
        cart_data = analyze_cart_data(cartDF)
        print("Cart data analyzed")
        category_data = analyze_category_data(categoryDF)
        print("Category data analyzed")
        catalog_data = analyze_catalog_data(catalogDF)
        print("Catalog data analyzed")
        checkout_data = analyze_checkout_data(checkoutDF)
        print("Checkout data analyzed")
        customer_data = analyze_customer_data(customerDF)
        print("Customer data analyzed")
        dimension_data = analyze_dimension_data(dimensionDF)
        print("Dimension data analyzed")
        manufacturer_data = analyze_manufacturer_data(manufacturerDF)
        print("Manufacturer data analyzed")
        payment_data = analyze_payment_data(paymentDF)
        print("Payment data analyzed")

        self.prelim_analysis_data = {
            'Address': address_data,
            'Cart': cart_data,
            'Category': category_data,
            'Catalog': catalog_data,
            'Checkout': checkout_data,
            'Customer': customer_data,
            'Dimension': dimension_data,
            'Manufacturer': manufacturer_data,
            'Payment': payment_data}
    
    def CustomerAnalysis(self):
        formatted_prompt = customer_prompt.format(
            analysis_data=self.prelim_analysis_data['Customer'],
            raw_data = self.raw_data['Customer'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def AddressAnalysis(self):
        formatted_prompt = address_prompt.format(
            analysis_data=self.prelim_analysis_data['Address'],
            raw_data = self.raw_data['Address'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def CartAnalysis(self):
        formatted_prompt = cart_prompt.format(
            analysis_data=self.prelim_analysis_data['Cart'],
            raw_data = self.raw_data['Cart'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def CategoryAnalysis(self):
        formatted_prompt = category_prompt.format(
            analysis_data=self.prelim_analysis_data['Category'],
            raw_data = self.raw_data['Category'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def CatalogAnalysis(self):
        formatted_prompt = catalog_prompt.format(
            analysis_data=self.prelim_analysis_data['Catalog'],
            raw_data = self.raw_data['Catalog'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def CheckoutAnalysis(self):
        formatted_prompt = checkout_prompt.format(
            analysis_data=self.prelim_analysis_data['Checkout'],
            raw_data = self.raw_data['Checkout'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def DimensionAnalysis(self):
        formatted_prompt = dimension_prompt.format(
            analysis_data=self.prelim_analysis_data['Dimension'],
            raw_data = self.raw_data['Dimension'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def ManufacturerAnalysis(self):
        formatted_prompt = manufacturer_prompt.format(
            analysis_data=self.prelim_analysis_data['Manufacturer'],
            raw_data = self.raw_data['Manufacturer'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    
    def PaymentAnalysis(self):
        formatted_prompt = payment_prompt.format(
            analysis_data=self.prelim_analysis_data['Payment'],
            raw_data = self.raw_data['Payment'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = agent.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    