import hashlib
import requests
from cachetools import cached, LRUCache, TTLCache


@cached(cache=TTLCache(maxsize=8192, ttl=360))
def get_xray_status():
    r = requests.get("http://www.n3kl.org/sun/images/status.gif")

    if r.status_code != 200:
        return "Invalid status code", None

    hashObj = hashlib.sha256()

    hashObj.update(r.content)

    digest = str(hashObj.hexdigest())

    lookup = {"3cc5b935db07b99ddf6740b42788936e6d07b0da3a766e56b584f8668ea26d14": "Normal",
              "55f8d7a96e30d5ed5b327b666b6cf51cf1349e1de177c934be26bd282ec1e9fe": "Active",
              "573a706178512326a8a941c8897cba56b0e1dfd5d7a58bf2f1be09d1c1f2590f": "Particularly Active",
              "b7199ceff0e345fc69aebe8b17531e7be11c564e762df5f7958de282318a776a": "Extremely Active",
              "a5428d7d60ffe2cb4b99a3d1c21973e1e33bd8acb394eb645b59f2280392b5fc": "Extremely Highly Active"}

    if lookup.get(digest):
        return False, lookup[digest]

    else:
        return "Hash not in hashmap", None


def get_magneto_status():
    r = requests.get("http://www.n3kl.org/sun/images/kpstatus.gif?")

    if r.status_code != 200:
        return "Invalid status code", None

    hashObj = hashlib.sha256()

    hashObj.update(r.content)

    digest = str(hashObj.hexdigest())

    print(str(digest))

    lookup = {"cc795490a5041d3ddda7b6791f676afa4797832d97a37192a051317890156a4d": "Quiet",
              "cbd1b5f332cf4d8a201f56ed0db811925835172c6dff14c133f7dec5afe65a79": "Unsettled",
              "2ab362523e7f3d6335df86997d70be77e160ef6537ff92d18c32db570a08e071": "Storm"}

    if lookup.get(digest):
        return False, lookup[digest]

    else:
        return "Hash not in hashmap", None

if __name__ == "__main__":
    print(str(get_xray_status()))
    print(str(get_magneto_status()))
