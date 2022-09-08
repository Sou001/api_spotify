import requests

class Artist():
    def __init__(self, token: str):
        self.token = token
        
    def popularity(self, artist_url):
        return requests.request(
            'GET',
            artist_url,
            headers={'Authorization': 'Bearer ' + self.token}
        ).json()["popularity"]
        