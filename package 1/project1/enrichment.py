#Adquisition web scraping + minicleaning of country in DF Population + Cleaning DF Population + Merge with DF Forbes
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

#Adquisition webscrap:
def web_to_scrap(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    return soup

def find_table(class_name):
    table = soup.find_all('table',{'class':{class_name}})[0]
    return table

def tags():
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p']
    text = [element.text for element in soup.find_all(tags)]


def rows(table):
    rows = table.find_all('tr')
    rows_parsed = [row.text for row in rows]
    return rows_parsed

def smart_parser(row_text):
    row_text = row_text.replace('World\nPopulation', 'World Population')
    row_text = row_text.replace('\n\n\n', '\n')
    row_text = row_text.replace('\n\n', '\n').strip('\n')
    row_text = re.sub('\[\d\]', '', row_text)
    return list(map(lambda x: x.strip(), row_text.split('\n')))

def well_parsed():
    well_parsed = list(map(lambda x: smart_parser(x), rows_parsed))
    return well_parsed

def web_df(well_parsed):
    colnames = well_parsed[0]
    data = well_parsed[1:]
    df = pd.DataFrame(data, columns=colnames)
    return df

def to_csv(df, folder, file):
    df.to_csv(f'../../../Ironhack-Module-1-Project-Mecaho/data/{folder}/{file}.csv', sep=',', index=False)
    print(f'{file}.csv file in path: "../../../Ironhack-Module-1-Project-Mecaho/data/{folder}" has been created')

#Minicleaning DF Population for Merge:
def drop_c(df, index):
    df = df.drop(df.index[index])
    return df

def append_row(df, new_row):
    df = df.append(pd.Series(new_row, index=df.columns),ignore_index=True)
    return df

def rename_c(df, old, new):
    df.rename(columns={old: new}, inplace=True)
    return df

def del_str_patt(df, col, del_str, new_str):
    df_enr[col] = df[col].apply(lambda x: re.sub(del_str, new_str, str(x))).str.strip()
    return df

#Cleaning:
def cast (df, col, type):
    df[col] = df[col].astype(type)
    return df

#Merge:
def merge(df, df_cln):
    dffull = dfforb.merge(dfpop, how='left', left_on='country', right_on='country')
    return df

if __name__=='__main__':
    def enrich(*args):
        web_to_scrap('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
        find_table('wikitable sortable mw-datatable')
        tags()
        rows()
        well_parsed()
        web_df('dfpop') 
        # Minicleaning dfpop
        df = drop_c(240)
        df = append_row(['–', 'World', "7,758,960,000", '100%', '4 Jan 2020', 'UN projection[200]'])
        df = rename_c('Country(or dependent territory)', 'country')
        df = rename_c('% of World Population', 'weight_wpopulation')
        df = rename_c('Rank', 'rank_pop')
        df = rename_c('Population', 'population')
        df = rename_c('Date', 'date')
        df = del_str_patt("country", '\([^()]*\)', '')
        df = del_str_patt("country", '\[[^\]]*\]', '')
        to_csv('dfpop', 'raw', 'dfpop1')
        #Cleaning:
        df = cast(df, 'population', int)
        df = del_str_patt(df, 'country', '\([^()]*\)', '')
        df = drop_c(df, 'Source')
        #Merge:
