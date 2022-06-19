
import pandas as pd
from pandas import dt
import time
import datetime

from requests import head

# Load Dataset

data= pd.read_csv("C:/GIT/Dataset/rca_2020_04_21.csv")

data

data.columns

data.sort_values("latency")
data.sort_values("timestamp")

# Data Processing

# Get distinct values of sources and destinations

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

new_result.head(1)


print(new_result)


# Cria novas Features

# Latencia X Target

new_result['LatxTarget'] = new_result['latency'] * new_result['target']


# Latencia X Source



# Nova coluna formato Data

from datetime import datetime, timedelta
timestamp = 1587398400084
timestamp = str(timestamp)
timestamp = (timestamp[0:10])
timestamp = int(timestamp)
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

print(dt_object + timedelta(hours=8))

# Função para transformar Timestamp em Data

def my_timestamp_date(times):
    #timestamp = str(times)
    #timestamp = (timestamp[0:10])
    #timestamp = int(timestamp)

    timestamp = int(times) / 1000.0

    dt_object = datetime.fromtimestamp(timestamp)

    #print("dt_object =", dt_object)
    #print(dt_object + timedelta(hours=7))
 #   return str(dt_object + timedelta(hours=7))
    return (dt_object + timedelta(hours=7))
    
teste = my_timestamp_date(1587398400118)
teste

my_timestamp_date("1587398400084")

new_result['data'] = (new_result['timestamp'])
new_result['data'] = datetime.fromtimestamp(new_result['data'])



new_result['data'] = my_timestamp_date(new_result['timestamp'])

new_result.head(10)

# Matriz de Correlação

matrix = new_result.corr()
print(matrix)

import seaborn as sns
import matplotlib.pyplot as plt


matrix = new_result.corr().round(2)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()





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


