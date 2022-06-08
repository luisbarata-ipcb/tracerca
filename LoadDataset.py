
import pandas as pd
import time
import datetime

from requests import head

# Load Dataset

data= pd.read_csv("Dataset/rca_2020_04_21.csv")

data

data.columns

data.sort_values("latency")
data.sort_values("timestamp")

# Data Processing

# Get distinct values of sources ans destinations

df_source = data.drop_duplicates(subset = ["source"])
df_source

df_target = data.drop_duplicates(subset = ["target"])
df_target


# Replace Strings with numbers

new_result = data.replace(
    {'source':{'docker_001':1, 'docker_002':2, 'docker_003':3, 'docker_004':4, 'docker_005':5, 'docker_006':6, 'docker_007':7, 
    'docker_008':8, 'os_021':11, 'os_022':12, 'db_003':21, 'db_007':22, 'db_009':23}, 
    'target':{'docker_001':1, 'docker_002':2, 'docker_003':3, 'docker_004':4, 'docker_005':5, 'docker_006':6, 'docker_007':7, 
    'docker_008':8, 'os_021':11, 'os_022':12, 'db_003':21, 'db_007':22, 'db_009':23}}
)

new_result = new_result.replace(
    {'source':{'None':0}}
)

new_result.head(10)


print(new_result)


matrix = new_result.corr()
print(matrix)

import seaborn as sns
import matplotlib.pyplot as plt


matrix = new_result.corr().round(2)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()


new_result['LatxTarget'] = new_result['latency'] * new_result['target']


from pyod.models.knn import KNN

detector = KNN(contamination=0.1, n_neighbors=15)
detector.fit(new_result.iloc[:,2:6])



# Normalize Data




# Load Injected Anomalies

anomalies= pd.read_csv("Dataset/ret_info.csv")

anomalies

anomalies.columns

anomalies.sort_values("latency")
anomalies.sort_values("timestamp")



s1 = "2020-04-21 04:17:00+08:00"
print(time.mktime(datetime.datetime.strptime(s1, "%Y-%m-%d %H:%M:%S%z").timetuple()))
s2 = "2020-04-21 04:22:00+08:00"
print(time.mktime(datetime.datetime.strptime(s2, "%Y-%m-%d %H:%M:%S%z").timetuple()))


print(data.loc[(data['timestamp'] >= 1587439020) & (data['timestamp'] <= 1587439320) ])


