import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyreadr

data = pyreadr.read_r ("births2006.smpl.rda")
# print (data.keys())

df = data['births2006.smpl']
print (df.columns)


'Task-1 : The first five records of the dataset'
# print (df.head(5))

'Task-2 : The Number of Birth in 2006 per day of the week in the U.S.'
dob_wk = df['DOB_WK']
day = np.array()

plt.bar(dob_wk,range = (1,7),color='teal', rwidth=0.8)
plt.title ("The Number of Birth in 2006 per day of the week in the U.S.")
# plt.xticks("Number of Birth")
# plt.yticks("Day of the week")
plt.show()


'Task-3: The Number of Birth per Delivery Method and Day of Week in 2006 in the U.S.'


'Task-4: The Number of Birth based on Birth Weight and Single or Multiple Birth Using Histogram.'








