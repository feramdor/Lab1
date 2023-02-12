"""
Created on Sun Feb  12 17:34:21 2023

@author: Fernanda
"""
import pandas as pd
import functions as fn
import matplotlib.pyplot as plt

plot = pd.DataFrame(fn.inversion_pasiva)
plot

plot['Rend (%)'].plot()
plt.title('Rendimiento del Portafolio')
