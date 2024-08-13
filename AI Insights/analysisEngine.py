import time 
from IPython.display import display,Markdown

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import QueryEngineTool,ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.callbacks import CallbackManager
from llama_index.core.memory.chat_memory_buffer import ChatMemoryBuffer
from llama_index.experimental.query_engine import PandasQueryEngine,PandasInstructionParser
from llama_index.core.query_pipeline import (QueryPipeline as QP,Link,InputComponent)
import pandas as pd
import numpy as np


from dbConnect import fetchAll
from tools import tools
from prompts import context,instruction_str,address_prompt,cart_prompt,category_prompt,catalog_prompt,checkout_prompt,customer_prompt,dimension_prompt,manufacturer_prompt,payment_prompt,complete_prompt
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


def ensure_dataframe(data):
    if isinstance(data, dict):
        return pd.DataFrame.from_dict(data)
    elif isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
        return data
    else:
        raise ValueError("Object is neither a DataFrame, Series, nor a dictionary")

def dict_to_dataframe(d):
    """Convert a dictionary to a DataFrame."""
    if isinstance(d, dict):
        return pd.DataFrame([d])
    elif isinstance(d, pd.DataFrame):
        return d
    else:
        raise ValueError(f"Unexpected type: {type(d)}")

def custom_pandas_output_processor(output: str, df: pd.DataFrame) -> str:
    try:
        # Evaluate the pandas operation
        result = eval(output, {"df": df, "pd": pd})
        
        # If the result is a Series of booleans, we probably want to know about the True values
        if isinstance(result, pd.Series) and result.dtype == bool:
            return f"Number of True values: {result.sum()}\nIndices of True values: {result[result].index.tolist()}"
        
        # For other types of results, convert to string
        return str(result)
    except Exception as e:
        return f"Error evaluating pandas operation: {str(e)}"

class AnalysisNode:
    def __init__(self, name):
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

        # Ensure all data is in DataFrame format
        self.data = {k: ensure_dataframe(v) for k, v in self.raw_data.items()}

        print("Data fetched successfully")

        # Perform hard data analysis and convert results to DataFrames
        self.prelim_analysis_data = {
            'Address': dict_to_dataframe(analyze_address_data(self.data['Address'])),
            'Cart': dict_to_dataframe(analyze_cart_data(self.data['Cart'])),
            'Category': dict_to_dataframe(analyze_category_data(self.data['Category'])),
            'Catalog': dict_to_dataframe(analyze_catalog_data(self.data['Catalog'])),
            'Checkout': dict_to_dataframe(analyze_checkout_data(self.data['Checkout'])),
            'Customer': dict_to_dataframe(analyze_customer_data(self.data['Customer'])),
            'Dimension': dict_to_dataframe(analyze_dimension_data(self.data['Dimension'])),
            'Manufacturer': dict_to_dataframe(analyze_manufacturer_data(self.data['Manufacturer'])),
            'Payment': dict_to_dataframe(analyze_payment_data(self.data['Payment']))
        }

        # Create query engines
        self.query_engines = {
            k: PandasQueryEngine(df=v, verbose=True, output_processor=custom_pandas_output_processor)
            for k, v in self.prelim_analysis_data.items()
        }

        # Concatenate all raw data
        self.all_data_raw = pd.concat(list(self.data.values()), axis=1)

        # Concatenate all preliminary analysis data
        self.all_data_prelim = pd.concat(list(self.prelim_analysis_data.values()), axis=1)

        # Create query engines for combined data
        self.all_data_prelim_DFQueryEngine = PandasQueryEngine(df=self.all_data_prelim, verbose=True)
        self.all_data_raw_DFQueryEngine = PandasQueryEngine(df=self.all_data_raw, verbose=True)

        
    def raw_data_print(self):
        return self.raw_data

    def prelim_analysis_data_print(self):
        return self.prelim_analysis_data
    
    """
    The below functions perform various types of data analysis on different categories using specific
    prompts and query engines, measuring the computation time for each analysis.
    :return: Each of the methods is returning a tuple containing the response from querying the data and
    the time taken to compute the analysis.
    """
    def CompleteAnalysis(self):

        formatted_prompt = complete_prompt.format(
            analysis_data = self.all_data_prelim,
            raw_data=self.all_data_raw,
            instruction_str=instruction_str
        )
        start_time = time.time()
        response = self.all_data_raw_DFQueryEngine.query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time-start_time
        return response,compute_time

    def CustomerAnalysis(self):
        formatted_prompt = customer_prompt.format(
            analysis_data=self.prelim_analysis_data['Customer'],
            raw_data = self.raw_data['Customer'],
            instruction_str=instruction_str
        )

        start_time = time.time()   
        response = self.query_engines["Customer"].query(formatted_prompt)
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
        response = self.query_engines["Address"].query(formatted_prompt)
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
        response = self.query_engines["Cart"].query(formatted_prompt)
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
        response = self.query_engines["Category"].query(formatted_prompt)
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
        response = self.query_engines["Catalog"].query(formatted_prompt)
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
        response = self.query_engines["Checkout"].query(formatted_prompt)
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
        response = self.query_engines["Dimension"].query(formatted_prompt)
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
        response = self.query_engines["Manufacturer"].query(formatted_prompt)
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
        response = self.query_engines["Payment"].query(formatted_prompt)
        end_time = time.time()
        compute_time = end_time - start_time   
        return response, compute_time
    

# testing 
testing = AnalysisNode("Testing")
# print(testing.raw_data_print())
# print(testing.prelim_analysis_data_print())
print(testing.CustomerAnalysis())