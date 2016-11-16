from tkinter import *
import time
import lyrics_grabber


class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Lyrics")
        self.pack(fill=BOTH, expand=1)

        search_lable=Label(self.master,text='Enter words')
        search_lable.pack(side=LEFT)
        search_lable.place(x=10,y=10)

        entry_box=Entry(self.master)
        entry_box.pack(side=RIGHT)
        entry_box.place(x=20,y=40)

        self.output_label = Label(self.master, text='Output')
        self.output_label.place(x=20,y=60)

        search_button=Button(self,text='Search')
        search_button.place(x=225,y=55)

    def backend(self,search_string):
        lyric_search_guy = lyrics_grabber.Music_match_search(search_string)
        search_result = lyric_search_guy.search_trackid()
        parsed_json = search_result.json()
        track_id = parsed_json['message']['body']['track_list'][0]['track']['track_id']
        time.sleep(1)
        lyric_text_guy = lyrics_grabber.Music_match_get_track(track_id)
        lyrics_data = lyric_text_guy.get_lyrics()
        parsed_lyrics = lyrics_data.json()
        lyric_string = parsed_lyrics['message']['body']['lyrics']['lyrics_body']

        self.output_label["text"]=str(lyric_string)


root=Tk()
root.geometry("300x100")
app=Window(root)
root.mainloop()