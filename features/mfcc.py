import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc as MFCC


def getMFCC(file_name): 	
	sample_rate, X = scipy.io.wavfile.read(file_name)
	ceps,mspec,spec = MFCC(X)
	ans = []
	num_ceps = len(ceps)
	ans.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
	mfcc = np.array(ans)
	return ans[0]

