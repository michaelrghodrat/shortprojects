"""
=== Module Description ===
This module holds the client information and important urls.

"""
from base64 import b64encode

CLIENT_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CLIENT_SECRET= "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

temp = f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('utf-8') 
AUTHORIZATION = "Basic " + b64encode(temp).decode() # 64-bit encoded <CLIENT_ID:CLIENT_SECRET>

TOKEN_URL = "https://accounts.spotify.com/api/token"
AUTH_URL = "https://accounts.spotify.com/authorize"
REDIRECT_URI = "http://localhost:8888/callback"

ALL_SCOPES =   "ugc-image-upload \
                user-read-recently-played \
                user-top-read \
                user-read-playback-position \
                user-read-playback-state \
                user-modify-playback-state \
                user-read-currently-playing \
                app-remote-control \
                streaming \
                playlist-modify-public \
                playlist-modify-private \
                playlist-read-private \
                playlist-read-collaborative \
                user-follow-modify \
                user-follow-read \
                user-library-modify \
                user-library-read \
                user-read-email \
                user-read-private"

