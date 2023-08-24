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
    yt = YT(link)
    try:
        Descarga = yt.streams.filter(only_audio=True).first().download(Direction(yt.author))
        song = AudioSegment.from_file(Descarga)
        song.export(formatAudioClip(Descarga), format="mp3")
        #audioclip = AudioFileClip(Descarga)
        #print(audioclip.filename)
        #print('-')
        #print(formatAudioClip(audioclip.filename))
        #audioclip.write_audiofile(formatAudioClip(audioclip.filename))
        os.remove(Descarga)
    except pytube.exceptions.VideoUnavailable:
        pass
def formatAudioClip(string):
    string = string.replace('.mp4', '.mp3')
    years = [str(num) for num in range(1950,2100)]
    listWords = years + ['(',')'
                ,'Official','Video','Español','//'
                ,'Letra','Music','4K','Sub.','Sub'
                ,'Remaster','[',']','HD','Visualizer',
                'Lyric','Remix','Version','Audio',
                'Live','On','MTV','Unplugged','Unedited',
                'Edit','edit','|','Alternate','-']
    for word in listWords:
        string = string.replace(word,'')
    while True:
        if(string[-5]==' '):
            string = string[0:-6]+'.mp3'
        else:
            break
    return string