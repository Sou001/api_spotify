#Playlist class : get info and get the tracks inside a playlist
import requests
import pandas as pd
import datetime

from Artist import Artist

class Playlist():
    def __init__(self, token: str):
        self.token = token

    def get(self, PlaylistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/playlists/' + PlaylistID,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()

    def tracks(self, PlaylistID: str):
        return requests.request(
            'GET',
            'https://api.spotify.com/v1/playlists/' + PlaylistID + '/tracks',
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()["items"]
    
    def collect_data(self, playlists_data, id_playlists):
        table1=[]
        table2=[]
        for i in range(0,len(playlists_data)):
            id_playlist=id_playlists[i]
            for track in playlists_data[i]: 
                for artiste in track["track"]["artists"]:
                    idartiste = artiste["id"]
                    name = artiste["name"]
                    ## la 1ère table
                    table1.append([id_playlist,idartiste,datetime.now(),'2099-12-31 00:00:00'])
                    ## La 2ème table
                    #table2.append([idartiste,name,spotifyapi.get_url(artiste["href"])["popularity"],datetime.now()])
                    artist =  Artist(self.token)
                    popularity = artist.popularity(artiste["href"])
                    table2.append([idartiste,name,popularity,datetime.now()])
                    
        df_table1 = pd.DataFrame(table1,columns=["id_playlist", "id_artiste","date_entree", "date_sortie"])
        df_table2 = pd.DataFrame(table2,columns=["id_artiste", "nom_artiste", "popularite", "date_effet"])
        
        return df_table1, df_table2

    def preprocessing(self, df, dct_type):
        return df.astype(dct_type)
        