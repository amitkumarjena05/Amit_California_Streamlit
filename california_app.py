import numpy as np
import joblib
import streamlit as st
obj=joblib.load('california.joblib')
model=obj['model']
cols=obj['columns']

st.title('California app')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} value:')
    In.append(v)
if st.button('click'):
    Input=np.array([In])
    out=model.predict(Input)
    st.success(f'The median House value is:{out}')