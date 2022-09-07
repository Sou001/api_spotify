# Connection to api_spotify with Python

  ## This project aims to connect to api spotify using python
  

1 - Create your spotify app or connect to one already created

  * link to create spotify app https://developer.spotify.com/dashboard/
  * Documentation : https://developer.spotify.com/documentation/general/guides/authorization/app-settings/


 2 - Set Redirect URIs in the spotify APP settings
 
  * We add the the path : http://localhost


 3 - Data mining of the API
 
  * Firstly, Check the json returned to locate the information that you want to collect from the api
  * Add the id of the playlists you want to map with the code in the "data/playlists.csv"

 4 - Implement the solution to :
 
  * Connect to the spotify API

  * Collect and transform the data to the solution you want. Ours deal with two cases :
    * Store the entry and exit of artists in each playlist
    * Daily evolution of popularity of each artist

  * Connect to the DataBase

  * Map the new data collected and structure it to deal with 2 cases :
    * Append the new data of popularity in the table "artists_popularity"
    * Deal with the sub cases to keep the history of entries and exits of artists in each playlist (check code)

  

