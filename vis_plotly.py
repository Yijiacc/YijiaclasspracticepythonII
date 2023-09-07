plotly==5.14.1
plotly-express==0.4.1
seaborn==0.12.2
matplotlib==3.7.1
joblib==1.1.1
Pillow==9.5.0
streamlit==1.21.0
pandas==1.5.3
pandas-profiling==3.2.0
scikit_learn==1.2.2
numpy==1.24.2

import streamlit as st
import pandas as pd
import numpy as np

#now we import for the first time Plotly
import plotly.express as px

st.header('Lets start to play with Plotly:teddy_bear:')

#we read the same data as before
data=pd.read_csv('tips.csv')

st.markdown('---')

st.subheader('Draw an histogram for the total bill')

fig=px.histogram(data_frame=data, x='total_bill')
st.plotly_chart(fig)

st.markdown('---')

st.subheader("Draw histogram for total bill and color by sex")

fig=px.histogram(data_frame=data, x='total_bill', color='sex')
st.plotly_chart(fig)

st.markdown('---')

st.subheader('Draw histogram for total bill and color by sex,smoker,day or time')

select=st.selectbox('Select the category you want to color', 
					('sex','smoker','day','time'))
fig=px.histogram(data_frame=data, x='total_bill', color=select)
st.plotly_chart(fig)

st.markdown('---')

st.subheader('Draw Scatter Plot for total bill and tips and color by sex,smoker,day or time')

color_option=st.selectbox('Select the category you to color', 
					('sex','smoker','day','time'))
fig=px.scatter(data_frame=data, x='total_bill', y='tip',color=color_option)
st.plotly_chart(fig)

st.markdown('---')

st.subheader('Draw Sunburst Chart on features: sex,smoker,day and time')

path=st.multiselect('Select the categorical features path', 
					('sex','smoker','day','time'))
fig=px.sunburst(data_frame=data, path=path)
st.plotly_chart(fig)







