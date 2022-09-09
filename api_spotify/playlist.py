#Playlist class : get info and get the tracks inside a playlist
from datetime import datetime
import pandas as pd
import requests


class Playlist():
    def __init__(self, token: str):
        self.token = token

    def get_json(self,url):
        ''' return json from url '''
        return requests.request('GET',url,headers={'Authorization': 'Bearer ' + self.token}).json()

    def get_tracks(self, PlaylistID: str):
        ''' return list of playlist's tracks information in dict format '''
        return self.get_json('https://api.spotify.com/v1/playlists/' + PlaylistID + '/tracks')["items"]

    def get_popularity(self,artist_data):
       # return self.get_json(artiste_url)["popularity"]
       return artist_data["popularity"]

    def convert_data_types(self, df, dct_type):
        ''' convert type of columns of a dataframe '''
        return df.astype(dct_type)
    
    def collect_data(self, id_playlists):
        ''' collect infos needed from playlists tracks '''
        table1=[]
        table2=[]

        playlists_data=[self.get_tracks(i) for i in  id_playlists]

        for i in range(0,len(playlists_data)):

            id_playlist=id_playlists[i]
            
            for track in playlists_data[i]: 

                for artiste in track["track"]["artists"]:

                    idartiste = artiste["id"]
                    name = artiste["name"]
                    ## la 1ère table
                    table1.append([id_playlist,idartiste,datetime.now(),'2099-12-31 00:00:00'])

                    ## La 2ème table
                    #popularity = self.get_json()
                    artist_data = self.get_json(artiste["href"])
                    table2.append([idartiste,
                                   name,
                                   self.get_popularity(artist_data),
                                   datetime.now()])

        ## we drop duplicates because an artist can appear more than once in a playlist          
        df_table1 = pd.DataFrame(table1,columns=["id_playlist", "id_artiste",
                                                 "date_entree", "date_sortie"]).drop_duplicates(subset=["id_playlist", "id_artiste"])

        ## we drop duplicates because an artist can appear multiple times in a playlist/S
        df_table2 = pd.DataFrame(table2,columns=["id_artiste", "nom_artiste", 
                                                "popularite", "date_effet"]).drop_duplicates()

        # preprocessing & formattage
        df_table1 = self.convert_data_types(df_table1, {'id_playlist': 'str',
                                                    'id_artiste': 'str',
                                                    'date_entree': 'datetime64',
                                                    'date_sortie': 'datetime64'})

        df_table2 = self.convert_data_types(df_table2, {'id_artiste': 'str',
                                                    'nom_artiste': 'str',
                                                    'popularite': 'str',
                                                    'date_effet': 'datetime64'})
        return df_table1, df_table2