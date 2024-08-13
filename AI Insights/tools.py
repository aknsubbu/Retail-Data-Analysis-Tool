import numpy as np
import pandas as pd
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool

def ensure_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        try:
            data = pd.DataFrame(data)
        except Exception as e:
            raise ValueError(f"Cannot convert data to DataFrame: {e}")
    return data

def describe_data(data):
    data = ensure_dataframe(data)
    return data.describe()

def fill_missing_values(data, method='mean'):
    data = ensure_dataframe(data)
    if method == 'mean':
        return data.fillna(data.mean())
    elif method == 'median':
        return data.fillna(data.median())
    elif method == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Unsupported method")

def drop_missing_values(data, axis=0):
    data = ensure_dataframe(data)
    return data.dropna(axis=axis)

def group_by(data, by, agg_func='sum'):
    data = ensure_dataframe(data)
    return data.groupby(by).agg(agg_func)

def pivot_table(data, index, columns, values, aggfunc='sum'):
    data = ensure_dataframe(data)
    return pd.pivot_table(data, index=index, columns=columns, values=values, aggfunc=aggfunc)

def merge_dataframes(df1, df2, on, how='inner'):
    data = ensure_dataframe(data)
    return pd.merge(df1, df2, on=on, how=how)

def sort_values(data, by, ascending=True):
    data = ensure_dataframe(data)
    return data.sort_values(by=by, ascending=ascending)

def filter_data(data, condition):
    data = ensure_dataframe(data)
    return data.query(condition)

def calculate_correlation(data):
    data = ensure_dataframe(data)
    return data.corr()

def add_columns(data, **kwargs):
    data = ensure_dataframe(data)
    for col_name, col_values in kwargs.items():
        data[col_name] = col_values
    return data

def remove_duplicates(data):
    data = ensure_dataframe(data)
    return data.drop_duplicates()

def apply_function(data, func):
    data = ensure_dataframe(data)
    return data.apply(func)

# Define numpy functions as tools
def numpy_mean(array):
    data = ensure_dataframe(data)
    return np.mean(array)

def numpy_std(array):
    data = ensure_dataframe(data)
    return np.std(array)

def numpy_sum(array):
    data = ensure_dataframe(data)
    return np.sum(array)

def numpy_median(array):
    data = ensure_dataframe(data)
    return np.median(array)

def numpy_max(array):
    data = ensure_dataframe(data)
    return np.max(array)

def numpy_min(array):
    data = ensure_dataframe(data)
    return np.min(array)

def numpy_percentile(array, q):
    data = ensure_dataframe(data)
    return np.percentile(array, q)

def numpy_unique(array):
    data = ensure_dataframe(data)
    return np.unique(array)

def numpy_histogram(array, bins):
    data = ensure_dataframe(data)
    return np.histogram(array, bins)

# Wrap functions in QueryEngineTool
tools = [
    FunctionTool.from_defaults(describe_data, name="describe_data", description="Provides a summary of the data."),
    FunctionTool.from_defaults(fill_missing_values, name="fill_missing_values", description="Fills missing values in the data using the specified method."),
    FunctionTool.from_defaults(drop_missing_values, name="drop_missing_values", description="Drops rows or columns with missing values."),
    FunctionTool.from_defaults(group_by, name="group_by", description="Groups data by specified columns and applies an aggregation function."),
    FunctionTool.from_defaults(pivot_table, name="pivot_table", description="Creates a pivot table."),
    FunctionTool.from_defaults(merge_dataframes, name="merge_dataframes", description="Merges two DataFrames."),
    FunctionTool.from_defaults(sort_values, name="sort_values", description="Sorts the DataFrame by specified columns."),
    FunctionTool.from_defaults(filter_data, name="filter_data", description="Filters data based on a condition."),
    FunctionTool.from_defaults(calculate_correlation, name="calculate_correlation", description="Calculates the correlation between columns."),
    FunctionTool.from_defaults(add_columns, name="add_columns", description="Adds new columns to the DataFrame."),
    FunctionTool.from_defaults(remove_duplicates, name="remove_duplicates", description="Removes duplicate rows."),
    FunctionTool.from_defaults(apply_function, name="apply_function", description="Applies a function to each element in a DataFrame or Series."),
    FunctionTool.from_defaults(numpy_mean, name="numpy_mean", description="Calculates the mean of a numpy array."),
    FunctionTool.from_defaults(numpy_std, name="numpy_std", description="Calculates the standard deviation of a numpy array."),
    FunctionTool.from_defaults(numpy_sum, name="numpy_sum", description="Calculates the sum of a numpy array."),
    FunctionTool.from_defaults(numpy_median, name="numpy_median", description="Calculates the median of a numpy array."),
    FunctionTool.from_defaults(numpy_max, name="numpy_max", description="Finds the maximum value in a numpy array."),
    FunctionTool.from_defaults(numpy_min, name="numpy_min", description="Finds the minimum value in a numpy array."),
    FunctionTool.from_defaults(numpy_percentile, name="numpy_percentile", description="Calculates the percentile of a numpy array."),
    FunctionTool.from_defaults(numpy_unique, name="numpy_unique", description="Finds the unique elements of a numpy array."),
    FunctionTool.from_defaults(numpy_histogram, name="numpy_histogram", description="Computes the histogram of a numpy array.")
]