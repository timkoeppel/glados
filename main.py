# GLaDOS

# Audio/Speech Imports
import speech_recognition as sr
import sys
import re
import smtplib
#import vlc
from time import strftime
import getpass
import random
import pyttsx3
import engineio
import subprocess

# Abilities Imports
from abilities import website, reddit, weather, \
    joke, news, application, knowledge


# engineio
engineio = pyttsx3.init()
engineio.setProperty('rate',100)
voices = engineio.getProperty('voices')
engineio.setProperty('voice', 'english+f4')

# Get username of device
username = getpass.getuser()


# convert text to speech
def GLaDOS(audio):
    """speaks audio passed as argument"""
    print(audio)
    for line in audio.splitlines():
        engineio.say(audio)
        engineio.runAndWait()



# Commands
def myCommand():
    """listens for commands"""
    r = sr.Recognizer()
    # keyword = "hello"       ##keyword to wake from sleeping mode
    with sr.Microphone() as source:
        subprocess.call('clear', shell=True)    #clear
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        # if r.recognize_google(audio) == keyword:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command


# Assistant
def assistant(command):
    """if statements for executing commands"""

    # SMALLTALK
    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            GLaDOS('Hello ' + username + '. Good morning')
        elif 12 <= day_time < 18:
            GLaDOS('Hello ' + username + '. Good afternoon')
        else:
            GLaDOS('Hello ' + username + '. Good evening')

    elif 'how are you' in command:
        rnd = random.randint(0, 4)
        if rnd == 0:
            GLaDOS('I am very good. Thanks for asking!')
        elif rnd == 1:
            GLaDOS('I am good. And you?')
        elif rnd == 2:
            GLaDOS('You are here. Now I feel fantastic.')
        elif rnd == 3:
            GLaDOS('You want to get something done or chit chat mate!')
        else:
            GLaDOS('Are you trying to get my attention? I am very busy, you know.')

    # SHUTDOWN
    elif 'shut down' in command:
        GLaDOS('Bye bye ' + username + '. Have a nice day!')
        sys.exit()

    # WEBSITE
    elif 'open' in command:
        GLaDOS(website.openWebsite(re.search('open (.+)', command)) + username)

    # REDDIT
    elif 'open reddit' in command:
        GLaDOS(reddit.openSubreddit(re.search('open reddit (.*)', command)) + username)

    # JOKE
    elif 'joke' in command:
        GLaDOS(joke.badJoke())

    # NEWS
    elif 'news for today' in command:
        GLaDOS(news.getNews())

    # WEATHER
    elif 'current weather' in command:
        GLaDOS(weather.currentWeather(re.search('current weather in (.*)', command)))

    # TIME
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        GLaDOS('Current time is %d hours %d minutes' % (now.hour, now.minute))

    # APPLICATION
    elif 'launch' in command:
        GLaDOS(application.launchApp(re.search('launch (.*)', command)) + username)

    # E-MAIL
    elif 'email' in command:
        GLaDOS('Who is the recipient?')
        recipient = myCommand()
        if 'rajat' in recipient:
            GLaDOS('What should I say to him?')
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('your_email_address', 'your_password')
            mail.sendmail('sender_email', 'receiver_email', content)
            mail.close()
            GLaDOS('Email has been sent successfuly. You can check your inbox.')
        else:
            GLaDOS('I don\'t know what you mean!')

    # KNOWLEDGE
    elif 'tell me about' in command:
        GLaDOS(knowledge.citeWikipedia(re.search('tell me about (.*)', command)) + username)


    # YOUTUBE
    #elif 'play me a song' in command:
    #    path = '~/Documents/videos/'
    #    folder = path
    #    for the_file in os.listdir(folder):
        #    file_path = os.path.join(folder, the_file)
        #    try:
        #        if os.path.isfile(file_path):
        #            os.unlink(file_path)
        #    except Exception as e:
        #        print(e)

    #GLaDOS('What song shall I play Sir?')
        #mysong = myCommand()
        #if mysong:
        #    flag = 0
        #    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
        #    response = urlopen(url)
        #    html = response.read()
        #    soup1 = soup(html,"lxml")
        #    url_list = []
        #    for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
        #        if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
        #            flag = 1
        #            final_url = 'https://www.youtube.com' + vid['href']
        #            url_list.append(final_url)url = url_list[0]
        #    ydl_opts = {}os.chdir(path)
        #    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #        ydl.download([url])
        #    vlc.play(path)if flag == 0:
        #        GLaDOS('I have not found anything in Youtube ')

    # WALLPAPER
    # elif 'change wallpaper' in command:

#change user directory to your path of wishes (maybe the dark side xD)
    #    folder = '~/Documents/Pictures/'
    #    for the_file in os.listdir(folder):
    #        file_path = os.path.join(folder, the_file)
    #        try:
    #            if os.path.isfile(file_path):
    #                os.unlink(file_path)
    #        except Exception as e:
    #            print(e)
    #    api_key = 'fd66364c0ad9e0f8aabe54ec3cfbed0a947f3f4014ce3b841bf2ff6e20948795'
    #    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key


#pic from unspalsh.com
    #    f = urlopen(url)
    #    json_string = f.read()
    #    f.close()
    #    parsed_json = json.loads(json_string)
    #    photo = parsed_json['urls']['full']
    #    urllib.urlretrieve(photo, "/Users/nageshsinghchauhan/Documents/wallpaper/a") # Location where we download the image to.
    #    subprocess.call(["killall Dock"], shell=True)
    #    GLaDOS('wallpaper changed successfully')

# loop to continue executing multiple commands
while True:
    assistant(myCommand())
