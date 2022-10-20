import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

def from_paraquet(tab_name):
    df_read=pd.read_parquet('parquets/'+tab_name+'.parquet', engine='pyarrow')
    return df_read
