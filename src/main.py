"""
=== Module Description ===
This is the driver file of the Spotify Weekly Songs Automation Project, more
details outlined in the README.

"""
import requests
import os
import json
from secrets import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTHORIZATION, AUTH_URL, TOKEN_URL
import requestUserAuth
from requestUserAuth import sendGetRequest, promptCode, requestAccessToken, \
     refreshAccessToken, getTopNSongs, getDiscoverWeeklySongs, getSongNameFromID, \
         getCurrentUserID

from base64 import b64encode


if __name__ == '__main__':
    os.system(f"start \" \" {sendGetRequest(CLIENT_ID, REDIRECT_URI)}") # opens the authorization link
    code = promptCode()
    d = requestAccessToken(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI)
    access_token = d["accessToken"]

    print(getCurrentUserID(access_token))
    songs = getDiscoverWeeklySongs(access_token)
    for songID in songs:
        print(getSongNameFromID(access_token, songID))


    
    
    

    

    

    
    










    