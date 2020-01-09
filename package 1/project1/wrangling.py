#Minicleaning of Country in DB Forbes + Cleaning of DB Forbes

import pandas as pd
import re
import numpy as np

#Minicleaning DF Forbes
def read_csv(folder, file):
    global df
    df = pd.read_csv(f'../../../Ironhack-Module-1-Project-Mecaho/data/{folder}/{file}.csv')
    return df

def drop_c(index):
    df = df.drop(df.index[index])
    return df

def replace(col, old_v, new_v):
    df[col] = df[col].str.strip().replace(old_v, new_v)
    return df

def to_csv(folder, file):
    df.to_csv(f'../../../Ironhack-Module-1-Project-Mecaho/data/{folder}/{file}.csv', sep=',', index=False)
    print(f'{file}.csv file in path: "../../../Ironhack-Module-1-Project-Mecaho/data/{folder}" has been created')

if __name__=='__main__':
    #def wrang(*args):
        read_csv('raw', 'dfforb')
        replace('country', 'USA', 'United States')
        replace('country', "People's Republic of China", 'China')
        replace('country', 'UK', 'United Kingdom')
        replace('country', 'Swaziland', 'Eswatini')
        replace('country', 'None', 'World')
        to_csv('raw', 'dfforb1')