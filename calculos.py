import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
import numpy as np

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        
    def calculo_media(self):
        media = self.datos["Peso"].mean()
        return media
    def calculo_desviacion(self):
        desviacion = self.datos["Peso"].std()
        return desviacion
    def percentiles(self, n):
        percentil = np.percentile(self.datos["Peso"], n)
        return percentil
    def mediana(self):
        return self.percentiles(50)
    
    
hola = Ejercicio("Datos.csv")
print (hola.calculo_media())
print(hola.calculo_desviacion())
print(hola.percentiles(70))
print(hola.mediana())