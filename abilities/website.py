import webbrowser


def openWebsite(reg_ex):
    """opens website with the given regEx as website nomain with TLD (from command)"""
    if reg_ex:
        domain = reg_ex.group(1)
        print(domain)
        url = 'https://www.' + domain
        webbrowser.open(url)
        return domain + ' has been opened for you '
    else:
        pass
