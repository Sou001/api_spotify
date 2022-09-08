# Connection to api_spotify with Python 

### Context of this github 📉

this github is a project that allow its user to connect to one of his spotify apps and collect data of playlists (pre-chosen by adding their ids in playlist csv file in data folder), then insert 2 tables into the specified database (that we call spotify_db but can be modified in constants.py for example) 



### Set up Spotify app ✅

1 - Create your spotify app or connect to one already created

  * link to create spotify app https://developer.spotify.com/dashboard/
  * Documentation : https://developer.spotify.com/documentation/general/guides/authorization/app-settings/


 2 - Set Redirect URIs in the spotify APP settings
 
  * We add the the path : http://localhost

### Work environnement - Prerequisites  ⚙️

  * To set the environnement (librairies,..) to work, use the file in utlls by running : mamba env create -f environment.yml
  * Should enter the information about the database and spotify app infos (id and secret) in the file /code/class/constants.py or in the right places in /code/notebook/spotify-api.ipynb  📂
 

### 📁 Organisation:
```
│   .gitignore
│   README.md
│   
│
├───code
│   ├───sql_db.sql                # contains sql code to create schema of final tables
│   ├───notebook                  # contains a notebook jupter of all the code in only one file
│   │   │   api-spotify.ipynb        
│   │   │ 
│   └───class                     # contains a structured python project with a main
│           Auth.py
│           constants.py
│           main.py
│           db_manager.py
│           playlist.py
│           utils.py
│       
├───data
│   ├───evolution_popularite.csv  # backup data of one of the final tables
│   ├───histo_entrees_sorties.csv # backup data of one of the final tables
│   └───playlists.csv             # contains ids of the playlists we want to map
│   
└───utils
        environment.yml           # contains conf for the env






