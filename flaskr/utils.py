import pandas as pd
import os

def create_column():
    df = pd.read_csv(os.path.join(os.getcwd(), 'data/data.csv'))
    column_names = list(df.columns)

    return column_names

def read_dataset():
    return pd.read_csv(os.path.join(os.getcwd(), 'data/data.csv'))


"""
    This function is used to add data to database and testing
    Don't use this function
"""

def assistant():
    col_names = create_column()
    str = ""
    for i in col_names:
        i = i.replace(',', '')
        i = i.replace(':', '')
        i = i.replace(' / ', '_')
        i = i.replace('/', '_')
        i = i.replace(' ', '_')
        i = i.replace('-', '_')
        str += f'self.{i} = data.get(\'{i}\')'
        str += "\n"

    print(str)

