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