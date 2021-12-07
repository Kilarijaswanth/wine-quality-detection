import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Dataframe object is being created
data = pd.read_csv(R'https://www.kaggle.com/rajyellow46/wine-quality')
print(data.head())
print(data.info())
print(data.describe())

data.hist(bins=25,figsize=(10,10))
# histogram displayed
plt.show()

plt.figure(figsize=[10,8])
# plot bar graph
plt.bar(data['quality'],data['alcohol'],color='R')
plt.xlabel('quality')
plt.ylabel('alcohol')

# ploting heatmap
plt.figure(figsize=[19,10],facecolor='blue')
sb.heatmap(data.corr(),annot=True)

for i in range(len(data.corr().columns)):
    for j in range(i):
        if abs(data.corr().iloc[i,j]) >0.7:
            hd = data.corr().columns[i]
            print(hd)
  # drop of row
new_data=data.drop('total sulfur dioxide',axis=1)

#handling of null values and filling them
new_data.isnull().sum()
new_data.update(new_data.fillna(new_data.mean()))

next_data = pd.get_dummies(new_data,drop_first=True)
# display new dataframe
next_data

data_dummyes[''best quality''] = [ 1 if x>=7 else 0 for x in data.quality] 
print(data_dummyes)

#data visualization and cleaning is done

