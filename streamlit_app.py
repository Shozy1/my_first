import streamlit as st
import pandas as pd

st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')
with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv')
  data = df.drop([BDC, 13: ] axis=1)
