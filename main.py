import streamlit as st
import plotly.express as px
import pandas as pd


# pick 3 variables to pull from csv and allow user to select what to plot on x/y axis
df = pd.read_csv("happy.csv")

st.title("Happiness Data Correlation Visualizer")
x_option = st.selectbox("Select X-axis to plot: ", ("happiness","gdp","social_support","life_expectancy","freedom_to_make_life_choices","generosity","corruption"))
y_option = st.selectbox("Select Y-axis to plot: ", ("happiness","gdp","social_support","life_expectancy","freedom_to_make_life_choices","generosity","corruption"))

x_data = df[x_option]
y_data = df[y_option]

st.subheader(f"{x_option} and {y_option}")

figure = px.scatter(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)



