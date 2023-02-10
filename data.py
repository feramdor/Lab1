# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:34:52 2023

@author: Fernanda
"""
import pandas as pd
import os


def file_concat(path):
    """
    File concat function
    ...
    """
    files = os.listdir(path)
    concat_list = []
    for file in files:
        concat_list.append(pd.read_csv("files/"+file,skiprows=2))
    return pd.concat(concat_list,axis=0).drop(37)

def tickers(x):
    """
    tickers function
    ...
    """
    dfW = pd.read_csv('files/NAFTRAC_20230125.csv',skiprows=2)
    tickers= x.groupby(["Ticker"])["Ticker"].count().to_frame()[x.groupby(["Ticker"])["Ticker"].count().to_frame()['Ticker'] == 25]
    cashTickers = x.groupby(["Ticker"])["Ticker"].count().to_frame()[x.groupby(["Ticker"])["Ticker"].count().to_frame()["Ticker"] != 25]
    output = list(tickers.index)
    cashTickersRaw = list(cashTickers.index)
    cashTickers = []
    WCash = [] 
    w = [dfW["Peso (%)"][dfW["Ticker"] == ticker].to_numpy()[0] for ticker in output]
    for ticker in cashTickersRaw:
        if dfW["Peso (%)"][dfW["Ticker"] == ticker].values > 0:
            WCash.append(dfW["Peso (%)"][dfW["Ticker"] == ticker].values)  
            cashTickers.append(ticker) 
        else:
            pass 
    return output, cashTickers, w, WCash
