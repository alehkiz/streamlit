import streamlit as st
import numpy as np
import pandas as pd
from core import get_dataframe, get_totals

df = get_dataframe()
cases, deaths = get_totals(df)
st.title('Covid Dados')

col1, col2 = st.columns(2)
col1.metric("Total de casos", f'{int(cases):,d}'.replace(',','.'), '')
col2.metric("Total de mortos", f'{int(deaths):,d}'.replace(',','.'), '')





