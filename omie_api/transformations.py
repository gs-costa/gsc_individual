import pandas as pd

def select_columns(df, columns = []):
    df = df[columns]
    return df

def rename_columns(df, dict_rename = {}):
    df = df.rename(columns = dict_rename)
    return df

def drop_useless(df, drop_columns =[]):
    df.drop(
        drop_columns, 
        axis=1,
        inplace=True)
    return df