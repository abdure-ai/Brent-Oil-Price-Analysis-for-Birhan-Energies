
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv(r"C:\Users\user\Projects\Brent-Oil-Price-Analysis-for-Birhan-Energies\data\proecessed\cleaned_brent_oil.csv")

st.title("Brent Oil Price Analysis Dashboard")

# Line chart for price trends
fig = px.line(df, x='Date', y='Price', title="Brent Oil Prices Over Time")
st.plotly_chart(fig)

st.write("### Summary Statistics")
st.write(df.describe())
