# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:23:15 2024

@author: HP
"""
 
import numpy as np
import streamlit as st
import pickle

lr=pickle.load(open('D:/Data Files Copy/Loan_data/trained_Loan_Model.sav','rb'))
def Predict(input_data):
#CHANGE THE INPUT DATA INTO ARRAY AND ITS IN TUPLE RIGHT NOW
    input_data_numpy=np.asarray(input_data)
#RESHAPE THE NUMPY ARRAY AS WE ARE PREDICTION ONLY ONE DATA POINT
    reshaped_data=input_data_numpy.reshape(1,-1)
    prediction=lr.predict(reshaped_data)
    if(prediction==1):
        return("Your Loan is approved")
    else:
        return("Sorry your Loan is not approved") 
        
def main():
    st.title("Loan Application Form")

    # Header
    st.header("Personal Information")
    # Input fields for personal information
    i1 = st.number_input("Married?")
    i2 = st.number_input("Dependents?")
    i3 = st.number_input("Education?")
    i4 = st.number_input("Self Employed?")
    i5 = st.number_input("Applicant Income?")
    i6 = st.number_input("Coapplicant Income?")
    i7 = st.number_input("Loan Amount(lk)?")
    i8 = st.number_input("Loan Amount Term?")
    i9 = st.number_input("Credit History?")
    i10 = st.number_input("Property Area?")


    # Header for Loan Details
    st.header("Loan Details")

   
 
   
    
    checking=""
    if st.button("Click Me!!"):
        checking = Predict([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10])
    st.success(checking)  
    
if __name__=='__main__':
    main()         