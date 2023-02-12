"""
Created on Thu Feb  9 16:34:56 2023

@author: Fernanda
"""
import pandas as pd
import numpy as np
import yfinance as yf

# Inversión Pasiva

def precios(tickers,start_date, end_date, fechas_consulta):
    """
    Función precios para inversión pasiva
    ...
    """
    historicos = yf.download(tickers, start = start_date, end = end_date)['Close'] 
    historicos_cash = yf.download("MXN=X",start = start_date,end = end_date)["Close"]
    MXN = pd.DataFrame(data = historicos_cash)
    mxn_consulta = np.array([MXN.loc[fechas_consulta[i]] for i in  range(len(fechas_consulta))])
    historicos_puntuales = [historicos.loc[fechas_consulta[i]] for i in range(len(fechas_consulta))]
    res = pd.DataFrame(data = historicos_puntuales, index = fechas_consulta)
    res["MXN"] = mxn_consulta   
    return res

def corregir(tickers):
    new_tickers = []
    for ticker in tickers:
        if ticker == "MXN":
            pass
        else:
            new_tickers.append(ticker.replace(".","-").replace("*","") +".MX")

    return new_tickers


def inversion_pasiva(precios,fechas_consulta,w, cash_w, c_0,tickers):

    precios_0 = np.array(precios.iloc[0,:])
    pos_inic_money = np.multiply(np.array(w)/100,c_0)
    pos_inic_cash_money = np.multiply(np.array(cash_w)/100,c_0)
    pos_inic = [pos_inic_money[i]/precios_0[i] for i in range(len(precios_0))]
    pos_inic = np.array(pos_inic)
    pos_inic_floor = np.floor(pos_inic)
    cash = np.multiply(pos_inic,precios_0).sum() - np.multiply(pos_inic_floor,precios_0).sum()
    cash += pos_inic_cash_money.sum()
    df_inicial = pd.DataFrame(columns= ["Ticker","Peso(%)","Precio","Acciones","Total"])
    df_inicial["Ticker"] = tickers
    df_inicial["Peso(%)"] = w
    df_inicial["Precio"] = precios_0
    df_inicial["Acciones"] = pos_inic_floor
    df_inicial["Total"] = df_inicial["Precio"]*df_inicial["Acciones"]
    df_inicial.loc["Cash"] = ["Cash",(cash/c_0)*100,cash,1,cash]

    #Final de procesamiento de inversion pasiva inicial

    out = pd.DataFrame(columns = ["Fecha","Portafolio","Rend (%)","Acum"])
    out["Fecha"] = fechas_consulta
    acciones = np.array(df_inicial["Acciones"][:-1])
    invest = precios*acciones
    temp = []
    for i in range(len(fechas_consulta)):
        temp.append(invest.iloc[i].sum()+cash)
    out["Portafolio"] = temp
    out["Rend (%)"] = out["Portafolio"].pct_change()*100
    out["Acum"] = out["Rend (%)"].cumsum()
    out["Portafolio"][0] = 1000000
    return out.round(2), df_inicial.round(2)

# Inversión Activa
def prices_act(tickers, start_date, end_date):
    """
    Función precios para inversión activa
    """
    data = yf.download(tickers, start =start_date, end=end_date)["Close"]
    serie_MXN = yf.download("MXN=X", start =start_date, end=end_date)["Close"]
    data.reset_index(inplace = True)
    # Nueva columna sin timezone
    nueva_col = data["Fecha"].dt.tz_localize(None)
    data["Fecha"] = nueva_col
    data.set_index("Fecha", inplace = True)
    mxn_consulta = np.zeros(len(nueva_col))
    # Pasamos a DataFrame
    MXN = pd.DataFrame(data = serie_MXN)
    for i in range(len(nueva_col)):
        mxn_consulta[i] = MXN.loc[nueva_col[i]]
    # Nueva columna de precios de cierre
    data["MXN"] = mxn_consulta
    return data

def inversion_activa_inicial(precios, tickers, w, w_cash, c_0):
    inicial_prices = np.array(precios.iloc[0, :])
    # Inversion inicial
    inicial = np.multiply(np.array(w['Pond']) / 100, c_0)
    # Cash 
    inicial_cash = 0
    for i in w_cash['Pond']:
        inicial_cash = inicial_cash + i / 100 * c_0
    # Diccionario para inivesion inicial
    inicial_pos  = {}
    for i, tikcer in enumerate(tickers):
        inicial_pos[tikcer] = inicial_cash[i] / inicial_prices[i]

    # Agregamos cash al diccionario
    inicial_pos['Cash'] = inicial_cash
    return inicial_pos

