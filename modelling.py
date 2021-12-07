import pandas as pd import numpy as np
import matplotlib.pyplot as plt import seaborn as sns
import warnings
%matplotlib inline warnings.filterwarnings('ignore')
data=pd.read_csv('../input/wine-quality/winequalityN.csv')
data.head()
data.describe()
data.dtypes
data.isnull().sum()
for cols,value in data.items():
   if cols!='type': data[cols]=data[cols].fillna(data[cols].mean())
    data.isnull().sum()
    
plt.figure(figsize=(10,8))
sns.heatmap(wn_df.corr(),annot=True)
plt.show()
# trainmodel
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
scaler.fit(data.drop('quality',axis=1))

from sklearn.model_selection import train_test_split
X=data.drop('quality',axis=1)
y=data['quality']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

#linear regression
from sklearn.linear_model import LinearRegression
lnr=LinearRegression()
lnr.fit(X_train,y_train) 
#acurracy
lnr=lnr.score(X_test, y_test)

# random forest
from sklearn.ensemble import RandomForestClassifier 
rdf=RandomForestClassifier(n_estimators=100)
rdf.fit(X_train,y_train)
rdf=rdf.score(X_test,y_test)

# decision tree
from sklearn.tree import DecisionTreeClassifier 
dst=DecisionTreeClassifier() 
dst.fit(X_train,y_train)
dst=dst.score(X_test,y_test)
models = pd.DataFrame({ 'Model': ['Linear Regression','Random Forest','Decision Tree'], 'Score': [lnr,rdf,dst]})
models.sort_values(by='Score', ascending=False)
plt.figure(figsize=(10,5)) 
sns.barplot(x='Model',y='Score',data=models) 
plt.show()



