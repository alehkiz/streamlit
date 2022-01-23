from pyparsing import col
import streamlit as st
import pandas as pd
from core import get_dataframe, get_totals, get_new
from utils import format_date

df = get_dataframe()
def populate_metrics(df : pd.DataFrame):
    date = df.iloc[0]['date']
    cases, deaths = get_totals(df, date)
    new_cases, new_deaths = get_new(df, date)
    
    st.title(f'Dados Covid - Atualizado em {date.strftime("%d/%m/%Y")}')
    st.header(f'Consolidado')
    c_new_cases, c_new_deaths = st.columns(2)
    st.markdown("""---""")
    c_total_cases, c_total_deaths = st.columns(2)
    c_total_cases.metric("Total de casos", f'{int(cases):,d}'.replace(',','.'), '')
    c_total_deaths.metric("Total de mortos", f'{int(deaths):,d}'.replace(',','.'), '')
    
    c_new_cases.metric('Novos casos', f'{int(new_cases):,d}'.replace(',','.'),'')
    c_new_deaths.metric('Novas mortes', f'{int(new_deaths):,d}'.replace(',','.'),'')

def populate_graphics(df : pd.DataFrame):
    # df = df.groupby(["date"], as_index=False)['new_deaths'].sum()
    # df.set_index('date', inplace=True)
    # df = df.rename({'new_deaths':'Mortes'}, axis=1)
    # st.markdown("""---""")
    # st.header('Evolução de mortes por dia')
    # st.bar_chart(df)

    deaths_df = df.groupby(["date"], as_index=False)['new_deaths'].sum()
    deaths_df.set_index('date', inplace=True)
    deaths_df.rename({'new_deaths':'Mortes'}, axis=1, inplace=True)
    st.markdown("""---""")
    st.header('Evolução de mortes por dia')
    st.bar_chart(deaths_df)
    
    cases_df = df.groupby(["date"], as_index=False)['new_cases'].sum()
    cases_df.set_index('date', inplace=True)
    cases_df.rename({'new_cases':'Casos'}, axis=1, inplace=True)
    st.markdown("""---""")
    st.header('Evolução de casos por dia')
    st.bar_chart(cases_df)


if not df is False:
    df.fillna(0, inplace=True)
    countries = df['location'].unique().tolist()
    st_contries = st.multiselect(label='Países', options= countries, help='Selecione um ou mais países')
    if not not st_contries:
        df = df[df['location'].isin(st_contries)]
    df = df.sort_values(by='date', ascending=False)
    populate_metrics(df)
    populate_graphics(df)
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")

    



