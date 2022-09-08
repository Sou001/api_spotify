from Playlist import Playlist

class Client():

    def __init__(self, token:str):
        self.token = token

        self.playlist = Playlist(self.token)
        