import streamlit as st
import pandas as pd
from core import get_dataframe, get_totals, get_new
from utils import format_date

df = get_dataframe()
if not df is False:

    df = df.sort_values(by='date', ascending=False)
    date = df.iloc[0]['date'].strftime('%d/%m/%Y')
    cases, deaths = get_totals(df)
    new_cases, new_deaths = get_new(df)
    st.title(f'Covid Dados')
    st.header(f'Atualizado em {date}')

    c_new_cases, c_new_deaths = st.columns(2)
    st.markdown("""---""")
    c_total_cases, c_total_deaths = st.columns(2)
    c_total_cases.metric("Total de casos", f'{int(cases):,d}'.replace(',','.'), '')
    c_total_deaths.metric("Total de mortos", f'{int(deaths):,d}'.replace(',','.'), '')
    
    c_new_cases.metric('Novos casos', f'{int(new_cases):,d}'.replace(',','.'),'')
    c_new_deaths.metric('Novas mortes', f'{int(new_deaths):,d}'.replace(',','.'),'')
else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")

    



