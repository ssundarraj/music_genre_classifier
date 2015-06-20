import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc

sample_rate, X = scipy.io.wavfile.read("../data/1.wav")
ceps,mspec,spec = mfcc(X)
mfcc = []
num_ceps = len(ceps)
mfcc.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
mfcc=np.array(mfcc)
print mfcc

