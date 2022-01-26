import streamlit as st
import pandas as pd
from core import analysis_by_country, get_dataframe, get_totals, get_new, populate_diary_evolution, populate_metrics, add_date_picker
from utils import format_date
import datetime

df = get_dataframe()

st.set_page_config(
    page_title='Dados Covid',
    page_icon='📈',
    layout="wide",
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
    df = df.sort_values(by='date', ascending=True)
    date = df.iloc[-1]['date'].strftime('%d/%m/%Y')
    print(date)
    st.sidebar.title(f'Dados Covid - Atualizado em {date}')
    menu = st.sidebar.selectbox(
     'Selecione a página:',
     ['Consolidado',
        'Evolução diária',
        'Análise por páís'])

    countries = sorted(df['country_pt'].unique().tolist())
    st_contries = st.sidebar.multiselect(label='Países', options= countries, help='Deseja analisar algum país específico, selecione um ou mais logo abaixo')
    if not not st_contries:
        df = df[df['country_pt'].isin(st_contries)]
    df = add_date_picker(df)
    if menu == 'Consolidado':
        populate_metrics(df)
    elif menu =='Evolução diária':
        populate_diary_evolution(df)
    elif menu == 'Análise por páís':
        analysis_by_country(df, date)
    
    st.sidebar.markdown('----')
    st.sidebar.markdown('Dados extraídos de [Our World in Data](https://ourworldindata.org/coronavirus)')
    
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")