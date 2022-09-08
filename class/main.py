import pandas as pd

from Auth import Auth
from Client import Client
from ManageDb import ManageDb

from constants import *

def main():
    # Authentification
    auth = Auth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    token = auth.get_token()["access_token"]

    # Client API
    client = Client(token)
    playlist = client.playlist

    ## Lecture du fichier métier contenant les identifiants des playlists
    id_playlists = pd.read_csv("playlists.csv").id_playlist.values.tolist()

    df_table1, df_table2 = playlist.collect_data([playlist.tracks(i) for i in id_playlists], id_playlists)

    co = ManageDb(df_table1, df_table2)
    co.update_db()

if __name__ == '__main__':
    main()