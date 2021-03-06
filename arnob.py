# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:57:57 2021

@author: LENOVO
"""


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Draw a title and some text to the app:
'''
# This is the document title of this website

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x

st.text('This website is created based on some consent information')
st.markdown('I am really **a cool guy**.')
# Mathmetical expression
st.latex(r'''
         a+ar+a r^2 + a r^3 + \cdots + a r^{n-1}=
         \sum_{k=0}^{n-1} ar^k =
         a\left(\frac{1-r^{n}}{1-r}\right)
         ''')
# now see what write do this
st.text('a+ar+a r^2 + a r^3 + \cdots + a r^{n-1}=\sum_{k=0}^{n-1} ar^k')

st.title ('Website of Shakhawat Hossain Arnob')

st.write("""
## My Name is Shakhawat Hossain Arnob. :sunglasses: I live in Bangladesh
### Currently I am working as Data Analyst.
My mobile number is 01841008583. To see my Photo please go bellow 
       

""")

uploaded_file = st.file_uploader("arnob1", type="jpg")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40],
     })
st.write('Below is a datafram', df, 'above is dataframe')

c= alt.Chart(df).mark_circle().encode(
    x='first column', y='second column', tooltip=['first column', 'second column'])
st.write('**This the the random chart**', c)

# Create a DataFram with Random number

df1 = pd.DataFrame(
    np.random.randn(50,10),
    columns =('col %d' % i for i in range(10)))
st.dataframe(df1)
st.text('The maximum value of the dataframe')
st.dataframe( df1.style.highlight_max(axis=0)) # this will highlight the max value of each column

## displaying chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.table(chart_data)

st.write('**The line chart of the table is**')
st.line_chart(chart_data)

st.write('**The area chart of the table is**')
st.area_chart(chart_data)

st.write('**The bar chart of the table is**')
st.bar_chart(chart_data)


# bokeh chart
st.write('**Bokeh chart**')
from bokeh.plotting import figure
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)

# Display map

st.write('Map')
import pandas as pd
dfa = pd.DataFrame(
    np.random.randn(10000,2) / [50,50] + [24.09, 90.11],
    columns = ['lat', 'lon'])
st.map(dfa)





import os
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

# Media Visualizaiton
st.write('**Image/Photo**')
from PIL import Image
image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains',
         use_column_width=True)


# Interactive gadgets

if st.button('Say hello'):
        st.write('Why hello there')
else:
            st.write('Goodbye')
            
genre = st.radio(
    "What is your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy")
    

fruit = st.radio(
    "What is your favorite fruit",
    ('Apple', 'Mango', 'Watermelon'))

if fruit == 'Apple':
    st.write('You selected Apple.')
elif fruit == 'Mango':
        st.write("You didn't select Mango")
else:
        st.write('You select watermelon')  

fruit1 = st.selectbox(
    'What is your favorite fruit?',
    ('Apple', 'Mango', 'Watermelon'))

st.write('You selected', fruit1)  

fruit2 = st.multiselect(
    'What is your favorite color',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ["Red"]) #this line is defult
st.write('You selected:', fruit2)  

# datetime slider

from datetime import datetime
start_time = st.slider(
    'When do you start?',
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY -hh:mm")
st.write("Start time:", start_time)

start_color, end_color = st.select_slider(
    'Selecgt a rnage of color wavelenght',
    options=['red', 'blue', 'orange', 'yellow', 'green', 'indigo','violet'],
    value=('red', 'blue'))
st.write('You selected wavelength between', start_color, 'and', end_color)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Inser a number')
st.write('Your number is',number)

import spacy as sp
import nltk 
import re
import streamlit.components.v1 as components
components.iframe("https://www.prothomalo.com/")






