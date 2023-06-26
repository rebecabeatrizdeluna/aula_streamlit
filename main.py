import streamlit as st
import yfinance as yf
import plotly.graph_objects as go 

# Título do App 
st.title('Stock History App')

# Criação de uma barra lateral (sidebar)
st.sidebar.title('Selecione o Stock')
ticker_symbol = st.sidebar.text_input('stock', 'APL', max_chars=10)

# Baixando dados do yahoo finanças
data = yf.download(ticker_symbol, start='2020-01-01', end = '2023-06-26')

# Exibir os dados 
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico 
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y = data['Close'], name = 'fechamento'))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "Data", yaxis_title = "Preço")
st.plotly_chart(fig)