import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("vehicles_us.csv")
st.header('Análisis de Datos de Venta de Coches')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Gráfico de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión')
if scatter_checkbox:  # al marcar la casilla
    st.write('Gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")
    st.plotly_chart(fig_scatter, use_container_width=True)