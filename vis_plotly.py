pip install plotly

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







