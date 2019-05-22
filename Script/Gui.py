import pandas as pd
from tkinter import *
from Work.Library import functions

base = pd.read_csv('/home/polina/Work/Data/laptops.csv', encoding='latin1', index_col='Unnamed: 0')

notebooks = functions.df_to_dict(base)
print(notebooks)