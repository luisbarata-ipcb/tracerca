##The following code shows how to normalize all values in a NumPy array:

import numpy as np 

#create NumPy array
data = np.array([[13, 16, 19, 22, 23, 38, 47, 56, 58, 63, 65, 70, 71]])

#normalize all values in array
data_norm = (data - data.min())/ (data.max() - data.min())

#view normalized values
data_norm

# array([[0.        , 0.05172414, 0.10344828, 0.15517241, 0.17241379,
#        0.43103448, 0.5862069 , 0.74137931, 0.77586207, 0.86206897,
#        0.89655172, 0.98275862, 1.        ]])



##The following code shows how to normalize all variables in a pandas DataFrame:

import pandas as pd

#create DataFrame
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

#normalize values in every column
df_norm = (df-df.min())/ (df.max() - df.min())

#view normalized DataFrame
df_norm

#        points	        assists	 rebounds
#0	0.764706	0.125	 0.857143
#1	0.000000	0.375	 0.428571
#2	0.176471	0.375	 0.714286
#3	0.117647	0.625	 0.142857
#4	0.411765	1.000	 0.142857
#5	0.647059	0.625	 0.000000
#6	0.764706	0.625	 0.571429
#7	1.000000	0.000	 1.000000