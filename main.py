# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:09:51 2023

@author: Fernanda
"""
import functions as fn
import data as dt
import pandas as pd
import numpy as np
import datetime

tickers, cash_tickers, pond, pond_cash = dt.tickers(dt.file_concat("files"))

fechasCon=pd.to_datetime(["2021-01-29","2021-02-26","2021-03-31","2021-04-30","2021-05-31",
        "2021-06-30","2021-07-30","2021-08-31","2021-09-30","2021-10-26",
        "2021-11-30","2021-12-31","2022-01-26","2022-02-28","2022-03-31",
        "2022-04-29","2022-05-31","2022-06-30","2022-07-29","2022-08-31",
        "2022-09-30","2022-10-31","2022-11-30","2022-12-30","2023-01-25"])

precios = fn.precios(
    fn.corregir(tickers),
    start_date=fechasCon[0],
    end_date=fechasCon[-1] + datetime.timedelta(days=1),
    fechas_consulta=fechasCon
    )

precios_cash = fn.precios(
    fn.ticker_reformat(cash_tickers),
    start_date=fechasCon[0],
    end_date=fechasCon[-1] + datetime.timedelta(days=1),
    fechasCon=fechasCon
)
precios_cash.drop("MXN",axis=1,inplace=True)
pasiva_inicial = fn.pasiva_inicial(precios,precios_cash,tickers,pond,pond_cash,1e6)

