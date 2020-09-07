# Importing libraries
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import decimal
import datetime
import re as re

#creating a function which finds 'whole cycyle' word to
#find the messages which includes the whole time cycle seconds inside of it
def Average_Cycle_Time():
    counter = 0
    total = 0
    average=0
    for index,row in df_log.iterrows():
        if row.Message.find('Whole cycle')!=-1:
            #print(row.Timestamp,row.Message)
            counter +=1
            total +=int(re.findall(r'\b\d+\b',row.Message)[0])
        else:
            continue
    average=total/counter
#total shows sum of seconds
#counter shows how many product assembled total
#average shows what is the average cycle time of products
    print(total,counter,average)
#importing csv log file
df_log= pd.read_csv('../../Desktop/logs.csv', sep=';', encoding='latin-1', names=["Timestamp", "Message"],
                    skiprows=[0], parse_dates=['Timestamp'])
#calling function
Average_Cycle_Time()

