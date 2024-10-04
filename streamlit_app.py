#importation of files

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import BEER  # Import the BEER module
import PPP  # Import the PPP module
import PEER
import FEER 



#import sklearn.ensemble import RandomForestClassifier

#Title of the work
st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')


# Create a navigation menu
page = st.sidebar.selectbox("Select a page", ["Home", "BEER", "PPP", "PEER", "FEER", "Google"])

# Define content for each page
if page == "Home":
    st.write("Welcome to the Home page! 🏠")
elif page == "BEER":
    st.write("Welcome to the BEER page! 🍺")
    BEER.app()  # This should call the `app()` function in BEER.py
elif page == "PPP":
    st.write("Welcome to the Purchasing Power Parity page! 💵")
    PPP.app()  # This should call the `app()` function in PPP.py
elif page == "PEER":
    st.write("Welcome to the PEER page! 👥")
    PEER.app()
elif page == "FEER":
    st.write("Welcome to the FEER page! 😱")
    FEER.app()
elif page == "Google":
    st.write("[Visit Google 🌎](http://www.google.com)")


with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv')
  data = df.drop(df.columns[13:], axis=1)
  data = data.drop(['BDC'], axis=1)
  data

#set metric
st.metric(label="Change in Exchange Rate", value =1587.39, delta=1.5, delta_color="normal")

tab1, tab2, tab3, tab4 = st.tabs(["Exchange rate and Inflation", "Exchange rate and Interest Rate", " Exchange rate and Differentials", "Exchange rate and Others"])

with tab1:
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

with tab2:
    tab2.write("Exchange rate and Interest rate")
    
    # Create figure and axes
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Bar plot for interest rates on the primary y-axis
    width = 0.4  # Width of the bars
    
    ax1.bar(data['Period'], data['INT_US'], width=width, label='INT_US', color='blue', alpha=0.7)
    ax1.bar(data['Period'], data['INT_NIG'], width=width, label='INT_NIG', color='orange', alpha=0.7, bottom=data['INT_US'])

    # Labels and title for the primary y-axis
    ax1.set_title('Exchange Rate and Interest Rates over Time')
    ax1.set_xlabel('Period')
    ax1.set_ylabel('Interest Rates (%)')
    ax1.legend(loc='upper left')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    # Secondary y-axis for EXR (Exchange Rate)
    ax2 = ax1.twinx()
    ax2.plot(data['Period'], data['EXR'], label='EXR', color='green', linewidth=3, marker='o')
    ax2.set_ylabel('Exchange Rate (₦)', color='green')  # Label for the secondary y-axis
    ax2.tick_params(axis='y', labelcolor='green')
    
    # Display the plot in Streamlit
    st.pyplot(fig)




data['INT1_Diff'] = data['INT_NIG'] - data['INT_US']
data['INF_Diff'] = data['INF_Nig'] - data['INF_US']

with tab3:
    tab3.write("Interest Rate and Inflation Differences along with Exchange Rate")
    
    # Create figure and axes
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plotting the differences on the primary y-axis
    ax1.plot(data['Period'], data['INT1_Diff'], label='Interest Rate Difference (INT_NIG - INT_US)', color='blue', linewidth=2, marker='o')
    ax1.plot(data['Period'], data['INF_Diff'], label='Inflation Difference (INF_Nig - INF_US)', color='orange', linewidth=2, marker='x')

    # Labels and title for the primary y-axis
    ax1.set_title('Interest Rate and Inflation Differences vs Exchange Rate')
    ax1.set_xlabel('Period')
    ax1.set_ylabel('Differences (%)')
    ax1.legend(loc='upper left')
    
    # Reduce x-axis labels for better clarity (showing every 5th label)
    ax1.set_xticks(data['Period'][::5])  # Show every 5th period
    plt.xticks(rotation=45)
    
    # Secondary y-axis for EXR (Exchange Rate)
    ax2 = ax1.twinx()
    ax2.plot(data['Period'], data['EXR'], label='Exchange Rate (₦)', color='green', linewidth=3, linestyle='--')
    ax2.set_ylabel('Exchange Rate (₦)', color='green')  # Label for the secondary y-axis
    ax2.tick_params(axis='y', labelcolor='green')
    
    # Display the plot in Streamlit
    st.pyplot(fig)


               

#Data Preparation
with st.sidebar: 
    st.header('Input features')
    Period = st.text_input("Write a date")
    INF_Nig = st.slider('Expected Inflation', 0.1, 50.0, 25.0)
    INF_US = st.slider('United States Inflation', 0.1, 20.0, 10.0) 
    NFA = st.slider('Net Foreign Asset', 5000000, 30000000, 10000000)
    EXPT = st.slider('Export', 500000, 30000000, 12000000)
    IMPT = st.slider('Import', 500000, 30000000, 12000000)
    COP = st.slider('Crude Oil Price', 10, 300, 150)
    EXR = st.slider('Exchange Rate', 100, 40000, 2000)
    INT_NIG = st.slider('Expected Interest Rate', 0.1, 50.0, 25.0)
    INT_US = st.slider('United States Interest Rate', 0.1, 50.0, 25.0)
    GXP = st.slider('Government Expenditure', 50000, 1000000, 500000)
    INT_DIFF = st.slider('Interest Rate Differential', 0.1, 50.0, 25.0) 


    data['Period'] = data['Period'].astype(str)
    #create data frame
    input= {
        'Period': Period,
        'INF_Nig': INF_Nig,
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
    input_penguins = pd.concat([input_df, data], axis=0)
    

# Display the input penguins DataFrame
with st.expander('Input features'):
    st.write('**Input penguins**')
    input
    st.write('**Combined penguins data**')
    input_penguins

input_row = input_penguins[:1]
y = input_penguins['EXR']
#Data Preparation        
with st.expander('Data Preparation'):
    st.write('**Input Penguin**')
    input_row
    st.write('**y**')
    y

#Model Training
#clf = RandomForestClassifier()
#clf.fit()
            

