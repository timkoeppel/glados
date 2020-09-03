import webbrowser


def openSubreddit(reg_ex):
    """opens subreddit with the given regEx as subreddit name (from command)"""
    url = 'https://www.reddit.com/'
    if reg_ex:
        subreddit = reg_ex.group(1)
        url = url + 'r/' + subreddit
    webbrowser.open(url)
    return 'The Reddit content has been opened for you'
