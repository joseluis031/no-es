import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer
import random

list=[]
for i in range(1):
    list.append(random.randint(0,12))

city = pd.DataFrame([[list]], columns=['Manzanas'])
city.to_csv('city.csv')
