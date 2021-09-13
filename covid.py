# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:54:57 2021

@author: saidul haq
"""


import pyodbc as pyodbc
import pandas as pd
import seaborn as sns
import matplotlib as plt
from bokeh.io import show 
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper,PrintfTickFormatter
from bokeh.plotting import figure
from sqlalchemy import create_engine
from bokeh.io import output_file, show
import altair as alt
import streamlit as st
import time

st.set_option('deprecation.showPyplotGlobalUse', False) # disbale some text in run 

# Time progress 
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
  # End time progress
  
  

SERVER = '182.160.110.210'
DATABASE = 'LabBioBank'
DRIVER = 'SQL Server'
USERNAME = 'Saidul'
PASSWORD = 'saidul@bdchrf'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

data = pd.read_sql_query("Select * from [LabBioBank].[dbo].[vw_TestStatusCovid] order by [LabID] desc", connection)
data1= data[data.Result!= 'Not Done']
data2 = data1[data1.Result!= 'No Human RNA found']
data3 = data2[data2.Result!= 'No human RNA found']
data4 = data3[data3.Result!= 'Inconclusive']
data_final = data4[data4.Result!= 'Quantity Not Sufficient']



data_final['Testyear'] = pd.to_datetime(
    data_final['TestDate']).dt.year
data_final['TestMonth'] = pd.to_datetime(
    data_final['TestDate']).dt.month
data_final['no_of_sample_day']= data_final['TestDate'].groupby(data['TestDate']).transform('count')
data_final['no_of_sample_AgeY']= data_final['TestDate'].groupby(data_final['AgeY']).transform('count')

st.title("COVID-19 Dashboard")

st.write("""
 ## Sample tested by Month
        
""")

sns.relplot(data=data_final, x= 'TestMonth', y='no_of_sample_day', hue='Result', kind='line')
st.pyplot()

result_filter = 'Positive'
filter_data = data_final[data_final['Result']== result_filter]
st.subheader(f'Chart for all: {result_filter} data')
sns.relplot(data=filter_data, x= 'TestMonth', y='no_of_sample_day', hue='Result', kind='line')
st.pyplot()

print(data_final)

sns.relplot(data=data_final, x= 'TestMonth', y='no_of_sample_day', hue='Result', col='Testyear')
st.pyplot()
data_final.columns
list(data_final.columns.values.tolist()) 

df=data_final[['AgeY', 'CTValue', 'AgeM', 'AgeD']]
sns.pairplot(df, kind='scatter')
st.pyplot()



