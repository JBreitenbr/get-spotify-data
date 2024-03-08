import pandas as pd
df0=pd.read_json("StreamingHistory_music_0.json")
df1=pd.read_json("StreamingHistory_music_1.json")
df=pd.concat([df0,df1])
print(len(df))

df.sort_values(["artistName","trackName"],inplace=True)
df["artist"]=df["artistName"]
df["track"]=df["trackName"]
del df["artistName"]
del df["trackName"]
gr=df.groupby(["artist","track"])["msPlayed"].max()
print(len(gr))
gr.to_csv("grouped.csv",index=True)
