import pandas as pd
import streamlit as st
import plotly.express as px

st.write('Por favor, selecciona un checkbox para mostrar un gráfico del conjunto de datos de anuncions de venta de coches:')        


car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')


if build_histogram: # si la casilla de verificación está seleccionada
    #Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches.')        
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
elif build_scatter:
    st.write('Creación de un gráfico despersión para el conjunto de datos de anuncios de venta de coches.')        
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)
    

    