import pandas as pd

class archivos2_1:
    def __init__(self,File):
        self.file = pd.read_csv(File)
    def lectura2_1(self):
        lista = []
        for i in range(len(self.file)):
            cosita1 = 0.3*int(self.file["Parcial1"][i])
            cosita2 = 0.3*int(self.file["Parcial2"][i])
            cosita3 = 0.4*int(self.file["Practicas"][i])
            append =  cosita1 + cosita2 + cosita3
            lista.append(append)
        self.file["Nota Final"] = lista
      print(self.file)
File = "no.csv"
hola = archivos2_1(File)
hola.lectura2_1()