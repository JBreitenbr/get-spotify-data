from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
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

"""
track_ids = []
arr_len=[]
df=pd.read_csv("grouped.csv")

rnd=math.floor(random.random()*len(df))

rlst=[ 134,  135,  136,  137,  569,  850,  853,  947,  949,  950,  951,  955,969, 1059, 1120, 1232, 1233, 1234, 1258, 1259, 1264, 1266, 1267, 1361,1669, 1672, 1785, 1788, 1995, 2002, 2005, 2007, 2008, 2009, 2011, 2012,2014, 2015, 2049, 2412, 2468, 2557, 2887, 2937, 3104, 3364, 3406, 3931,3932, 3936, 3943, 3946, 3950, 4139, 4230, 4247, 4253, 4266, 4302, 4537,4541, 4691, 4821, 4822, 4823]
df=df.iloc[rlst]
print(len(df))
track_ids=[]
flags=[]
bez=[]
for i in rlst:
   artist=df.loc[i,"artist"]
   track=df.loc[i,"track"]
   artist=artist.replace("'","")
   track=track.replace("'","")
   print(i,artist,track)
   print("@@@")
   track_id=sp.search(q='artist:'+artist+' track:'+track,type="track",market="DE")

   lst=[]
   l=track_id['tracks']['items']
   for i in range(len(l)):
     lst.append({})
     lst[i]["name"]=l[i]["album"]["name"]
     lst[i]["year"]=l[i]["album"]["release_date"][:4]
     lst[i]["album_type"]=l[i]["album"]["album_type"]
     lst[i]["artists"]=l[i]["album"]["artists"][0]["name"]
     lst[i]["id"]=l[i]["id"]
     lst[i]["bez"]=l[i]["name"]
     #print(track)
     if l[i]["name"].replace("'","")==track:
       lst[i]["flag"]="a"
     else:
       lst[i]["flag"]="b"
  
   print(lst)

   nlst = sorted(lst, key=lambda d: (d["flag"],d['album_type'],d["year"]))
   if len(nlst)>0:
     track_ids.append(nlst[0]["id"])
     flags.append(nlst[0]["flag"])
     bez.append(nlst[0]["bez"])
   else:
     track_ids.append("x")
     flags.append("x")
     bez.append("x")
df["track_id"]=track_ids
df["flag"]=flags
df["bez"]=bez
df.to_csv("check_names.csv")
"""
     