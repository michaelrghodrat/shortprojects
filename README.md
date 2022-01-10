# spotifyPython

=== Module Description ===

Welcome to my small but original Spotify automation project. The purpose of this project is to
automate the saving of weekly "Discover Weekly" spotify playlist. The playlists are
erased by default every week, so if you do not save the songs, you may never see
them again. This project allows you to easily save your weekly songs, so
you may return to them at a later date.

=== Method ===

Step 0 is to create and register an app with Spotify. Assuming you
already have a Spotify Account, it shouldn't take more than 5 minutes:
https://developer.spotify.com/dashboard/applications

1. Request Authorization to access data. Requires:
    1. client id (given by Spotify when you register an app)
    2. response type
    3. redirect uri

I saved the client ID, client secret, redirect_uri, authorization code (essentially an encoded client id and client secret),
token url (for http requests), auth url (for http requests), and all scopes (to allow particular priveleges in the user's account)
in the file <secretsPublic.py>. Here I modified my client id and secret (which you get when you register the app)
for security purposes, but besides this modification, it is equivalent to my original <secrets.py>.
More details on the the Authorization Code Flow may be found here:
https://developer.spotify.com/documentation/general/guides/authorization/code-flow/


Then the <request_user_authorization> function sends a GET request to prompt the user for access, and
you need to copy the "code" in the resulting url to proceed to step 2.


2. Request access and refresh tokens. Requires:
    1. client id
    2. client secret (given by Spotify when you register an app)
    3. code
    4. redirect uri

The function <request_access_token> sends a POST request to gain an
access token, which can then be used to communicate with Spotify Web API in
subsequent step. 


3. Get Discover Weekly Songs and put them into a playlist.

The <get_discover_weekly_songs> function can then be used to get the current
Discover Weekly Songs, while the <create_playlist> and <add_song_to_playlist>
functions are then used to create a playlist in your Spotify library and iteratively
add each of the songs to the created playlist.

