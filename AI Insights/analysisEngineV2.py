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
from loggerConfig import setup_logger
from prompts import context,instruction_str,address_prompt,cart_prompt,category_prompt,catalog_prompt,checkout_prompt,customer_prompt,dimension_prompt,manufacturer_prompt,payment_prompt,complete_prompt
from hardDataAnalysis import analyze_address_data, analyze_cart_data, analyze_category_data, analyze_catalog_data, analyze_checkout_data, analyze_customer_data, analyze_dimension_data, analyze_manufacturer_data, analyze_payment_data

# The line `Settings.llm = Ollama(model='llama3:8b', request_timeout=600.0)` is setting the `llm`
# attribute of the `Settings` class to an instance of the `Ollama` class. Here's a breakdown of what
# each part of this line is doing:
Settings.llm = Ollama(model = 'llama3:8b',request_timeout=600.0)

llm = Settings.llm

memory = ChatMemoryBuffer.from_defaults()

logger = setup_logger("AnalysisLogger", "logs/analysisEngine.log")



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
        try:
            addressDF, cartDF, categoryDF, customerDF, catalogDF, checkoutDF, dimensionDF, manufacturerDF, paymentDF = fetchAll() 
            logger.info("Data fetched successfully")
        except Exception as e:
            logger.error(f"Error fetching data: {e}")
            raise ValueError(f"Error fetching data: {e}")
        #raw data df conversion
        try:
            master_raw_df_assembler = {"Adress":[addressDF], "Cart":[cartDF], "Category":[categoryDF], "Customer":[customerDF], "Catalog":[catalogDF], "Checkout":[checkoutDF], "Dimension":[dimensionDF], "Manufacturer":[manufacturerDF], "Payment":[paymentDF]}
            self.master_raw_df = pd.DataFrame(master_raw_df_assembler)
            self.master_raw_df_1size = self.master_raw_df.shape[0]
            logger.info("Packaged into dataframe -- RAW")
        except Exception as e:
            logger.error(f"Error creating master raw dataframe: {e}")
            raise ValueError(f"Error creating master raw dataframe: {e}")
        
        self.master_raw_df_QueryEngine = QueryEngineTool(
            query_engine=PandasQueryEngine(self.master_raw_df,head=self.master_raw_df_1size),
            metadata=ToolMetadata(
                name = "self.master_raw_df",
                description="Query engine for the master raw data... This contains the data with respect to the address, cart, category, customer, catalog, checkout, dimension, manufacturer, and payment.... This data is used the generation of conclusions with respect to the ecommerce and buying patterns that are displayed by the users of the retail client...",
            ),

        )
        #math analysis
        try:
            self.addressAnalysed = analyze_address_data(addressDF)
            self.cartAnalysed = analyze_cart_data(cartDF)
            self.categoryAnalysed = analyze_category_data(categoryDF)
            self.customerAnalysed = analyze_customer_data(customerDF)
            self.catalogAnalysed = analyze_catalog_data(catalogDF)
            self.checkoutAnalysed = analyze_checkout_data(checkoutDF)
            self.dimensionAnalysed = analyze_dimension_data(dimensionDF)
            self.manufacturerAnalysed = analyze_manufacturer_data(manufacturerDF)
            self.paymentAnalysed = analyze_payment_data(paymentDF)
            logger.info("Mathematical Single Atrribute Analysis done successfully")
        except Exception as e:
            logger.error(f"Error in Mathematical Single Atrribute Analysis: {e}")
            raise ValueError(f"Error in Mathematical Single Atrribute Analysis: {e}")
        
        try:
            self.master_analysed_df_assembler = {"Adress":[self.addressAnalysed], "Cart":[self.cartAnalysed], "Category":[self.categoryAnalysed], "Customer":[self.customerAnalysed], "Catalog":[self.catalogAnalysed], "Checkout":[self.checkoutAnalysed], "Dimension":[self.dimensionAnalysed], "Manufacturer":[self.manufacturerAnalysed], "Payment":[self.paymentAnalysed]}
            self.master_analysed_df = pd.DataFrame(self.master_analysed_df_assembler)
            self.master_analysed_df_1size = self.master_analysed_df.shape[0]
            logger.info("Packaged into dataframe -- ANALYSED")
        except Exception as e:
            logger.error(f"Error creating master analysed dataframe: {e}")
            raise ValueError(f"Error creating master analysed dataframe: {e}")
        
        self.master_analysed_df_QueryEngine = QueryEngineTool(
            query_engine=PandasQueryEngine(self.master_analysed_df,head=self.master_analysed_df_1size),
            metadata=ToolMetadata(
                name = "self.master_analysed_df",
                description="""
                    This query engine has the raw data after masic mathematical analysis.... This data contains the follwing...
                    analyze_address_data(df_address)

        Attributes Analyzed:

            •	State: The State column is analyzed to count occurrences of each state.
            •	Line1: The length of addresses in the Line1 column is calculated to determine the average length.

        Output Data:

            •	State_Counts: A DataFrame with counts of addresses for each state. The index is the state name, and the values represent the count of occurrences.
            •	Average_Line1_Length: A single value representing the average length of the address lines in Line1.

        Attributes Analyzed:

            •	User_id: The User_id column is used to group data.
            •	sub_total: The sum of the sub_total column is calculated for each user.

        Output Data:

            •	Total_Subtotal_by_User: A DataFrame where the index is User_id and the values are the total subtotal amounts for each user.

        Attributes Analyzed:

            •	Name: The Name column is analyzed to count occurrences of each category name.

        Output Data:

            •	Category_Counts: A DataFrame with counts of each category name. The index is the category name, and the values are the count of occurrences.

        Attributes Analyzed:

            •	Category_id: The Category_id column is used to group data.
            •	price: The average price is calculated for each category.

        Output Data:

            •	Average_Price_by_Category: A DataFrame where the index is Category_id and the values are the average price of items in each category.


        Attributes Analyzed:

            •	Total_Paid: The average value of the Total_Paid column is calculated.

        Output Data:

            •	Average_Total_Paid: A DataFrame with a single value representing the average amount paid during checkout. The index is labeled Average_Total_Paid.

        Attributes Analyzed:

            •	age: The age column is converted to numeric, with non-numeric values coerced to NaN and then dropped. Age distribution is calculated.

        Output Data:

            •	Age_Distribution: A DataFrame with counts of each age. The index is age, and the values are the counts of occurrences.

        

        Attributes Analyzed:

            •	Length, Breadth, Height: These columns are used to calculate the volume (Length * Breadth * Height).

        Output Data:

            •	Average_Volume: A DataFrame with a single value representing the average volume of items based on dimensions. The index is labeled Average_Volume.


        Attributes Analyzed:

            •	Location: The Location column is analyzed to count occurrences of each location.

        Output Data:

            •	Location_Counts: A DataFrame with counts of each location. The index is the location, and the values are the count of occurrences.


        Attributes Analyzed:

            •	Method_Payment: The Method_Payment column is used to group data.
            •	Amount: The sum of the Amount column is calculated for each payment method.

        Output Data:

            •	Total_Amount_by_Method_Payment: A DataFrame where the index is Method_Payment and the values are the total amount for each payment method.

                """
            ),

        )

        # TODO - Query Pipelines - 1 Each for the attributes for independent outlook
        # TODO - Query Pipelines - 1 for the master raw data
        # TODO - Query Pipelines - 1 for the master analysed data
        # TODO - Query Pipelines - 1 for the master raw data and master analysed data
        # TODO - Query Pipelines - 1 each for each subcombination of the attributes...
        # TODO - Query Pipelines - route for them to request specific combinations of the data

    def complete_analysis(self):
        agent = ReActAgent(
            tools=[self.master_analysed_df_QueryEngine,self.master_raw_df_QueryEngine],
            memory=memory,
            llm=llm,
            verbose=True,
            context=context,
            callback_manager=CallbackManager(),
        )
        logger.info("Agent created for complete analysis")
        formatted_prompt = complete_prompt.format(
            analysis_data = self.master_analysed_df,
            raw_data = self.master_raw_df,
            instruction_str = instruction_str
        )
        start_time = time.time()
        response = agent.query(formatted_prompt)
        end_time = time.time()
        display(Markdown(f"**Response:** {response}"))
        compute_time = end_time - start_time
        logger.info(f'Complete Analysis is done in {compute_time} seconds')
        return response,compute_time



#testing 
testNode = AnalysisAgentNode()
print(testNode.complete_analysis())