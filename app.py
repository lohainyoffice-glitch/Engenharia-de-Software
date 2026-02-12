import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Criar histograma')
title = st.title('Análise de anúncios de venda de carros')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(car_data, x = 'odometer')

    st.plotly_chart(fig, use_container_width=True)



scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para um conjunto de anúncios de vendas de carros de acordo com ano do modelo e valor.')
    
    fig = px.scatter(car_data, x="model_year", y="price")
    
    st.plotly_chart(fig, use_container_width=True)
    