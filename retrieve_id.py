from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import random
import math
client_id = "dec967d105634e55942f249a600780f1"
client_secret = "33524391083f4259a50bb489370a48a6"
username = "31nfsp7vapk4zh24xzvw3lkavx5e"
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'
import requests
from datetime import datetime
from typing import List
import spotipy.util as util
from os import listdir
import warnings
warnings.filterwarnings("ignore")
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
track_ids = []
arr_len=[]
df=pd.read_csv("grouped.csv")[:200]
#rnd=math.floor(random.random()*200)
for i in range(200):
   artist=df.loc[i,"artist"]
   track=df.loc[i,"track"]
   artist=artist.replace("'","")
   track=track.replace("'","")
   print(i,artist,track)
   track_id=sp.search(q='artist:'+artist+' track:'+track, type='track',market='DE')
   z=0
   l=track_id["tracks"]["items"]
   for j in range(len(l)):
     if l[j]["name"]==track:
       z=z+1
   arr_len.append(z)
   if len(l)>0:
     track_ids.append(track_id["tracks"]["items"][0]["id"])
   else:
     track_ids.append("x")
df["track_id"]=track_ids
df["flag"]=arr_len
df.to_csv("snapshot.csv",index=False)
"""
for i in range(200):
    artist=df0.loc[i,"artist"]
    track=df0.loc[i,"track"]
    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track',limit=1)
    if track_id["tracks"]["items"]!=[]:
       trackId = track_id['tracks']['items'][0]
       lst1.append(trackId["album"]["images"][2]["url"])
       lst2.append(trackId["album"]["id"])
       lst3.append(trackId["id"])
    else:
      lst1.append("x")
      lst2.append("x")
      lst3.append("x")
df0["imgUrl"]=lst1
df0["album_id"]=lst2
df0["track_id"]=lst3
fauls=[]
for i in range(200):
  if df0.loc[i,"imgUrl"]=="x":
    fauls.append(i)
print(fauls)
"""