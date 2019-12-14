import csv
import pandas as pd
import logging
from pandas.compat import StringIO

from .models import Frame

from django.core.cache import cache

logger = logging.getLogger(__name__)

def process_frame(file_handle):
    df = pd.read_csv(file_handle, delimiter = ',')
    dfi, dft = process_content_info(df)
    frame = Frame(head=20)
    frame.info = dfi
    frame.dtypes = dft
    frame.stats = df.describe().to_html(classes='modaltable')
    frame.data = df.head(frame.head).to_html(classes='modaltable')
    frame.alldatahtml = df.to_html(classes='modaltable')
    frame.alldata = df
    frame.source = file_handle
    corr = df.corr()
    frame.corr = corr.to_html(classes='modaltable')
    frame.columns = df.columns.values.tolist()

    cache.set(file_handle, frame)

    return frame

def process_content_info(content: pd.DataFrame):
    content_info = StringIO()
    content.info(buf=content_info, null_counts=False)
    str_ = content_info.getvalue()

    lines = str_.split("\n")
    table = StringIO("<br>".join(lines[3:-3]))
    datatypes = pd.read_csv(table, delim_whitespace=True, names=["column", "count", "null", "dtypes"])
    info = "<br>".join(lines)

    return info, datatypes

def magnify():
    return [dict(selector="th",
                 props=[("font-size", "7pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])
]