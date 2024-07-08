from io import BytesIO
import numpy as np
import pandas as pd
import holoviews as hv
import panel as pn
from scipy.optimize import minimize
pn.extension('tabulator', design='material', template='material', loading_indicator=True)
import hvplot.pandas

from dataFetch import get_data

@pn.cache
def load_data():
    data = get_data()
    return data

data = load_data()

columns = list(data.columns[0][1:-1])

x = pn.widgets.Select(value='bill_length_mm', options=columns, name='x')
y = pn.widgets.Select(value='flipper_length_mm', options=columns, name='y')

dashboard = pn.Row(pn.Column('## Penguins', x, y),
       pn.bind(data[0].hvplot.scatter, x, y, by='species'))

dashboard.show()
