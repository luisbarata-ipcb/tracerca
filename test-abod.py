from pickle import FALSE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from pyod.models.abod import ABOD
import time
import datetime


data= pd.read_csv("Dataset/dcos_docker.csv")

data

data.columns


data.head(100)



cpu_data = data[data['name'] == 'container_cpu_used']
cpu_data.head(100)

data_normalizada = data

data_normalizada["succ"].replace({"True": "1", "Flase": "0"}, inplace=True)

detector = ABOD()
detector.fit(cpu_data.iloc[:,4:5])


from pyod.models.knn import KNN
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print
from pyod.utils.example import visualize








previsoes = detector.labels_
previsoes

np.unique(previsoes, return_counts=True)

confianca_previsoes = detector.decision_scores_
confianca_previsoes

outliers = []
for i in range(len(previsoes)):
    #print(i)
    if previsoes[i] == 1:
        outliers.append(i)
print(outliers)

lista_outliers = data.iloc[outliers,:]

lista_outliers

cpu_data.sort_values("value", ascending=False)


objectdate = datetime.fromtimestamp(1590080192)
print ("timestamp to date conversion.")
print (" date" , objectdate)

from dateutil import tz
ts = 1590079983 
dt_UTCplus8 = datetime.fromtimestamp(ts, tz=tz.gettz("Etc/GMT-8"))
print(dt_UTCplus8)