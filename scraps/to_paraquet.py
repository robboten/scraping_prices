import pyarrow as pa
import pyarrow.parquet as pq

def to_paraquet(tab_name,df_obj):
    table=pa.Table.from_pandas(df_obj)
    pq.write_table(table,'parquets/'+tab_name+'.parquet')
    return table
