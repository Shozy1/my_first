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



#Data Preparation
with st.sidebar: 
    st.header('Input features')
    INF_Nig = st.slider('Expected Inflation', 0.1, 50.0, 25.0)
    INF_US = st.slider('United States Inflation', 0.1, 20.0, 10.0) 
    NFA = st.slider('Net Foreign Asset', 5000000, 30000000, 10000000)
    EXPT = st.slider('Export', 500000, 30000000, 12000000)
    IMPT = st.slider('Import', 500000, 30000000, 12000000)
    COP = ('Crude Oil Price', 10, 300, 150)
    EXR = ('Exchange Rate', 100, 40000, 2000)
    INT_NIG = st.slider('Expected Interest Rate', 0.1, 50.0, 25.0)
    INT_US = st.slider('United States Interest Rate', 0.1, 50.0, 25.0)
    GXP = st.slider('Government Expenditure', 50000, 1000000, 500000)
    INT_DIFF = st.slider('Interest Rate Differential', 0.1, 50.0, 25.0) 


    
    #create data frame
    input= {'INF_Nig': INF_Nig,
            'INF_US': INF_US, 
            'NFA': NFA,
            'EXPT': EXPT,
            'IMPT': IMPT,
            'COP': COP,
            'EXR': EXR,
            'INT_NIG': INT_NIG,
            'INT_US': INT_US,
            'GXP': GXP,
            'INT_DIFF': INT_DIFF}
    input_df = pd.DataFrame(input, index=[0])
    
    # Assuming 'X' is defined elsewhere in your code
    # Make sure X is defined before concatenation
    try:
        input_penguins = pd.concat([input_df, data], axis=0)
    except NameError:
        st.error("Variable 'X' is not defined. Please ensure it's defined before this code.")

# Display the input penguins DataFrame
st.write(input_penguins)
            
            
    
            

