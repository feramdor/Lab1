# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:09:51 2023

@author: Fernanda
"""
import functions as fn
import data as dt
import pandas as pd
import numpy as np

tickers, cash_tickers, pond, pond_cash = dt.tickers(dt.file_concat("files"))

fechasCon=pd.to_datetime(["2021-01-29","2021-02-26","2021-03-31","2021-04-30","2021-05-31",
        "2021-06-30","2021-07-30","2021-08-31","2021-09-30","2021-10-26",
        "2021-11-30","2021-12-31","2022-01-26","2022-02-28","2022-03-31",
        "2022-04-29","2022-05-31","2022-06-30","2022-07-29","2022-08-31",
        "2022-09-30","2022-10-31","2022-11-30","2022-12-30","2023-01-25"])
