import pandas as pd
from datetime import date, timedelta

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

def change_status(df):
    df_change = df.query('status == "ATRASADO"')
    df_unchange = df.query('status != "ATRASADO"')
    today_date = date.today()
    td = timedelta(-3)
    for i in range(len(df_change)):
        data_vencimento = list(map(int, df_change.iloc[i]['dt_vencimento'].split('/')))
        dt_vencimento = date( 
            data_vencimento[2],
            data_vencimento[1],
            data_vencimento[0])
        if  dt_vencimento >= today_date+td:
            df_change.iloc[i]['status'] = 'Vence hoje (D+1) (boleto gerado)'
    df = pd.concat([df_change,df_unchange])
    
    return df