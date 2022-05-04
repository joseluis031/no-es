import pandas as pd
import random
class archivos2_1:
    def __init__(self,File):
        self.file = pd.read_csv(File)
    def lectura2_1(self):
        lista = []
        
        for i in range(len(self.file)):
            
            append =  random.randint(1,100)
            lista.append(append)
        self.file["Peso"] = lista

        print(self.file)
    
    def __init__(self,File):
        self.file = pd.read_csv(File)
        self.N = self.file["Peso"].count()   
    def calculo_media(self):
        suma = self.file["Peso"].sum()
        return suma/self.N




File = "no.csv"
hola = archivos2_1(File)
hola.lectura2_1()