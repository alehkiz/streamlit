from pyparsing import col
import streamlit as st
import pandas as pd
from core import get_dataframe, get_totals, get_new, populate_graphics, populate_metrics
from utils import format_date

df = get_dataframe()

st.set_page_config(
    page_title='Dados Covid',
    page_icon='📈',
    layout="wide",
     initial_sidebar_state="expanded"
    )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#TODO: Traduzir os nomes dos países
if not df is False:
    df.fillna(0, inplace=True)
    countries = df['country_pt'].unique().tolist()
    
    st_contries = st.multiselect(label='Países', options= countries, help='Selecione um ou mais países')
    if not not st_contries:
        df = df[df['country_pt'].isin(st_contries)]
    df = df.sort_values(by='date', ascending=False)
    populate_metrics(df)
    populate_graphics(df)
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")

    



