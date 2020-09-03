import requests


def badJoke():
    """tells random joke from icanhazdadjoke website"""
    res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        return str(res.json()['joke'])
    else:
        return 'oops!I ran out of jokes'
