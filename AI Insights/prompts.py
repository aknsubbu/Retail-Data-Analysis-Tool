from llama_index.core import PromptTemplate

instruction_str = """
1. Review the data provided and find patterns and trends  in the data to find hidden patterns.
2. Use the data to make predictions and recommendations.
3. Use the data to identify potential risks and opportunities.
4. Justify the findings with data and visualizations.
5. Use the data to make informed decisions.
6. Use the data to optimize business processes.
7. Use the data to improve customer experience.
"""

address_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Address: Contains information about customer addresses.

    Raw Data:
    {raw_data}
    
    Data after mathematical analysis:
    {analysis_data}


    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

cart_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Cart: Contains information about customer carts.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

category_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Category: Contains information about product categories.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

catalog_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Catalog: Contains information about product catalog.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

checkout_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Checkout: Contains information about customer checkouts.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

customer_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Customer: Contains information about customers.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

dimension_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Dimension: Contains information about product dimensions.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

manufacturer_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Manufacturer: Contains information about product manufacturers.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

payment_prompt = PromptTemplate(
    """
    As a retail analysis expert, you have been provided with data from a retail company. The data includes information about customers, products, sales, and more. Your task is to analyze the data and provide insights that can help the company make informed decisions and improve its business processes.

    VERIFY ALL SUGGESTIONS WITH DATA AND VISUALIZATIONS.

    The data includes the following tables:
    - Payment: Contains information about customer payments.

    Data:
    {analysis_data}

    Instructions:
    {instruction_str}

    Always follow the instructions and do not deviate from the task...

""")

context = """
Purpose: The purpose of this analysis is to provide insights that can help the retail company make informed decisions and improve its business processes.
Data: The data includes information about customers, products, sales, and more.
Style:Formal and Data driven
Domain: Data Analysis
Tone: Professional
"""