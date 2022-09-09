from sqlalchemy import create_engine
from datetime import datetime
from constants import * 
import pandas as pd

class ManageDb():

    dbConnection = None
    df_table1 = None
    df_table2 = None

    def __init__(self, df_table1, df_table2) :
        path = "postgresql+psycopg2://"+USER+":"+PWD+"@"+HOST+":"+PORT+"/"+DATABASE
        self.dbConnection = create_engine(path)
        self.df_table1 = df_table1
        self.df_table2 = df_table2

    def get_connection(self):
        return self.dbConnection

    def update_db(self):
        try :
            
            ## Récupéraiton de l'historique des entrées sorties d'artistes des playlists du métier et seulement ceux toujours dispo
            histo_playlist=pd.read_sql("select * from histo_playlist where date_sortie ='2099-12-31'", self.dbConnection)
            
            print("histo shape" , histo_playlist.shape)
            
            ## Append new data to old data
            self.df_table2.to_sql("artistes_popularity", self.dbConnection, if_exists='append', index=False)
            
                                #####################################################################
            try :
                ## Récupéraiton de l'historique des entrées sorties d'artistes des playlists du métier et seulement ceux toujours dispo
                histo_playlist=pd.read_sql("select * from histo_playlist where date_sortie ='2099-12-31'", self.dbConnection)

                ## on crée une clé sur la playlist artistes dans la table histo
                histo_playlist["artiste_histo"]=histo_playlist[["id_playlist","id_artiste"]].apply(lambda x:
                                                                                                x.id_playlist+x.id_artiste,
                                                                                                axis=1)

                ## on crée une clé sur la playlist-artiste des nouvelles détections
                self.df_table1["new_artistes"]=self.df_table1[["id_playlist","id_artiste"]].apply(lambda x:(x.id_playlist+x.id_artiste),axis=1)

                ## on prend les artistes détectés aujourd'hui & qui ne sont pas dans l'historique
                artistes_to_append=self.df_table1[~self.df_table1.new_artistes.isin(
                    histo_playlist["artiste_histo"].values.tolist())].drop("new_artistes",axis=1)

                ## on prend les artistes dans l'histo & non dans la nouvelle collecte
                artistes_to_update=histo_playlist[~histo_playlist["artiste_histo"].isin(
                    self.df_table1["new_artistes"].values.tolist())].artiste_histo.values.tolist()

                if len(artistes_to_update)>0:
                    histo_playlist["date_sortie"]=histo_playlist[["artiste_histo","date_sortie"]].apply(
                        lambda x:datetime.now() if (x.artiste_histo in artistes_to_update) 
                        else x.date_sortie, axis=1)

                histo_playlist=histo_playlist.drop("artiste_histo",axis=1)
                
                ## si on a bien des nouveaux artistes on les ajoute à l'historique
                if artistes_to_append.shape[0]>0:
                    dffinal=pd.concat([artistes_to_append,histo_playlist])
                    
                else:
                    dffinal=histo_playlist
                    
                    
                dffinal.to_sql("histo_playlist", self.dbConnection, if_exists='replace', index=False)
                
                print("new data added ")
                
                print("New shape for histo ", dffinal.shape)
                
            except Exception as e:
                print("no new insert in the table due to : ", e)

        except :
            print(" First insertion of data in DB ")
            
            self.df_table1.to_sql("histo_playlist", self.dbConnection, if_exists='replace', index=False)
            self.df_table2.to_sql("artistes_popularity", self.dbConnection, if_exists='replace', index=False)
            