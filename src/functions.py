"""
=== Module Description ===
The purpose of this module is to request spotify account authorization from the
user. This is step 1 in the process outlined in README.

"""

import requests
import json
from secrets import AUTH_URL, TOKEN_URL, AUTHORIZATION, ALL_SCOPES
from typing import List
from base64 import b64encode


def request_user_authorization(client_id: str, redirect_uri: str, response_type="code" ) -> str:
    """Sends a GET request to '/authorize' endpoint to request authorization from
    user and returns the url of the user authorization link.
    """
    d = {       'client_id': client_id,
                'response_type': response_type,
                'redirect_uri': redirect_uri,
                'scope': ALL_SCOPES
        }
    response = requests.get(AUTH_URL, params=d)
    return response.url
    
# user must click on the link and authorize, this is done through main.py
# then the code must be taken from the url in resulting link


def prompt_code() -> str:
    """Prompts the user for the code and returns it
    """
    return input("Please enter the code from the url in the post-authorization \
                 page:\n")


def get_current_user_ID(access_token: str) -> str:
    """Returns the current user's ID.
    """
    headers = {  "Authorization": "Bearer " + access_token }

    resp = requests.get('https://api.spotify.com/v1/me', headers=headers)
    d = json.loads(resp.text)
    return d["id"]

    


def request_access_token(client_id: str, client_secret: str, code: str, redirect_uri: str) -> dict:
    """Sends a POST request to the '/api/token' endpoint. Returns a dict of the
    form:   accessToken: <accessToken>
            refreshToken: <refeshToken>
    """

    data = {    'grant_type': "authorization_code",
                'code': code,
                'redirect_uri': redirect_uri,
                }
    
    headers = { 'Authorization': AUTHORIZATION,
                'Content-Type': "application/x-www-form-urlencoded"}

    resp = requests.post(TOKEN_URL, data=data, headers=headers)
    d = json.loads(resp.text)

    return {    "accessToken": d['access_token'],
                "refreshToken": d['refresh_token']
            }


def refreshAccessToken(refresh_token: str) -> str:
    """ Sends a POST request to '/api/token' endpoint to receive a refreshed
    Access Token and returns the refreshed access token.
    """
    data = {    "grant_type": "refresh_token",
                "refresh_token": refresh_token
            }
    headers = { "Authorization": AUTHORIZATION,
                "Content-Type": "application/x-www-form-urlencoded"
            }
    
    resp = requests.post(TOKEN_URL, data=data, headers=headers)
    d = json.loads(resp.text)
    return d["access_token"]


def getTopNSongs(access_token: str, n: int, time_range: str) -> List[str]:
    """ Uses <access_token> to send a GET request and returns top <n> songs for 
    the user over given <time_range>.
    
    Preconditions:  (1) User is already authorized and access token is available.
                    (2) 1 <= n <= 50
                    (3) time_range = "short_term" OR "medium_term" OR "long_term"

                    short_term is approx. 4 weeks
                    medium_term is approx. 6 months
                    long_term is several years
    """
    songs = []
    headers = {  "Authorization": "Bearer " + access_token }
    params = {  "time_range": time_range,
                "limit": n}
    resp = requests.get('https://api.spotify.com/v1/me/top/tracks', params=params, headers=headers)
    d = json.loads(resp.text)

    # d[items] is a list where each entry is a dictionary that contains
    # information about a given song.
    # In each such dicitonary, we want the value corresponding to the key "name"

    for dict_ in d["items"]:
        songs.append(dict_["name"])
    return songs


def get_discover_weekly_songs(access_token: str) -> List[str]:
    """Returns the DiscoverWeekly Playlist as a list of strings where each string
    is the track id of a song in the playlist. 
    """
    songs = []
    headers = {  "Authorization": "Bearer " + access_token }
    params = {  "q": "Discover Weekly",
                "type": "playlist"}

    search = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # run a search for the playlist
    d = json.loads(search.text)
    playlists = d["playlists"]["items"]
    
    for playlist in playlists:
        if playlist["name"] == "Discover Weekly": # verify this is the desired playlist
            playlist_id = playlist["id"]
            break

    resp = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers)
    dict_ = json.loads(resp.text)
    for song in dict_["items"]:
        songs.append(song["track"]["id"])
    
    return songs


def get_song_name_from_ID(access_token: str, songID: str) -> List[str]:
    """Returns name of the song specified by <songID>.
    """
    headers = {  "Authorization": "Bearer " + access_token }

    resp = requests.get(f'https://api.spotify.com/v1/tracks/{songID}', headers=headers)
    d = json.loads(resp.text)
    return d["name"]


def create_playlist(access_token: str, playlistName: str) -> str:
    """Creates a playlist titled <playlistName> in the user's library and returns the playlist ID of the created playlist.
    """
    user_id = get_current_user_ID(access_token)
    headers = {     "Authorization": "Bearer " + access_token,
                    "Content-Type": "application/json"
                }
    data = json.dumps({     "name": playlistName,
                            "description": "Python-generated Discover Weekly playlist"
                        })
    resp = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', data=data, headers=headers)
    d = json.loads(resp.text)
    return d["id"]


def add_song_to_playlist(access_token: str, playlistID: str, songURI: str) -> None:
    """Adds song specified by <songURI> to the playlist specified by <playlistID>.
    """
    headers =   {   "Authorization": "Bearer " + access_token,
                    "Content-Type": "application/json"
                }
    
    preData =   {   "position": 0,
                    "uris": [f'spotify:track:{songURI}']
                }

    data = json.dumps(preData)
    
    requests.post(f'https://api.spotify.com/v1/playlists/{playlistID}/tracks', data=data, headers=headers)

    
    


    




    





    
    
        

    







    

    


