
"""
Created on Tue Feb  7 21:09:51 2023

@author: Fernanda
"""
import functions as fn
import data as dt
import pandas as pd
import numpy as np
import datetime

tickers, cash_tickers, w, w_cash = dt.tickers(dt.file_concat("files"))

fechasCon= dt.fechasConsultaPasiva()

precios = fn.precios(fn.corregir(tickers), start_date = fechasCon[0], end_date = fechasCon[-1] + datetime.timedelta(days = 1),
    fechas_consulta = fechasCon)

precios_cash = fn.precios(fn.corregir(cash_tickers), start_date=fechasCon[0], end_date = fechasCon[-1] + datetime.timedelta(days=1),
    fechas_consulta = fechasCon)
precios_cash.drop("MXN",axis = 1,inplace = True)
inversion_pasiva, inversion_pasiva_inicial = fn.inversion_pasiva(
    precios=precios,
    fechas_consulta=fechasCon,
    w = w,
    cash_w = w_cash,
    c_0 = 1000000,
    tickers = tickers)