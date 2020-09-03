import wikipedia


def citeWikipedia(reg_ex):
    """cites 100 words of a wikipedia article with given regEx as search term """
    # noinspection PyBroadException
    try:
        result = ''
        topic = reg_ex.group(1)
        if reg_ex:
            ny = wikipedia.page(topic)
            result = str(ny.content[:100].encode('utf-8'))
    except Exception as e:
        result = 'I do not know anything about' + reg_ex.group(1)
    return result
