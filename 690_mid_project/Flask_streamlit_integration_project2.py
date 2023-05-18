
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import datetime

app_mode = st.sidebar.selectbox('Select Page',['Home','Dataset','Visualization','Insights'])

if app_mode=='Home':
    st.header('NYC Flight Data Analysis')
    st.image("flight.png")

elif app_mode=='Dataset':
    file= st.file_uploader('upload the file', type=['csv'])

    if file is not None:
        df= pd.read_csv(file)
        st.subheader("Dataset")
        st.dataframe(df)
        Exploration_type = st.radio('Explore Dataset', ['Dataset summary','Dataset shape', 'Dataset columns', 'Nulls in Dataset'], horizontal=True)
        
        if Exploration_type == 'Dataset summary':
            st.markdown('Dataset summary statistics')
            st.write(df.describe())
        elif Exploration_type == 'Dataset shape':
            st.markdown('Dataset shape')
            st.write(df.shape)
        elif Exploration_type == 'Dataset columns':
            st.markdown('Dataset columns')
            st.write(df.columns)
        else:
            st.markdown('Nulls in Dataset')
            st.write(df.isnull().sum())

elif app_mode=='Insights':
    dp=pd.read_csv('flight_data.csv')
    da= pd.read_csv("nyc_airlines.csv")
    df= pd.merge(dp, da, on= 'carrier', how= 'left')
    df.rename(columns={'name': 'carrier_name'}, inplace= True)
    df.dropna(axis=0,how ='any', inplace=True)


    st.subheader('Insights of NYC Flight dataset')

    index = sorted(df.columns.unique())
    
    default_index_col1 = index.index('carrier_name')
    default_index_col2 = index.index('dep_delay')

    first_col= st.selectbox('column1',index, index= default_index_col1)
    second_col= st.selectbox('column2',index, index= default_index_col2)
    
    stats= st.radio('statistics', ['Count','Avg', 'Max', 'Min'])

  
    if stats=='Count':
        st.write('Count')
        st.write(df.groupby([first_col])[second_col].count().sort_values(ascending= False).reset_index())
      
    elif stats=='Avg':
         st.write('Average')
         st.write(df.groupby([first_col])[second_col].mean().sort_values(ascending= False).reset_index())

    elif stats=='Max':
         st.write('Maximum')
         st.write(df.groupby([first_col])[second_col].max().sort_values(ascending= False).reset_index()) 
    
    else:
         st.write('Minimum')
         st.write(df.groupby([first_col])[second_col].min().sort_values(ascending= False).reset_index()) 


else:
  dp=pd.read_csv('flight_data.csv')
  da= pd.read_csv("nyc_airlines.csv")
  df= pd.merge(dp, da, on= 'carrier', how= 'left')
  df.rename(columns={'name': 'carrier_name'}, inplace= True)
  df.dropna(axis=0,how ='any', inplace=True)

  st.sidebar.header("User Inputs for Visualizations")
  plot_type = st.sidebar.selectbox('Graph',['Histogram','Barchart','Piechart','Boxplot'])
  index = sorted(df.columns.unique())

  # Setting default value for x, y, and color
  default_index_x = index.index('origin')
  default_index_y = index.index('air_time')
  default_index_col = index.index('origin')    
  
  x_label = st.sidebar.selectbox("X label Parameter", index, index= default_index_x)
  y_label = st.sidebar.selectbox("Y label Parameter", index, index= default_index_y)
  color= st.sidebar.selectbox("Color", index, index= default_index_col)


  
  dt= df.groupby([x_label])[y_label].mean().sort_values(ascending= False).reset_index() 
  dp= df[x_label].value_counts().sort_values(ascending= False).reset_index()


  if st.sidebar.button('Plot'):
      if plot_type== 'Histogram':
          st.write(plot_type)
          plot= px.histogram(df,x=x_label, color= color, title='Frequency distribution of '+x_label)
          st.plotly_chart(plot)

      elif plot_type== 'Barchart': 
          st.write(plot_type)
          plot= px.bar(dt, x=x_label, y=y_label, color= color,title='Barchart of '+x_label+' vs avg '+y_label)
          st.plotly_chart(plot)
          
      elif plot_type== 'Boxplot': 
          st.write(plot_type)
          plot= px.box(df, x=x_label, y=y_label, color=color, title= 'Boxplot of '+x_label+' vs avg '+y_label)
          st.plotly_chart(plot)
      
      else:
          
          st.write(plot_type)
          plot= px.pie(dp, values=x_label, names='index', color=color, title='Piechart shows % '+x_label)
          st.plotly_chart(plot) 



