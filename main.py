import streamlit as st
import plotly.express as px
import pandas as pd


# pick 3 variables to pull from csv and allow user to select what to plot on x/y axis

st.title("Happiness Data Correlation Visualizer")
x_option = st.selectbox("Select X-axis to plot: ", ("GDP", "Generosity", "Corruption"))
y_option = st.selectbox("Select Y-axis to plot: ", ("GDP", "Generosity", "Corruption"))

match x_option:
    case "GDP":
        x_data = [100,5045,700]
    case "Generosity":
        x_data = [80, 150, 300]
    case "Corruption":
        x_data = [55, 200, 310]

match y_option:
    case "GDP":
        y_data = [100,5045,700]
    case "Generosity":
        y_data = [80, 150, 300]
    case "Corruption":
        y_data = [55, 200, 310]


st.subheader(f"{x_option} and {y_option}")


figure = px.line(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)


# def get_data(days):
#     #temp data will get from weather data later
#     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures = [10,11,15]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures
#
# d, t = get_data(days)
#
# figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures (C)"})
# st.plotly_chart(figure)

