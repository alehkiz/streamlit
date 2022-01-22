import pandas as pd
import requests
import datetime
import threading
from io import StringIO
from os import listdir, remove as remove_file
from os.path import isfile
from utils import format_date

file_folder = './files/'
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

file_name = f'data-covid-{today.strftime("%Y-%m-%d")}.csv'
current_file = file_folder +  file_name
th = None


def get_file():
    rq = requests.get(url)
    if rq.status_code != 200:
        raise Exception('Não foi possível acessar o arquivo')
    df = pd.read_csv(StringIO(rq.text))
    df = df[df['location'] == 'Brazil']
    df.reset_index(inplace=True, drop=True)
    df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
    df.drop(columns=['new_deaths_smoothed', 'total_cases_per_million',
       'new_cases_per_million', 'new_cases_smoothed_per_million',
       'total_deaths_per_million', 'new_deaths_per_million',
       'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients',
       'icu_patients_per_million', 'hosp_patients',
       'hosp_patients_per_million', 'weekly_icu_admissions',
       'weekly_icu_admissions_per_million', 'weekly_hosp_admissions',
       'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
       'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations',
       'people_vaccinated', 'people_fully_vaccinated', 'total_boosters',
       'new_vaccinations', 'new_vaccinations_smoothed',
       'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
       'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
       'new_vaccinations_smoothed_per_million',
       'new_people_vaccinated_smoothed',
       'new_people_vaccinated_smoothed_per_hundred', 'stringency_index',
       'population', 'population_density', 'median_age', 'aged_65_older',
       'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index',
       'excess_mortality_cumulative_absolute', 'excess_mortality_cumulative',
       'excess_mortality', 'excess_mortality_cumulative_per_million'], inplace=True)
    df.to_csv(file_folder+file_name, index=False)
    files = [_ for _ in listdir(path='./files/') if not file_name in _]
    if len(files) > 1:
        for file in files:
            remove_file(f'./files/{file}')


def get_dataframe():
    global th
    if not isfile(current_file):
        th = threading.Thread(target=get_file, name='Downloader')
        th.start()
    if len(listdir(path=file_folder)) == 0:
        return False
    file = file_folder + listdir(path=file_folder)[0]
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.sort_values(by=['date'], inplace=True, ascending=True)
    
    return df
def get_totals(df : pd.DataFrame):
    df = df.sort_values(by='date', ascending=False)
    total_deaths = df.iloc[0]['total_deaths']
    total_cases = df.iloc[0]['total_cases']
    return [total_cases, total_deaths]

def get_new(df : pd.DataFrame):
    df = df.sort_values(by='date', ascending=False)
    new_deaths = df.iloc[0]['new_deaths']
    new_cases = df.iloc[0]['new_cases']
    return [new_cases, new_deaths]