import streamlit as st
import numpy as np
import pandas as pd
from core import get_dataframe, get_totals
from utils import format_date

df = get_dataframe()
if not df is False:

    df = df.sort_values(by='date', ascending=False)
    print(df.iloc[0]['date'])
    date = df.iloc[0]['date'].strftime('%d/%m/%Y')
    cases, deaths = get_totals(df)
    st.title(f'Covid Dados {date}')

    col1, col2 = st.columns(2)
    col1.metric("Total de casos", f'{int(cases):,d}'.replace(',','.'), '')
    col2.metric("Total de mortos", f'{int(deaths):,d}'.replace(',','.'), '')

else:
    st.title('Dados sendo carregados...')
    st.button("Atualizar")

    



