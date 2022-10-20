import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

def get_sek():
    df_currency=from_paraquet('currency_prices')
    return df_currency.tail(1)['OBS_VALUE'].values[0]

def from_paraquet(tab_name):
    df_read=pd.read_parquet('parquets/'+tab_name+'.parquet', engine='pyarrow')
    return df_read

def to_paraquet(tab_name,df_obj):
    table=pa.Table.from_pandas(df_obj)
    pq.write_table(table,'parquets/'+tab_name+'.parquet')
    return table
