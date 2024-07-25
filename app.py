import pandas as pd
import plotly.express as px 
import streamlit as st

st.header('Graficas de datos de anuncios de venta de coches')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')
hist_button_2 = st.button('Construir grafico de dispersion')

if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='model_year')
    st.plotly_chart(fig, use_container_width=True)
    
if hist_button_2:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig_2 = px.scatter(car_data, x='model', y= 'price')
    st.plotly_chart(fig_2)