import requests
import pandas as pd
import pyarrow.parquet as pq
import scr_utils as scru

def get_steam_games_list():
    #read stored nr rows
    steam_pq_rows=pq.read_metadata('parquets/steam_games_list.parquet').num_rows

    #get list of games from steam
    steamAppsResponse = requests.get(
        "https://api.steampowered.com/ISteamApps/GetAppList/v2/")

    steamApps = steamAppsResponse.json()
    steamApps = steamApps['applist']['apps']

    steam_df=pd.json_normalize(steamApps)

    #get rows from online steam list
    steam_df_rows=len(steam_df.index)

    #compare the nr of rows. If same return the saved list, if not save the new and return it
    if steam_df_rows==steam_pq_rows:
        return scru.from_paraquet('steam_games_list')
    else:
        scru.to_paraquet('steam_games_list',steam_df)
        return steam_df



    


