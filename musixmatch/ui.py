from tkinter import *
from tkinter import messagebox as tkMessageBox
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

        #search_lable=Label(self.master,text='Enter words')
        #search_lable.pack(side=LEFT)
        #search_lable.place(x=10,y=10)

        entry_box1=Entry(self.master)
        entry_box1.pack(side=RIGHT)
        entry_box1.place(x=20,y=20)
        entry_box1.insert(END,"Enter lyrics")

        entry_box2 = Entry(self.master)
        entry_box2.pack(side=RIGHT)
        entry_box2.place(x=20, y=50)
        entry_box2.insert(END, "Enter Artist")

        #self.output_label = Label(self.master, text='Output')
        #self.output_label.place(x=20,y=60)

        search_button=Button(self,text='Search',command=lambda: self.backend(str(entry_box1.get()),str(entry_box2.get())) )
        search_button.place(x=225,y=55)

    def backend(self,search_string,search_artist):
        lyric_search_guy = lyrics_grabber.Music_match_search(search_string,search_artist)
        search_result = lyric_search_guy.search_trackid()
        parsed_json = search_result.json()
        track_id = parsed_json['message']['body']['track_list'][0]['track']['track_id']
        time.sleep(1)
        lyric_text_guy = lyrics_grabber.Music_match_get_track(track_id)
        lyrics_data = lyric_text_guy.get_lyrics()
        parsed_lyrics = lyrics_data.json()
        print(parsed_lyrics)
        lyric_string = parsed_lyrics['message']['body']['lyrics']['lyrics_body']


        tkMessageBox.showinfo('Text', lyric_string)


root=Tk()
root.geometry("300x100")
app=Window(root)
root.mainloop()