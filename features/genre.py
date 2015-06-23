import eyed3
import pygn
clientID = '11545856-DEC3E5FFDC52222C23C090C9C280B9EC'
audiofile = eyed3.load("2.mp3")
artist = audiofile.tag.artist
album = audiofile.tag.album 
title= audiofile.tag.title
userID = pygn.register(clientID)
metadata = pygn.search(clientID=clientID, userID=userID, artist=artist, album=album, track=title)
print metadata ['genre']

