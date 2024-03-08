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
df0=pd.read_csv("snapshot.csv")
df=df0[df0["track_id"]!="x"]
df=df.reset_index(drop=True)


dfList=[]
for i in range(1000):
  track=df.loc[i,"track_id"]
  fts=sp.audio_features(tracks=track)
  ln=pd.DataFrame.from_dict(fts)
  ln["track_id"]=track
  del ln["id"]
  del ln["uri"]
  del ln["analysis_url"]
  del ln["type"]
  del ln["track_href"]
  dfList.append(ln)

features=pd.concat(dfList)
hd=df.iloc[:1000]
mrg=pd.merge(hd,features,on="track_id")
mrg.to_csv("fts1.csv",index=False)
