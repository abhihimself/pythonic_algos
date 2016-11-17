import requests
import json
import time

api_key = 'c40f39bbbd8522886a8300a2054b81d8'
root_url = 'http://api.musixmatch.com/ws/1.1/'

class Music_match_search(object):
    def __init__(self,target_keyword,target_artist):

        self.target_keyword=target_keyword
        self.target_artist=target_artist

    def search_trackid(self):
        self.search_url=root_url+'track.search?apikey='+api_key+'&q_track='+self.target_keyword+'&q_artist='+self.target_artist+'&f_has_lyrics=1'
        self.result=requests.get(self.search_url)
        return self.result


class Music_match_get_track(object):
    def __init__(self,track_id):
        self.track_id=track_id

    def get_lyrics(self):
        self.lyrics_url=root_url+'track.lyrics.get?apikey='+api_key+'&track_id='+str(self.track_id)+'&format=json'
        self.track_result=requests.get(self.lyrics_url)
        return self.track_result

if __name__ == '__main__':

    lyric_search_guy=Music_match_search('Something To Believe in')
    search_result=lyric_search_guy.search_trackid()
    parsed_json=search_result.json()
    track_id=parsed_json['message']['body']['track_list'][0]['track']['track_id']
    time.sleep(1)
    lyric_text_guy=Music_match_get_track(track_id)
    lyrics_data=lyric_text_guy.get_lyrics()
    parsed_lyrics=lyrics_data.json()
    lyric_string=parsed_lyrics['message']['body']['lyrics']['lyrics_body']
    #file=open("test.txt","w")
    #file.write(lyric_string)
