import subprocess


def launchApp(reg_ex):
    """launches application on the device with given regEx as application name"""
    # noinspection PyBroadException
    try:
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname + ".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            result = 'I launched ' + appname + ' for you'
    except Exception:
        result = 'I am sorry, I could not find the application'
    return result
