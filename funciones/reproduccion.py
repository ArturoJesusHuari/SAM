#import pygame
import os
import sys
from time import sleep
from os import system, path
from .download import *
from colorama import init, Fore, Back
init()
class SAM:
    #Sistema de archivos musicales
    def __init__(self):
        self.bands = dict(enumerate(os.listdir(os.getcwd()+'/songs/'),start=1))
    def clear(self):
        if(os.name =='nt'):
            system('cls')
        elif(os.name =='posix'):
            system('clear')
    def home(self):
        self.viewBands()
        inp = input('>>')
        if(inp == 'exit'):
            exit()
        try:
            self.selectionBand(int(inp))
        except:
            Download(inp)
            self.home()
    def viewBands(self):
        self.clear()
        print(Fore.CYAN+"""███████╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗████╗ ████║
███████╗███████║██╔████╔██║
╚════██║██╔══██║██║╚██╔╝██║
███████║██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝"""+Fore.RESET)
        self.__init__()
        for key in self.bands:
            print(Fore.GREEN+key,self.bands[key]+Fore.RESET)
    def selectionBand(self,selection):
        try:
            self.songsFrom(self.bands[selection])
        except:
            self.viewBands()
    def songsFrom(self,band):
        self.clear()
        songs = dict(enumerate(os.listdir(os.getcwd()+'/songs/'+band+'/'),start=1))
        for key in songs:
            name, ext = os.path.splitext(songs[key])
            print(Fore.YELLOW+key,songs[key].replace('.mp3','')+Fore.RESET)
        self.selectionSong(band,songs)
    def sound(self,path):
        try:
            system('mpv '+path.replace(' ','\ '))
        except:
            pass
    def selectionSong(self,band,songs):
        selection = input('>> ')
        if(selection=='back'):
            self.home()
        elif(selection=='all'):
            for song in songs.values():
                print(song)
                self.sound(os.getcwd()+'/songs/'+band+'/'+song)
            self.songsFrom(band)
        try:
            for e in list(selection.split(',')):
                print(songs[int(e)])
                self.sound(os.getcwd()+'/songs/'+band+'/'+songs[int(e)])
            self.songsFrom(band)
        except:
            self.songsFrom(band)

