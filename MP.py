from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
current_volume = float(0.5)
#functions
def play_song():
    filename = filedialog.askopenfilename(initialdir = "C:/",title = " Please select an audio file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    print(song_title)

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_Label.config(fg = "green", text = 'now playing:'+ str(song_title))
        volume_Label.config(fg = "green", text = "volume:" + str(current_volume))
    except Exception as e:
        print(e)
        song_title_Label.config(fg = "red", text = 'error playing song')

def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_Label.config(fg='red', text = 'muted')
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_Label.config(fg= 'green', text = 'volume:'+ str(current_volume))
    except Exception as e :
        print(e)
        song_title_Label.config(fg= 'red', text = ' track has not been selected yet')

def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_Label.config(fg='green', text = 'max')
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_Label.config(fg= 'green', text = 'volume:'+ str(current_volume))
    except Exception as e :
        print(e)
        song_title_Label.config(fg= 'red', text = ' track has not been selected yet')

def pause():
    try:
        mixer.music.pause()
    except Exception as e :
        print(e)
        song_title_Label.config(fg='red',text='track has not been selected yet')

def resume():
    try:
        mixer.music.unpause()
    except Exception as e :
        print(e)
        song_title_Label.config(fg='red',text='track has not been selected yet')


#main screen
master = Tk()
master.title('music player')

#Labels
Label(master,text = 'custom music player', font=("Calibri", 15),fg = "red").grid(sticky= "N", row = 0 , padx = 120)
Label(master,text = 'Please select a music track you would like to play', font=("Calibri", 12),fg = "blue").grid(sticky= "N", row = 1 , padx = 120)
Label(master,text = 'Volume', font=("Calibri", 12),fg = "red").grid(sticky= "N", row = 4 , padx = 120)
song_title_Label = Label(master,font = ("Calibri",12))
song_title_Label.grid(stick = "N", row = 3)
volume_Label = Label(master, font = ("calibri",12))
volume_Label.grid(sticky= "N", row = 5)

#Buttons
Button(master, text = 'select song',font = ('Calibri',12), command = play_song).grid(row=2,sticky= "N")
Button(master, text = "pause", font=("Calibri",12),  command = pause).grid(row = 3 , sticky = "E")
Button(master, text = "resume", font=("Calibri",12),command= resume).grid(row = 3 , sticky = "W")
Button(master, text = "-", font =("Calibri",12), width = 5, command = reduce_volume).grid(row = 5 , sticky = "W")
Button(master, text = "+", font =("Calibri",12), width = 5, command = increase_volume).grid(row = 5 , sticky = "E")

master.mainloop()