from pyparsing import col
import streamlit as st
import pandas as pd
from core import get_dataframe, get_totals, get_new, populate_graphics, populate_metrics, add_date_picker
from utils import format_date
import datetime

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
    df = df.sort_values(by='date', ascending=True)
    st_contries = st.multiselect(label='Países', options= countries, help='Selecione um ou mais países')
    if not not st_contries:
        df = df[df['country_pt'].isin(st_contries)]
    populate_metrics(df)

    df = add_date_picker(df)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
    # st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

    mean = st.radio(
     "Informe a média diária",
     (7,14,28))
    populate_graphics(df, mean=mean)
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")