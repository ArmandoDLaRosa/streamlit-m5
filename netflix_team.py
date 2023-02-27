import streamlit as st
import pandas as pd
import numpy as np
import codecs


DATA_URL = ('movies.csv')
st.title("Realiza una búsqueda de película")

@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    return pd.read_csv(doc, nrows=nrows)

def filter_by_title(title):
    filtered_data = data[data['name'].str.upper().str.contains(title)]
    return filtered_data

def filter_by_director(name):
    filtered_data = data[data['director'] == name]
    return filtered_data


load_state = st.text('Cargando la DB de netflix...')
data = load_data(500)
load_state.text('¿Qué peli quieres buscar?')

# -----------------------------------------------------------
# DASHBOARD
# -----------------------------------------------------------

#   Checkbox
if st.sidebar.checkbox('Listar todo'):
    st.subheader('Todas las películas')
    st.write(data)

#    Search Button (Title)
title_input = st.sidebar.text_input('Título de la película:')
search_button = st.sidebar.button('Buscar película')    
if (search_button):
   st.write(f"Filtrado por Título")
   filtered = filter_by_title(title_input.upper())
   st.write(filtered)

#    Dropdown (Director's Name)
director_name = st.sidebar.selectbox("Nombre del director", data['director'].unique())
dropdown = st.sidebar.button('Filtrar por nombre')
if (dropdown):
   st.write(f"Filtrado por Director")
   filtered = filter_by_director(director_name)
   st.dataframe(filtered)