import streamlit as st
import pandas as pd

st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')
With st.expander("Data"):
  st.write('**Rae data**)
  df = pd.read_csv('https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv')
  df
