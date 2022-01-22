import pandas as pd

def get_dataframe():
    df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-20-2022.csv')

    df.drop(columns=['FIPS', 'Admin2'], inplace=True)

    df_br = df[df['Country_Region'] == 'Brazil']

    return df_br

def get_totals(df : pd.DataFrame):
    total_deaths = df.Deaths.sum()
    total_cases = df.Confirmed.sum()
    return [total_cases, total_deaths]
