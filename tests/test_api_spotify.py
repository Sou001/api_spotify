import pandas as pd

from api_spotify.playlist import Playlist

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

