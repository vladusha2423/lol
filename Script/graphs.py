import pandas as pd
import matplotlib
from Library import functions as fun
import matplotlib.pyplot as plt

base = pd.read_csv('laptops.csv', encoding='latin1', index_col='Unnamed: 0')
notebooks = fun.df_to_dict(base)


def create_graphs(dct, specificaton):
    if specificaton == "Company":
        matplotlib.rcParams['figure.figsize'] = [15, 12]
    if specificaton == "TypeName":
        matplotlib.rcParams['figure.figsize'] = [11, 6]
    if specificaton == "Inches":
        matplotlib.rcParams['figure.figsize'] = [21, 8]
    if specificaton == "OpSys":
        matplotlib.rcParams['figure.figsize'] = [11, 8]
    x = fun.unique_specifications(notebooks, specificaton)
    y = [fun.aver_prices(notebooks, specificaton)[i] for i in x]
    print(len(x))
    fig, ax = plt.subplots()
    if specificaton != "Inches":
        ax.bar(x, y)
    else:
        ax.bar(x, y, width=0.07)
    plt.show()
    return 0

