
import sqlite3
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import datetime
import pickle

app_mode = st.sidebar.selectbox('Select Page',['Home','Database table','Insertion'])

# conn = sqlite3.connect('loan.db')
# c = conn.cursor()

# loan = pd.read_csv('loan.csv')
# loan.to_sql('loan', conn, if_exists='append', index = False)

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn


if app_mode=='Home':
    st.header('Loan Application')
    st.image("loan.png")
    
elif app_mode=='Database table':

    conn= create_connection('lat.db')
    
    loan = pd.read_csv('loan.csv')
    loan.to_sql('loan', conn, if_exists='replace', index = False)
    st.markdown('Dataset')
    st.write(pd.read_sql('''SELECT * FROM loan''', conn))
    conn.close()

elif app_mode=='Insertion':
    
    conn= create_connection('lat.db')
    
    loan = pd.read_csv('loan.csv')
    loan.to_sql('loan', conn, if_exists='append', index = False)
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)

    with col1:
        v1= st.text_input('Loan_ID')

    with col2:
        v2= st.selectbox('Gender',['Male','Female'])

    with col3:
        v3= st.selectbox('Married',['Yes','No'])

    with col4:
       v4= st.slider('Dependents',0,5)

    with col5:
        v5= st.selectbox('Education', ['Graduate', 'Not Graduate'])

    with col6:
        v6= st.selectbox('Self_Employed', ['Yes','No'])

    with col7:
        v7= st.number_input('ApplicantIncome',0,1000000)

    with col8:
        v8= st.number_input('CoapplicantIncome',0,1000000)

    with col9:
        v9= st.number_input('LoanAmount',0,1000000)

    with col10:
        v10= st.number_input('Loan_Amount_Term',0,1000000)

    with col11:
        v11= st.number_input('Credit_History',0,1000000)

    with col12:
        v12= st.selectbox('Property_Area', ['Urban','Semiurban', 'Rural'])
    
    def predict():

        sample= pd.DataFrame([[v2 , v3 , v4 ,v5 ,v6, v7, v8 , v9 , v10, v11, v12]], 
                     columns= ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 
                                'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property_Area'])
        prediction = loaded_model.predict(sample)
        
        return prediction

    prediction_op = predict()
    
    if st.button('Predict'):
        
        #prediction = loaded_model.predict(sample)
        v13= st.text_input('Loan_Status', prediction_op[0])
   
    #v14= st.text_input('Loan_Status', prediction_op[0])
    
    if st.button('Insert'):
    
        query= '''INSERT INTO loan (Loan_ID, Gender, Married, Dependents, Education,\
                                    Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, \
                                    Property_Area, Loan_Status) \
                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        conn.execute(query,(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,prediction_op[0]))
    
        st.markdown('Inserted output')
        st.write(pd.read_sql('''SELECT * FROM loan''', conn))
    conn.commit()
    conn.close()
