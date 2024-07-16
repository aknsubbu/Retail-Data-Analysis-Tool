import numpy as np
import pandas as pd
from llama_index.core.tools import QueryEngineTool,ToolMetadata

def describe_data(data):
    return data.describe()

def fill_missing_values(data, method='mean'):
    if method == 'mean':
        return data.fillna(data.mean())
    elif method == 'median':
        return data.fillna(data.median())
    elif method == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Unsupported method")

def drop_missing_values(data, axis=0):
    return data.dropna(axis=axis)

def group_by(data, by, agg_func='sum'):
    return data.groupby(by).agg(agg_func)

def pivot_table(data, index, columns, values, aggfunc='sum'):
    return pd.pivot_table(data, index=index, columns=columns, values=values, aggfunc=aggfunc)

def merge_dataframes(df1, df2, on, how='inner'):
    return pd.merge(df1, df2, on=on, how=how)

def sort_values(data, by, ascending=True):
    return data.sort_values(by=by, ascending=ascending)

def filter_data(data, condition):
    return data.query(condition)

def calculate_correlation(data):
    return data.corr()

def add_columns(data, **kwargs):
    for col_name, col_values in kwargs.items():
        data[col_name] = col_values
    return data

def remove_duplicates(data):
    return data.drop_duplicates()

def apply_function(data, func):
    return data.apply(func)

# Define numpy functions as tools
def numpy_mean(array):
    return np.mean(array)

def numpy_std(array):
    return np.std(array)

def numpy_sum(array):
    return np.sum(array)

def numpy_median(array):
    return np.median(array)

def numpy_max(array):
    return np.max(array)

def numpy_min(array):
    return np.min(array)

def numpy_percentile(array, q):
    return np.percentile(array, q)

def numpy_unique(array):
    return np.unique(array)

def numpy_histogram(array, bins):
    return np.histogram(array, bins)

# Wrap functions in QueryEngineTool
tools = [
    QueryEngineTool(fn=describe_data, metadata=ToolMetadata(name="describe_data", description="Provides a summary of the data.")),
    QueryEngineTool(fn=fill_missing_values, metadata=ToolMetadata(name="fill_missing_values", description="Fills missing values in the data using the specified method.")),
    QueryEngineTool(fn=drop_missing_values, metadata=ToolMetadata(name="drop_missing_values", description="Drops rows or columns with missing values.")),
    QueryEngineTool(fn=group_by, metadata=ToolMetadata(name="group_by", description="Groups data by specified columns and applies an aggregation function.")),
    QueryEngineTool(fn=pivot_table, metadata=ToolMetadata(name="pivot_table", description="Creates a pivot table.")),
    QueryEngineTool(fn=merge_dataframes, metadata=ToolMetadata(name="merge_dataframes", description="Merges two DataFrames.")),
    QueryEngineTool(fn=sort_values, metadata=ToolMetadata(name="sort_values", description="Sorts the DataFrame by specified columns.")),
    QueryEngineTool(fn=filter_data, metadata=ToolMetadata(name="filter_data", description="Filters data based on a condition.")),
    QueryEngineTool(fn=calculate_correlation, metadata=ToolMetadata(name="calculate_correlation", description="Calculates the correlation between columns.")),
    QueryEngineTool(fn=add_columns, metadata=ToolMetadata(name="add_columns", description="Adds new columns to the DataFrame.")),
    QueryEngineTool(fn=remove_duplicates, metadata=ToolMetadata(name="remove_duplicates", description="Removes duplicate rows.")),
    QueryEngineTool(fn=apply_function, metadata=ToolMetadata(name="apply_function", description="Applies a function to each element in a DataFrame or Series.")),
    QueryEngineTool(fn=numpy_mean, metadata=ToolMetadata(name="numpy_mean", description="Calculates the mean of a numpy array.")),
    QueryEngineTool(fn=numpy_std, metadata=ToolMetadata(name="numpy_std", description="Calculates the standard deviation of a numpy array.")),
    QueryEngineTool(fn=numpy_sum, metadata=ToolMetadata(name="numpy_sum", description="Calculates the sum of a numpy array.")),
    QueryEngineTool(fn=numpy_median, metadata=ToolMetadata(name="numpy_median", description="Calculates the median of a numpy array.")),
    QueryEngineTool(fn=numpy_max, metadata=ToolMetadata(name="numpy_max", description="Finds the maximum value in a numpy array.")),
    QueryEngineTool(fn=numpy_min, metadata=ToolMetadata(name="numpy_min", description="Finds the minimum value in a numpy array.")),
    QueryEngineTool(fn=numpy_percentile, metadata=ToolMetadata(name="numpy_percentile", description="Calculates the percentile of a numpy array.")),
    QueryEngineTool(fn=numpy_unique, metadata=ToolMetadata(name="numpy_unique", description="Finds the unique elements of a numpy array.")),
    QueryEngineTool(fn=numpy_histogram, metadata=ToolMetadata(name="numpy_histogram", description="Computes the histogram of a numpy array.")),
]