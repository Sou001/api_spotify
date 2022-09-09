import pandas as pd

from api_spotify.playlist import Playlist
from api_spotify.Auth import Auth
from api_spotify.constants import *

from pandas.testing import assert_frame_equal

def test_convert_data_types():
    # GIVEN
    playlist = Playlist("abc")
    df = pd.DataFrame(data={'str_col': ["a", "b"],
                            'int_col': ["1", "2"], 
                            'dt_col': ["2022-09-09", "2022-09-10"]})
    # WHEN
    wanted_types = {'str_col': 'str',
                    'int_col': 'int64',
                    'dt_col': 'datetime64'}

    df_actual = playlist.convert_data_types(df, wanted_types)
    
    # THEN
    df_expected = pd.DataFrame({'str_col':pd.Series(["a","b"], dtype='str'), 
                            'int_col':pd.Series([1,2], dtype='int64'),
                            'dt_col':pd.Series(["2022-09-09", "2022-09-10"], dtype='datetime64[ns]')})
    
    assert_frame_equal(df_actual, df_expected, check_dtype=True)

def test_get_popularity():
    # GIVEN
    playlist = Playlist("token")
    artist_data = {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh"
        },
        "followers": {
            "href": None,
            "total": 25941343
        },
        "genres": [
            "dance pop",
            "hip pop",
            "pop",
            "queens hip hop",
            "rap"
        ],
        "href": "https://api.spotify.com/v1/artists/0hCNtLu0JehylgoiP8L4Gh",
        "id": "0hCNtLu0JehylgoiP8L4Gh",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb6a8e5e8752d1dc2dafa63f20",
                "width": 640
            },
            {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051746a8e5e8752d1dc2dafa63f20",
                "width": 320
            },
            {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1786a8e5e8752d1dc2dafa63f20",
                "width": 160
            }
        ],
        "name": "Nicki Minaj",
        "popularity": 86,
        "type": "artist",
        "uri": "spotify:artist:0hCNtLu0JehylgoiP8L4Gh"
    }
    
    # WHEN
    actual_popularity = playlist.get_popularity(artist_data)
    
    # THEN
    expected_popularity = 86
    assert(actual_popularity == expected_popularity)

def test_collect_data():
    # GIVEN
    token = Auth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET).get_token()
    playlist = Playlist(token)

    # WHEN
    id_playlists = ['37i9dQZF1DXcBWIGoYBM5M']
    actual1, actual2 = playlist.collect_data(id_playlists)
    df1_cols = ['id_playlist', 'id_artiste', 'date_entree', 'date_sortie']
    df2_cols = ['id_artiste', 'nom_artiste', 'popularite', 'date_effet']
    # THEN
    assert(actual1.columns == df1_cols).all()
    assert(actual2.columns == df2_cols).all()


