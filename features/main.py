import wavconvert
import pitch
import scale
import tempo
# import key
# import mfcc


def get_feature_vector(filename):

    feature_vector = []

    # wavconvert.mp3_to_wav(filename)
    tempo_arr = tempo.get_tempo(filename, 10)
    scale_arr = scale.get_scale(filename, 5)
    # print tempo_arr
    # print scale_arr
    feature_vector.extend(tempo_arr)
    feature_vector.extend(scale_arr)


get_feature_vector("Pompeii.wav")
