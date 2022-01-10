"""
=== Module Description ===
This is the driver file of the Spotify Weekly Songs Automation Project, more
details outlined in the README.

"""
import requests
import os
import json
from secrets import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTHORIZATION, AUTH_URL, TOKEN_URL
from functions import request_user_authorization, prompt_code, request_access_token, \
     get_discover_weekly_songs, create_playlist, add_song_to_playlist


def save_discover_weekly_songs(playlist_name: str) -> None:
    """ Saves Discover Weekly Songs Playlist as <playlist_name>
    in the client's spotify library.
    """
    os.system(f"start \" \" {request_user_authorization(CLIENT_ID, REDIRECT_URI)}") # opens the authorization link
    code = prompt_code()
    access_dict = request_access_token(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI)
    access_token = access_dict["accessToken"]

    songIDs = get_discover_weekly_songs(access_token)
    
    playlist = create_playlist(access_token, playlist_name) # create a playlist to hold the Discover Weekly songs

    for songID in songIDs[::-1]: # so the playlist displays the songs in the same order as the Discover Weekly playlist
        add_song_to_playlist(access_token, playlist, songID)

    return








if __name__ == '__main__':
    save_discover_weekly_songs("Discover Weekly Songs 1/10/22")
    

    
    
    

    

    

    
    










    