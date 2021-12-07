import pandas as pd import numpy as np
import matplotlib.pyplot as plt import seaborn as sns
import warnings
%matplotlib inline warnings.filterwarnings('ignore')
df=pd.read_csv('../input/wine-quality/winequalityN.csv')
df.head()
df.describe()
df.dtypes
df.isnull().sum()
for cols,value in df.items():
   if cols!='type': df[cols]=df[cols].fillna(df[cols].mean())
    df.isnull().sum()
    
plt.figure(figsize=(10,8))
sns.heatmap(wn_df.corr(),annot=True)
plt.show()
# trainmodel
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
scaler.fit(df.drop('quality',axis=1))

from sklearn.model_selection import train_test_split
X=df.drop('quality',axis=1)
y=df['quality']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

