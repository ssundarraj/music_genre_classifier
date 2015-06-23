import wavconvert
import pitch
import scale
import tempo
import mfcc


def get_feature_vector(filename):

    feature_vector = []

    #wavconvert.mp3_to_wav(filename)
    tempo_arr = tempo.get_tempo(filename, 10)
    scale_arr = scale.get_scale(filename, 5)
    mfcc_arr = mfcc.getMFCC(filename) 
    # print scale_arr
    feature_vector.append(tempo_arr)

    feature_vector.extend(scale_arr)
    feature_vector.extend(mfcc_arr)
    return feature_vector	

print get_feature_vector("1.wav")
