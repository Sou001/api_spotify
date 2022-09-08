## Pour établir la connexion à la DB
from sqlalchemy import create_engine
from constants import * 

class Connection():

    dbConnection = None
    df_table1 = None
    df_table2 = None

    def __init__(self, df_table1, df_table2) :
        path = "postgresql+psycopg2://"+USER+":"+PWD+"@"+HOST+":"+PORT+"/"+DATABASE
        self.dbConnection = create_engine(path)
        self.df_table1 = df_table1
        self.df_table2 = df_table2

    def update_db(self):
        return 
