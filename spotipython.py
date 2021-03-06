import sys
import spotipy
import spotipy.util as util

# To be altered, currently finds top 250 results
def search(key, sp):
    results1 = sp.search(q=key, limit=50, offset=0, type='track')
    results2 = sp.search(q=key, limit=50, offset=50, type='track')
    results3 = sp.search(q=key, limit=50, offset=100, type='track')
    results4 = sp.search(q=key, limit=50, offset=150, type='track')
    results5 = sp.search(q=key, limit=50, offset=200, type='track')
    # This is to circumvent Spotify API search limits
    result = results1['tracks']['items'] + results2['tracks']['items'] + results3['tracks']['items'] + results4['tracks']['items'] + results5['tracks']['items']
    
    return result

client_id = ''
client_secret = ''
redirect_uri = ''
scope = 'playlist-modify-public'

username = ''  

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

key = input('Enter playlist theme: ')

#Does search on Spotify

sp = spotipy.Spotify(auth=token)

items = search(key, sp)
max = 0

#Finds the most popular track.
for i in items:
    if i['popularity'] > max:
        max = i['popularity']
        top_track = i

playlist_name = key + " - Python Generated"

playlist = sp.user_playlist_create(username, playlist_name)

threshold = max - (max / 4)

tracks = []

#Adds tracks that are in the top//This needs improvement//.
for i in items:
    if i['popularity'] > threshold:
        tracks.append(i['id'])

sp.user_playlist_add_tracks(username, playlist['id'], tracks)
