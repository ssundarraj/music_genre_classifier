import wavconvert
import pitch
import scale
import tempo
import mfcc
import genre
import sys
import os
import csv


def get_feature_vector(filename):
    filename = os.path.join(os.getcwd(), filename)
    print filename
    song_genre = genre.get_genre(filename)
    if song_genre is None:
        return None

    feature_vector = []
    filename = wavconvert.mp3_to_wav(filename)

    tempo_arr = tempo.get_tempo(filename, 10)
    scale_arr = scale.get_scale(filename, 5)
    mfcc_arr = mfcc.getMFCC(filename)

    feature_vector.append(tempo_arr)
    feature_vector.extend(scale_arr)
    feature_vector.extend(mfcc_arr)

    feature_vector.append(song_genre)
    return feature_vector


def feature_extract(file_list):
    print "Total: {0}".format(len(file_list))
    with open('data.csv', 'wb') as csvfile:
        fvwriter = csv.writer(
            csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for index, f in enumerate(file_list):
            print index
            try:
                fv = get_feature_vector(f)
                if fv is None:
                    continue
                fvwriter.writerow(fv)
            except:
                pass
