import requests
import json

APIKEY='c40f39bbbd8522886a8300a2054b81d8'

root_url='http://api.musixmatch.com/ws/1.1/'
search_url=root_url+'track.search?apikey='+APIKEY+'&q_track=back%20to%20december&q_artist=taylor%20swift&f_has_lyrics=1'
text="wilder side"
req=requests.get(search_url)
j_format=req.json()
#track_id=j_format{}
