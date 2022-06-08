import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
# from pyod.models.abod import ABOD
from pyod.models.knn import KNN

df = pd.read_csv("Dataset/rca_2020_04_21.csv")

df.head(10)
detector = KNN(contamination=0.1, n_neighbors=15)
detector.fit(df.iloc[:,2:6])
previsoes = detector.labels_
previsoes
np.unique(previsoes, return_counts=True)
confianca_previsoes = detector.decision_scores_
confianca_previsoes
outliers = []
for i in range(len(previsoes)):
    print(i)
    if previsoes[i] == 1:
        outliers.append(i)
# print(outliers)
lista_outliers = df.iloc[outliers,:]
lista_outliers