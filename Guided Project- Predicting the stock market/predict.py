import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data=pd.read_csv('sphist.csv')

data['Date']=pd.to_datetime(data['Date'])


#data=data.sort_values(by='Date', ascending=True)


data['AvgPrice365Days']=0
data['AvgPrice5Days']=0
data['StDev5Days']=0
#data['StDevVol5Days']=0
#data['StDevVol365Days']=0
data['AvgVol5Days']=0
data['AvgVol365Days']=0

#print(data)

for i, row in data.iterrows():
    
    if row['Date']>datetime(year=1950, month=3, day=6):
        
        row['AvgPrice5Days']=np.mean(data.iloc[i-5:i]['Close'])
        row['StDev5Days']=np.std(data.iloc[i-5:i]['Close'])
        #row['StDevVol5Days']=np.std(data.iloc[i-5:i]['Volume'])
        row['AvgVol5Days']=np.mean(data.iloc[i-5:i]['Volume'])
        
        if row['Date']>datetime(year=1951, month=3, day=1):
            
            row['AvgPrice365Days']=np.mean(data.iloc[i-365:i]['Close'])
            #row['StDevVol365Days']=np.std(data.iloc[i-365:i]['Volume'])
            row['AvgVol365Days']=np.mean(data.iloc[i-365:i]['Volume'])
   
    data.iloc[i]=row

#print(data)

data=data[data['Date']>datetime(year=1951, month=3, day=1)]
data=data.dropna(axis=0)

data_train=data[data['Date']<datetime(year=2013, month=1, day=1)]
data_test=data[data['Date']>=datetime(year=2013, month=1, day=1)]


lr=LinearRegression()
lr.fit(data_train[['AvgPrice365Days','AvgPrice5Days','StDev5Days','AvgVol5Days','AvgVol365Days']],data_train['Close'])
predictions=lr.predict(data_test[['AvgPrice365Days','AvgPrice5Days','StDev5Days','AvgVol5Days',
 'AvgVol365Days']])

error=mean_absolute_error(data_test['Close'],predictions)

print(error)