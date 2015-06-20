import envoy


def mp3_to_wav(file_name):
    wav_file_name = "".join(file_name.rsplit('.')[:-1:]) + ".wav"
    cmd = "ffmpeg -i {0} {1}".format(file_name, wav_file_name)
    e = envoy.run(cmd)
    e.status_code
    return e.status_code == 0

