########New Python Program
########main.py
########GLaDOS

import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
import youtube_dl
#import vlc
import urllib.request
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
import pocketsphinx
from time import strftime
import getpass
import pyttsx3
import engineio
import lxml

import weather
import joke

# engineio
engineio = pyttsx3.init()
engineio.setProperty('rate',50)

# Get username of device
username = getpass.getuser()

# convert text to speech
def GLaDOS(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system(audio)


def myCommand():
    "listens for commands"
    r = sr.Recognizer()
#    keyword = "hello"       ##keyword to wake from sleeping mode
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
#        if  r.recognize_google(audio) == keyword:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command



def assistant(command):
    "if statements for executing commands"

#open subreddit Reddit
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        GLaDOS('The Reddit content has been opened for you ' + username +'.')
        engineio.say("The Reddit content has been opened for you " + username)
        engineio.runAndWait()


    elif 'shut down' in command:
        engineio.say("Bye Bye" + username + " Have a nice day")
        engineio.runAndWait()
        GLaDOS('Bye bye ' + username + '. Have a nice day!')
        sys.exit()


#open website
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            GLaDOS('The website you have requested has been opened for you ' + username + '.')
            engineio.say("The website you have requested has been opened for you " + username + '.')
            engineio.runAndWait()
        else:
            pass



#greetings
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            GLaDOS('Hello ' + username + '. Good morning')
            engineio.say("Hello " + username + " Good morning")
            engineio.runAndWait()
        elif 12 <= day_time < 18:
            GLaDOS('Hello ' + username + '. Good afternoon')
            engineio.say("Hello " + username + " Good afternoon")
            engineio.runAndWait()
        else:
            GLaDOS('Hello ' + username + '. Good evening')
            engineio.say("Hello " + username + " Good evening")
            engineio.runAndWait()
        #elif 'help me' in command:
        #GLaDOS("""
        #You can use these commands and I'll help you out:1. Open reddit subreddit : Opens the subreddit in default browser.
    #    2. Open xyz.com : replace xyz with any website name
    #    3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
    #    4. Current weather in {cityname} : Tells you the current condition and temperture
    #    5. Hello
    #    6. play me a video : Plays song in your VLC media player
    #    7. change wallpaper : Change desktop wallpaper
    #    8. news for today : reads top news of today
    #    9. time : Current system time
    #    10. top stories from google news (RSS feeds)
    #    11. tell me about xyz : tells you about xyz
    #    """)



#joke
    elif 'joke' in command:
        GLaDOS(joke.badjoke())


#top stories from google news
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            client = urlopen(news_url)
            xml_page = client.read()
            client.close()
            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item")
            for news in news_list[:5]:
                GLaDOS(news.title.text.encode('utf-8'))
        except Exception as e:
            print(e)



# current weather in weather.py
    elif 'current weather' in command:
        GLaDOS(weather.currentWeather(re.search('current weather in (.*)', command)))

#time
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        GLaDOS('Current time is %d hours %d minutes' % (now.hour, now.minute))

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



#launch any application
    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)

            GLaDOS('I have launched the desired application')


#play youtube song
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

#change wallpaper
#    elif 'change wallpaper' in command:

#change user directory to your path of wishes (maybe the dark side xD)
    #    folder = '~/Documents/wallpaper/'
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

#askme anything
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                GLaDOS(str(ny.content[:500].encode('utf-8')))
        except Exception as e:
                print(e)
                GLaDOS(e)
                GLaDOS('Hi ' + username + ', I am GLaDOS and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
