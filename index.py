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
    df = df.sort_values(by='date', ascending=False)
    st_contries = st.multiselect(label='Países', options= countries, help='Selecione um ou mais países')
    if not not st_contries:
        df = df[df['country_pt'].isin(st_contries)]
    # st_contries = st.multiselect(label='Países', options= countries, help='Selecione um ou mais países')
    # if not not st_contries:
    #     df = df[df['country_pt'].isin(st_contries)]
    # 
    # dates = [pd.to_datetime(_).date() for _ in df['date'].unique()]
    
    # min_value=df.iloc[-1]['date']
    # max_value=df.iloc[0]['date']
    # c1, c2 = st.columns(2)
    # init_date = c1.date_input("Data inicial", min_value)
    # end_date = c2.date_input('Data final', max_value)
    # df = df[(df['date'] >= pd.to_datetime(init_date)) & (df['date'] <= pd.to_datetime(end_date))]
    populate_metrics(df)

    df = add_date_picker(df)
    populate_graphics(df)
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")

    



