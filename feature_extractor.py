import sys
import random
from features import feature_extract

if __name__ == '__main__':
    tot = len(sys.argv[1:])
    nrows = 750
    song_list = sys.argv[1:]
    random.shuffle(song_list)
    feature_extract(song_list[0:nrows])
