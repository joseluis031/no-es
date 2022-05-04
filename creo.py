import numpy as np


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.DataFrame(np.random.randint(1,100,size=(101,1)),columns=["Peso"])
df.to_csv("Datos.csv")
