import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

#Functions:
def web_to_scrap(url):
    global soup
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")

def find_table(class_name):
    global table
    table = soup.find_all('table',{'class':{class_name}})[0]

def tags(*args):
    global text
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p']
    text = [element.text for element in soup.find_all(tags)]

def rows(*args):
    global rows_parsed
    rows = table.find_all('tr')
    rows_parsed = [row.text for row in rows]

def smart_parser(row_text):
    row_text = row_text.replace('World\nPopulation', 'World Population')
    row_text = row_text.replace('\n\n\n', '\n')
    row_text = row_text.replace('\n\n', '\n').strip('\n')
    row_text = re.sub('\[\d\]', '', row_text)
    return list(map(lambda x: x.strip(), row_text.split('\n')))

def well_parsed():
    global well_parsed
    well_parsed = list(map(lambda x: smart_parser(x), rows_parsed))

def enrich()
#if __name__=='__main__':
    web_to_scrap('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    find_table('wikitable sortable mw-datatable')
    tags()
    rows()
    well_parsed()
