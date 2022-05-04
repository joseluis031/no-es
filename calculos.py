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
        return self.datos["Peso"].median()
    def calculo(self):
        contador = 0
        for i in self.datos["Peso"]:
            if i > 40:
                contador+=1
        return contador
    
    def diagrama_sectores(self):
        fig, ax = plt.subplots()
    # Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Peso"].plot(kind = 'pie', ax = ax)
    # Ponermos el título
        ax.set_title('sectores', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
    # Guardamos el gráfico.
        plt.savefig('graficas/sectores.png', bbox_inches='tight')
        return plt.show()
        
    def diagrama_barras(self):
        fig, ax = plt.subplots()
    # Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Peso"].plot(kind = 'bar', ax = ax)
    # Ponermos el título
        ax.set_title('barras', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
    # Guardamos el gráfico.
        plt.savefig('graficas/barras.png', bbox_inches='tight')
        return plt.show()
    def histograma(self):
        fig, ax = plt.subplots()
    # Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Peso"].plot(kind = 'hist', ax = ax)
    # Ponermos el título
        ax.set_title('histograma', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
    # Guardamos el gráfico.
        plt.savefig('graficas/historia.png', bbox_inches='tight')
        return plt.show()
    
    
    def dispersion(self):
        fig, ax = plt.subplots()
    # Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        ax.scatter(self.datos["Peso"] and self.datos["M"])
    # Ponermos el título
        ax.set_title('dispersion', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
    # Guardamos el gráfico.
        plt.savefig('graficas/dispersion.png', bbox_inches='tight')
        return plt.show()

#Ejemplo
    
hola = Ejercicio("Datos.csv")
print (hola.calculo_media())
print(hola.calculo_desviacion())
print(hola.percentiles(70))
print(hola.mediana())
print(hola.calculo())
print(hola.diagrama_sectores())
print(hola.diagrama_barras())
print(hola.histograma())
print(hola.dispersion())