#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False) # disbale some text in run 

st.title("CT Value analysis")
st.write("""
## Analysis the CT value of Positive case         
""")

# In[2]:


sns.set(style='whitegrid')
sns.set_theme()


# In[3]:


sns.set_theme(style="dark")


# In[4]:

@st.cache
def load_data(nrows):
    ped = pd.read_csv('ct_value_ped.csv', nrows=nrows)
    return ped


data_load_state = st.text('Loading data...')
ped = load_data(111111288)
data_load_state.text('loading data..done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(ped.head())

if st.checkbox('Show description of data'):
    st.subheader('Data Description')
    st.write(ped.describe())


# In[5]:


ped.head()


hour_to_filter = st.slider('hour', 0, 23, 17)



# In[10]:


st.write("""
### Pair Plot among age and CT value          
""")

sns.pairplot(ped, corner=True)
st.pyplot()


# In[11]:

st.write(""" ### Joint Plot among age and Ct value """)
g= sns.jointplot(data= ped, x='AgeY', y='ctvalue', kind='reg',height=5, ratio=2, marginal_ticks=True)
g.set_axis_labels("Age(Years)", "CT value")
st.pyplot()



g= sns.jointplot(data= ped, x='AgeY', y='ctvalue', kind='hex',  height=5, ratio=2, marginal_ticks=True)
g.set_axis_labels("Age(Years)", "CT value")



# In[23]:


sns.jointplot(data= ped, x='AgeY', y='ctvalue', kind='hist')
g.set_axis_labels("Age(Years)", "CT value")




# In[18]:

st.write(""" ### CT value by Age in the kde plot         
""")
g = sns.jointplot(data=ped, x="AgeY", y="ctvalue")
g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6)
g.plot_marginals(sns.rugplot, color="r", height=-.15, clip_on=False)
st.pyplot()

import altair as alt
brush = alt.selection(type='interval')

points = alt.Chart(ped).mark_point().encode(
    x='AgeY',
    y='ctvalue',
    color=alt.condition(brush, 'sex', alt.value('lightgray'))
).add_selection(
    brush
)  
bars = alt.Chart(ped).mark_bar().encode(
    y='sex',
    color='sex',
    x='count(sex)'
).transform_filter(
    brush
)
points & bars

st.pyplot()


# In[19]:



# In[ ]:


# Logistic regression 

