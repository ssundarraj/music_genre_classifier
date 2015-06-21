import envoy
import requests
import json


def get_fp(file_name):
    cmd = "fpcalc {0}".format(file_name)
    e = envoy.run(cmd)
    if e.status_code is 0:
        fp_out = e.std_out
    else:
        print "err"
    duration = fp_out.split("\n")[1].split("=")[-1]
    fp = fp_out.split("\n")[2].split("=")[-1]
    return duration, fp


def get_genre(file_name):
    duration, fp = get_fp(file_name)
    acoustid_uri = "http://api.acoustid.org/v2/lookup"
    acoust_data = {'format': 'json', 'client': 'ULjKruIh',
            'duration': duration, 'fingerprint': fp,}
    acoustid_req = requests.get(acoustid_uri, data=acoust_data)
    mb_id = json.loads(acoustid_req.text)['results'][0]['id']
    
    # api_key
    # tadb_uri =  "http://www.theaudiodb.com/api/v1/json/{0}/track-mb.php?i={1}".format(api_key, mb_id)
    # tadb_data = {'mbid': mb_id, 'api_key': '528efbcb0ff6bd81aee158efbbfa77f2'}
    # r = requests.get(lastfm_uri, data=lastfm_data)
    # print r.status_code
    # print r.text


get_genre("Pompeii.wav")
