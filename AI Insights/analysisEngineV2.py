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


    

class AnalysisAgentNode:
            
    def __init__(self):
        #data fetch
        addressDF, cartDF, categoryDF, customerDF, catalogDF, checkoutDF, dimensionDF, manufacturerDF, paymentDF = fetchAll() 
        master_raw_df_assembler = {"Adress":[addressDF], "Cart":[cartDF], "Category":[categoryDF], "Customer":[customerDF], "Catalog":[catalogDF], "Checkout":[checkoutDF], "Dimension":[dimensionDF], "Manufacturer":[manufacturerDF], "Payment":[paymentDF]}
        self.master_raw_df = pd.DataFrame(master_raw_df_assembler)
        self.master_raw_df_1size = self.master_raw_df.shape[0]
        self.master_raw_df_QueryEngine = PandasQueryEngine(self.master_raw_df,head=self.master_raw_df_1size)
        #math analysis
        self.addressAnalysed = analyze_address_data(addressDF)
        self.cartAnalysed = analyze_cart_data(cartDF)
        self.categoryAnalysed = analyze_category_data(categoryDF)
        self.customerAnalysed = analyze_customer_data(customerDF)
        self.catalogAnalysed = analyze_catalog_data(catalogDF)
        self.checkoutAnalysed = analyze_checkout_data(checkoutDF)
        self.dimensionAnalysed = analyze_dimension_data(dimensionDF)
        self.manufacturerAnalysed = analyze_manufacturer_data(manufacturerDF)
        self.paymentAnalysed = analyze_payment_data(paymentDF)
        self.master_analysed_df_assembler = {"Adress":[self.addressAnalysed], "Cart":[self.cartAnalysed], "Category":[self.categoryAnalysed], "Customer":[self.customerAnalysed], "Catalog":[self.catalogAnalysed], "Checkout":[self.checkoutAnalysed], "Dimension":[self.dimensionAnalysed], "Manufacturer":[self.manufacturerAnalysed], "Payment":[self.paymentAnalysed]}
        self.master_analysed_df = pd.DataFrame(self.master_analysed_df_assembler)
        self.master_analysed_df_1size = self.master_analysed_df.shape[0]
        self.master_analysed_df_QueryEngine = PandasQueryEngine(self.master_analysed_df,head=self.master_analysed_df_1size)

        # TODO - Query Pipelines - 1 Each for the attributes for independent outlook
        # TODO - Query Pipelines - 1 for the master raw data
        # TODO - Query Pipelines - 1 for the master analysed data
        # TODO - Query Pipelines - 1 for the master raw data and master analysed data
        # TODO - Query Pipelines - 1 each for each subcombination of the attributes...
        # TODO - Query Pipelines - route for them to request specific combinations of the data
        



#testing 
testNode = AnalysisAgentNode()
