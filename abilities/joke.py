###joke.py
import requests
import re

def badjoke():
    res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept":"application/json"})
    if res.status_code == requests.codes.ok:
        ret = str(res.json()['joke'])
    else:
        ret = 'oops!I ran out of jokes'
    #engineio.say("oops!I ran out of jokes")
    #engineio.runAndWait()
    return ret
