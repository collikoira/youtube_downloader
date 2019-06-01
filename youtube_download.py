from pytube import YouTube
import os
import time
from pydub import AudioSegment

def download(stream):
    """Download stream"""
    stream.download()

def convert():
    file_name = yt.title
    file = AudioSegment.from_file(str(file_name)+".webm")
    file.export(str(file_name)+".mp3", format="mp3")
    """delete old one"""
    os.remove(file_name+".webm")


yt = YouTube('Youtube link')
stream = yt.streams.filter(only_audio=True).all()
"""Youtube lists streams by format mp4, webm and so on.
 The one we are interested is audio/webm, webm is audio format.
 Usually it's the second one"""
this = stream[1]

download(this)
convert()



