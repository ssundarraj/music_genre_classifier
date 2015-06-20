import scikits.audiolab
import scipy
import operator


def calc_scale(file_name, scale_len):
    x, fs, nbits = scikits.audiolab.wavread(file_name)
    X = scipy.fft(x)
    XwoZ = []
    for v in X:
        if v[0] != 0 and v[1] != 0:
            XwoZ.append(v)
    Xdb = 20 * scipy.log10(scipy.absolute(XwoZ))
    f = scipy.linspace(0, fs, len(Xdb))
    scale_dict = {}
    for i in Xdb:
        freq_val = -int((i[0] + i[1])/2)
        k = freq_val - freq_val % 5
        scale_dict[k] = scale_dict.get(k, 0) + 1
    sorted_scale_dict = sorted(scale_dict.items(), key=operator.itemgetter(1), reverse=True)
    scale = sorted([v[0] for v in sorted_scale_dict[0:scale_len]])
    return scale


print calc_scale("Pompeii.wav", 5)