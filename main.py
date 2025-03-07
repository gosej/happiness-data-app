import streamlit as st
import plotly.express as px
import pandas as pd


# read csv
df = pd.read_csv("happy.csv")

st.title("Happiness Data Correlation Visualizer")
# x_option = st.selectbox("Select X-axis to plot: ", ("happiness","gdp","social_support","life_expectancy","freedom_to_make_life_choices","generosity","corruption"))
# y_option = st.selectbox("Select Y-axis to plot: ", ("happiness","gdp","social_support","life_expectancy","freedom_to_make_life_choices","generosity","corruption"))

x_option = st.selectbox("Select X-axis to plot: ", ("Happiness","GDP","Social Support","Life Expectancy","Freedom to Make Life Choices","Generosity","Corruption"))
y_option = st.selectbox("Select Y-axis to plot: ", ("Happiness","GDP","Social Support","Life Expectancy","Freedom to Make Life Choices","Generosity","Corruption"))


#modying the x/y_option format to match csv column names
x_data = df[x_option.lower().replace(' ','_')]
y_data = df[y_option.lower().replace(' ','_')]

st.subheader(f"{x_option} and {y_option}")

figure = px.scatter(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)



