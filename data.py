
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

def fechasConsultaPasiva():
    f = pd.to_datetime(["2021-01-29","2021-02-26","2021-03-31","2021-04-30","2021-05-31",
        "2021-06-30","2021-07-30","2021-08-31","2021-09-30","2021-10-26",
        "2021-11-30","2021-12-31","2022-01-26","2022-02-28","2022-03-31",
        "2022-04-29","2022-05-31","2022-06-30","2022-07-29","2022-08-31",
        "2022-09-30","2022-10-31","2022-11-30","2022-12-30","2023-01-25"])
    return f

def tickers_activa():
    dfAct = pd.read_csv("files/NAFTRAC_20210129.csv", skiprows = 2)
    tickers = pd.unique(dfAct["Ticker"])[:-1]
    # DataFrame con precios y pesos 
    w = pd.DataFrame(columns=["Ticker", "Pond"])
    w["Ticker"] = tickers
    # Pesos para cada ticker
    temp = []
    for ticker in tickers:
        weight = dfAct["Peso (%)"][dfAct["Ticker"] == ticker].to_numpy()[0]
        temp.append(weight)
    # Añadimos los pesos al DataFrame
    w["Pond"] = temp
    w.set_index("Ticker", inplace = True)
    return tickers, w

