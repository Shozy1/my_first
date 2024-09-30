#importation of files

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openai 



import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_interpretation(data_description):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model you want to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": data_description}
        ]
    )
    return response['choices'][0]['message']['content']




#Title of the work
st.title('Forcasting External Sector Variables')

st.info('Become an External Sector Expert')

# Set your OpenAI API key
openai.api_key = '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'


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
    
   # Function to generate AI interpretation
def get_interpretation(data_description):
    prompt = f"Based on the following data description, provide an interpretation: {data_description}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

# Collecting the description for interpretation
data_description = "This chart displays inflation rates (INF_Nig and INF_US) and exchange rates (EXR) over a specified period."
if st.button('Get AI Interpretation'):
    interpretation = get_interpretation(data_description)
    st.write("AI Interpretation:")
    st.write(interpretation)
