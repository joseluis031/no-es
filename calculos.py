import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.N = self.datos["Peso"].count()
        
    def calculo_media(self):
        suma = self.datos["Peso"].sum()
        return suma/self.N
    
hola = Ejercicio("no.csv")
hola.calculo_media()