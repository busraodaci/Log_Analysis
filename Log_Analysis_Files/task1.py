# Importing libraries
import pandas as pd
import numpy as np
import decimal
import datetime as dt
import pytz

#Importing csv file to project
df_log=pd.read_csv('../../Desktop/logs.csv', sep=';', encoding='latin-1', names=["Timestamp", "Message"], skiprows=[0], parse_dates=['Timestamp'])

#Changing timezone to EEST and save to different column
df_log['Timestamp_EEST']= df_log['Timestamp'].dt.tz_convert('Europe/Tallinn')
#defining 'Timestamp_EEST' as index
df_log.set_index('Timestamp_EEST',inplace=True)
#creating additional columns for next steps
df_log['Timestamp_EEST_H']= df_log['Timestamp'].dt.tz_convert('Europe/Tallinn').dt.time
df_log['Timestamp_EEST_D']= df_log['Timestamp'].dt.tz_convert('Europe/Tallinn').dt.date
#defining criteria for understand the working hours according to information
df_log['working_hours']= df_log['Timestamp_EEST_H'].between_time('7:30','19:30')

# filtering data
df_log = df_log[df_log['working_hours'].notnull()]

# df_log.to_csv(r'datas.csv', index = False) #usage: check the data

#defining product which is done during working hours
df=df_log[df_log['Message'].str.contains("PRODUCT_WORK_DONE")]
#grouping products which is done per shift
df=df.groupby("Timestamp_EEST_D")["Message"].count()
# How many products are assembled per shift
print(df.head(10))
