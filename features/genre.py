import eyed3
import pygn
import sys


def get_genre(filename):
    clientID = '11545856-DEC3E5FFDC52222C23C090C9C280B9EC'
    audiofile = eyed3.load(filename)
    artist = audiofile.tag.artist
    album = audiofile.tag.album
    title = audiofile.tag.title
    userID = pygn.register(clientID)
    metadata = pygn.search(
        clientID=clientID, userID=userID, artist=artist, album=album, track=title)
    try:
        print metadata['genre']['1']['TEXT']
        return metadata['genre']['1']['TEXT']
    except:
        return None
