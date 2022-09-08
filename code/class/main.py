
from Playlist import Playlist
from ManageDb import ManageDb
from constants import *
from Auth import Auth
import pandas as pd


def main():
    
    # Authentification and get token
    token = Auth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET).get_token()
    print(token)

    ## Lecture du fichier métier contenant les identifiants des playlists
    id_playlists = pd.read_csv("../data/playlists.csv").id_playlist.values.tolist()
    df_table1, df_table2 = Playlist(token).collect_data(id_playlists)

    ## connect to db and update it
    ManageDb(df_table1, df_table2).update_db()

if __name__ == '__main__':
    main()