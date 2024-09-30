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
    # Create a figure and a set of subplots
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plotting INF_US and INF_Nig on the primary y-axis
    ax1.scatter(data['Period'], data['INF_US'], label='INF_US', alpha=0.5, color='blue')
    ax1.scatter(data['Period'], data['INF_Nig'], label='INF_Nig', alpha=0.5, color='orange')
    
    # Labels and title for the primary y-axis
    ax1.set_title('Scatter Plot of Inflation Rates against Period')
    ax1.set_xlabel('Period')
    ax1.set_ylabel('Inflation Rates')
    ax1.legend(loc='upper left')

    # Creating a secondary y-axis for EXR
    ax2 = ax1.twinx()
    ax2.plot(data['Period'], data['EXR'], label='EXR', color='green', linewidth=2)
    ax2.set_ylabel('EXR', color='green')  # Label for the secondary y-axis
    ax2.tick_params(axis='y', labelcolor='green')

    # Display the plot in Streamlit
    st.pyplot(fig)
    
   
