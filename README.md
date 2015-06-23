# music_genre_classifier

Given an input .mp3 file, the program will output it's genre.

## Features

We chose the following features to describe the song:
* MFCC
* Tempo
* Scale

To extract features
`python feature_extractor.py /path/to/1.mp3 /path/to/2.mp3 ...`

To clean the data
`python data)cleaner.py data.csv`
