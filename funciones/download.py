import pytube
from pytube import YouTube
import config as cfg
import os
from os import system
import pathlib
from pydub import AudioSegment
from colorama import Fore
def Direction(autor):
    return str(pathlib.Path(__file__).parent.absolute()).replace('funciones','songs')+'/'+autor+'/'
def YT(link):
    return YouTube(str(link))
def Download(link):
    for e in link.split(','):
        yt = YT(e)
        try:
            Descarga = yt.streams.filter(only_audio=True).first().download(formatAuthor(Direction(yt.author)))
            song = AudioSegment.from_file(Descarga)
            song.export(formatAudioClip(Descarga), format="mp3")
            os.remove(Descarga)
        except pytube.exceptions.VideoUnavailable:
            pass
def formatAuthor(string):
    entry = input("The song's name is "+string+" :")
    if(entry==''):
        return string
    else:
        return entry
def formatAudioClip(string):
    songName = string.split('/')[-1]
    entry = input("The song's name is "+songName+" :")
    if(entry==''):
        return songName
    else:
        return entry
    