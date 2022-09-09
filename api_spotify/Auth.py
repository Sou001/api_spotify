

import requests
from utils import *

        
class Auth():
    
    client_id = None
    client_secret = None
    token = None
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token=self.set_token()

    def set_token(self):
        return requests.request(
            'POST',
            'https://accounts.spotify.com/api/token',
            data={
                'grant_type': 'client_credentials'
            },
            headers={'Authorization': 'Basic ' + b64(str(self.client_id) + ':' + str(self.client_secret))}
        ).json()

    def get_token(self):
        return self.token["access_token"]
