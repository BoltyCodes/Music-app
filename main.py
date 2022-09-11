from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer
import os

path = r'C:\Users/dhruv/OneDrive/Desktop/CyberSecurity(priv)/music players'
filelist = []


pygame.init()

class MusicPlayer:


  
    def __init__(self, window):
        
        window.geometry('1080x900')
        window.title('Music player'); window.resizable(0, 0)

        load = Button(window, text = 'Load', width = 10, font = ('verdana',10,'bold'), command = self.load)
       # load.config( height = WHATEVER, width = WHATEVER2 )

        play = Button(window, text = 'Play', width = 10, font = ('verdana',10,'bold'), command = self.play)
     #   play.config( height = WHATEVER, width = WHATEVER2 )

        pause = Button(window, text = 'Pause', width = 10, font = ('verdana',10,'bold'), command = self.pause)
     #   pause.config( height = WHATEVER, width = WHATEVER2 )

        stop = Button(window, text = 'Stop', width = 10, font = ('verdana',10,'bold'), command = self.stop)
  #      stop.config( height = WHATEVER, width = WHATEVER2 )
#
        rewind = Button(window, text = 'rewind', width = 10, font = ('verdana',10,'bold'), command = self.rewind)
   #     rewind.config( height = WHATEVER, width = WHATEVER2 )

        getPos = Button(window, text = 'current pos', width = 10, font = ('verdana',10,'bold'), command = self.getpos)
        getPos.config( height = 30, width = 23 )

        loaddir = Button(window, text = 'load dir', width = 10, font = ('verdana',10,'bold'), command = self.loaddir)
        loaddir.config( height = 30, width = 20 )
        


        load.place(x = 0, y = 20); play.place(x = 110, y = 20); stop.place(x = 110, y = 60); pause.place(x = 220, y = 20); rewind.place(x = 220, y = 60); getPos.place(x = 0, y = 60)
        loaddir.place(x = 0 , y = 110)
       

        self.music_file = False
        self.playingstate = False



    
    def load(self):
        self.music_file = filedialog.askopenfilename()
    
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    
    def pause(self):
        if not self.playingstate:
            mixer.music.pause()
            self.playingstate = True
        
        else:
            mixer.music.unpause()
            self.playingstate = False
        
    def stop(self):
        mixer.music.stop()

    def rewind(self):
     pygame.mixer.music.rewind()

    
    def getpos(self):
        position = pygame.mixer.music.get_pos()

    def loaddir(self):
      for files in os.walk(path):

        for file in files:

          if file.endswith(".mp3".lower()):
            filelist.append(file)

            for song in filelist:
                mixer.init()
                mixer.music.load(song)
                mixer.music.play()
                
            




pygame.mixer.music.set_volume(0.08)

root = Tk() 
app = MusicPlayer(root)  
root.mainloop()




