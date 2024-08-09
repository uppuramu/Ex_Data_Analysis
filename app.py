import streamlit as st
import pandas as pd


# Set the title of the Streamlit app
st.title("Exploratory Data Analysis (EDA) App with Interactive Buttons")

# File uploader to upload the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Initialize session state to track button clicks
if 'show_overview' not in st.session_state:
    st.session_state['show_overview'] = False

if 'show_basic_info' not in st.session_state:
    st.session_state['show_basic_info'] = False

if 'show_summary_stats' not in st.session_state:
    st.session_state['show_summary_stats'] = False

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Button to show Dataset Overview
    if st.button("Show Dataset Overview"):
        st.session_state['show_overview'] = True

    if st.session_state['show_overview']:
        st.subheader("Dataset Overview")
        st.write(df.head())

    # Button to show Basic Information
    if st.button("Show Basic Information"):
        st.session_state['show_basic_info'] = True

    if st.session_state['show_basic_info']:
        st.subheader("Basic Information")
        st.write("Number of rows:", df.shape[0])
        st.write("Number of columns:", df.shape[1])
        st.write("Data types:")
        st.write(df.dtypes)

    # Button to show Summary Statistics
    if st.button("Show Summary Statistics"):
        st.session_state['show_summary_stats'] = True

    if st.session_state['show_summary_stats']:
        st.subheader("Summary Statistics")
        st.write(df.describe())

else:
    st.write("Please upload a CSV file to begin the analysis.")
