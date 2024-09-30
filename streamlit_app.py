import streamlit as st
import pandas as pd

st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')

st.page_link("your_app.py", label="Home", icon="🏠")  # Home icon is fine.
st.page_link("pages/BEER.py", label="BEER", icon="🍺")  # Beer mug icon for BEER.
st.page_link("pages/PPP.py", label="Purchasing Power Parity", icon="💵")  # Money icon for PPP.
st.page_link("pages/PEER.py", label="PEER", icon="👥")  # Two people icon for PEER (peer comparison).
st.page_link("http://www.google.com", label="Google", icon="🌍")  # Globe icon is fine for Google.
st.page_link("pages/FEAR.py", label="FEAR", icon="😱")

with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv')
  data = df.drop(df.columns[13:], axis=1)
  data = data.drop(['BDC'], axis=1)
  data



