#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height/100) ** 2
    return bmi

st.title('BMI Calculator')
weight = st.number_input('Enter your weight (kg):', min_value=1.0, step=0.1)
height = st.number_input('Enter your height (cm):', min_value=1.0, step=0.1)

if st.button('Calculate BMI'):
    bmi = calculate_bmi(weight, height)
    st.write(f'Your BMI is {bmi:.2f}')
    
    if bmi < 18.5:
        st.write('You are underweight.')
    elif 18.5 <= bmi < 24.9:
        st.write('You have a normal weight.')
    elif 25 <= bmi < 29.9:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')


# In[ ]:




