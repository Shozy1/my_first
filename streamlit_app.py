import streamlit as st
import pandas as pd
import numpy as np
st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')

import streamlit as st

# Create a navigation menu
page = st.sidebar.selectbox("Select a page", ["Home", "BEER", "Purchasing Power Parity", "PEER", "FEAR", "Google"])

# Define content for each page
if page == "Home":
    st.write("Welcome to the Home page! 🏠")
elif page == "BEER":
    st.write("Welcome to the BEER page! 🍺")
elif page == "Purchasing Power Parity":
    st.write("Welcome to the Purchasing Power Parity page! 💵")
elif page == "PEER":
    st.write("Welcome to the PEER page! 👥")
elif page == "FEAR":
    st.write("Welcome to the FEAR page! 😱")
elif page == "Google":
    st.write("[Visit Google 🌎](http://www.google.com)")


with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv')
  data = df.drop(df.columns[13:], axis=1)
  data = data.drop(['BDC'], axis=1)
  data

data = pd.DataFrame({
    "period": range(175),  # Example 'period' data from 0 to 174
    "EXR": range(175),  # Replace with your actual EXR data
    "INF_Nig": range(175),  # Replace with your actual INF_Nig data
    "INF_US": range(175)  # Replace with your actual INF_US data
})

st.line_chart(data.set_index("period"))
