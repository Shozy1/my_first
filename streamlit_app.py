#importation of files

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Title of the work
st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')




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

with st.expander('Data Visualization'):
    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['EXR'], data['INF_US'], label='INF_US', alpha=0.5)
    plt.scatter(data['EXR'], data['INF_Nig'], label='INF_Nig', alpha=0.5)
    plt.title('Scatter Plot of INF_US and INF_Nig against EXR')
    plt.xlabel('EXR')
    plt.ylabel('Inflation Rates')
    plt.legend()
    
    # Display the plot in Streamlit
    st.pyplot(plt)
