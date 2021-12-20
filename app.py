# bj test bot
import os
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

randomGreetings = [
    'Hey',
    'Hi',
    'Hello there',
    'Howdy'
]

randomNames = [
    'champ!',
    'slugger!',
    'partner!',
    'boyo!',
    'kiddo!',
    'sonny'
]

winningsonImages = [
    'winningson0.png',
    'winningson1.png',
    'winningson2.jpeg',
    'winningson3.jpeg',
    'winningson4.png'
]

winningsonUrls = [
  'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Ffacebook%2F001%2F100%2F432%2F0f5.jpg&f=1&nofb=1',
  'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi1.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F001%2F100%2F438%2F907.jpg&f=1&nofb=1',
  'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fare-ya-winning-son-1621129.png&f=1&nofb=1',
  'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F4l44szb9p3051.png&f=1&nofb=1',
  'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.kym-cdn.com%2Fphotos%2Fimages%2Ffacebook%2F001%2F390%2F715%2Ff2c.jpg&f=1&nofb=1',
  'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgur.com%2FKQ03nyV.png&f=1&nofb=1',
  'https://ruinmyweek.com/wp-content/uploads/2020/05/are-ya-winning-son-memes-12.jpg',
  'https://ruinmyweek.com/wp-content/uploads/2020/05/are-ya-winning-son-memes-4-1024x601.jpg',
  'https://cdn.ebaumsworld.com/mediaFiles/picture/2543003/86274102.jpg'
]

# use a file b/c I think this app.py runs only
# when a message is recieved, so a global variable
# won't save anything
def changeTimeout(timeoutBool):
    if (timeoutBool):
        os.system("echo 1 > isTimeout.txt")
    else:
        if os.path.exists("isTimeout.txt"):
            os.system("rm isTimeout.txt")

# called whenever the bot recieves a POST request
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # we don't want to reply to ourselves!
    #if data['name'] != 'dad bot tester':
    if data['name'] != 'Dad Bot':
        
        userText = data['text']
        
        # timeout feature
        if userText.upper() == 'SHUT UP DAD':
            changeTimeout(True)
            send_message('Ok sport... :(')
            return "ok", 200
        
        elif userText.upper() == 'COME BACK DAD' or userText.upper() == 'DAD COME BACK':
            changeTimeout(False)
            greetStr = random.choice(randomGreetings)
            nameStr = random.choice(randomNames)
            msg = '{}, {}'.format(greetStr, nameStr)
            send_message(msg)
            return "ok", 200
        
        print('Dad environ:', os.path.exists("isTimeout.txt"))
        if not os.path.exists("isTimeout.txt"):

            # Are ya winning, son?
            if userText.upper().startswith('AM I WINNING DAD') or userText.upper().startswith('AM I WINNING, DAD'):
                print('Sending winning son!')
                send_winningson()

            #starts with /dadjoke
            elif userText.startswith('/DADJOKE'):
                send_dadjoke()
            
            # contains i'm
            elif ' I\'m ' in userText:
                send_message('Hi, {}, I\'m Dad!'.format(userText.split(' I\'m ')[1]))
            
            elif ' I\’m ' in userText:
                send_message('Hi, {}, I\'m Dad!'.format(userText.split(' I\’m ')[1]))
            
            elif ' i\'m ' in userText:
                send_message('Hi, {}, I\'m Dad!'.format(userText.split(' i\'m ')[1]))
            
            elif ' Im ' in userText:
                send_message('Hi, {}, I\'m Dad!'.format(userText.split(' Im ')[1]))
            
            elif ' im ' in userText:
                send_message('Hi, {}, I\'m Dad!'.format(userText.split(' im ')[1]))
                
            # starts with im 
            elif userText.startswith('I\'m'):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('I\'m', '')))
                
            elif userText.startswith('I’m'):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('I’m', '')))
            
            elif userText.startswith('i\'m'):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('i\'m', '')))
            
            elif userText.startswith('im '):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('im ', '')))
            
            elif userText.startswith('Im '):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('Im ', '')))
            
            elif userText.startswith('IM '):
                send_message('Hi, {}, I\'m Dad!'.format(userText.replace('IM ', '')))
                
            elif 'HI DAD' in userText.upper():
                greetStr = random.choice(randomGreetings)
                nameStr = random.choice(randomNames)
                msg = '{}, {}'.format(greetStr, nameStr)
                send_message(msg)
        
    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    
    testcommand = 'curl -d "{\\"text\\" : \\"' + msg + '\\", \\"bot_id\\" : \\"' + os.getenv('GROUPME_BOT_ID') + '\\"}" https://api.groupme.com/v3/bots/post'
    print('command string: ' + testcommand)
    os.system(testcommand)

def send_dadjoke():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/plain',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    
    print('In send dadjoke!')
    request = Request('https://icanhazdadjoke.com/', headers=headers)
    json = urlopen(request).read().decode()
    
    url = 'https://api.groupme.com/v3/bots/post'
    
    testcommand = 'curl -d "{\\"text\\" : \\"' + json.replace('\\n', ' ').replace('"', '').replace('\\t', '    ').replace('\\', '"') + '\\", \\"bot_id\\" : \\"' + os.getenv('GROUPME_BOT_ID') + '\\"}" https://api.groupme.com/v3/bots/post'
    print('command string: ' + testcommand)
    os.system(testcommand)

def send_fortune():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    
    print('In send fortune!')
    
    request = Request('https://helloacm.com/api/fortune/', headers=headers)
    json = urlopen(request).read().decode()
    
    url = 'https://api.groupme.com/v3/bots/post'
    
    testcommand = 'curl -d "{\\"text\\" : \\"' + json.replace('\\n', ' ').replace('"', '').replace('\\t', '    ').replace('\\', '"') + '\\", \\"bot_id\\" : \\"' + os.getenv('GROUPME_BOT_ID') + '\\"}" https://api.groupme.com/v3/bots/post'
    print('command string: ' + testcommand)
    os.system(testcommand)

def send_winningson():
    
    print('In send winningson!')
    
    url = 'https://api.groupme.com/v3/bots/post'

    testcommand = 'curl -d "{\\"text\\" : \\"' + 'Are ya winning, son?\n' + random.choice(winningsonUrls).replace('\\n', ' ').replace('"', '').replace('\\t', '    ').replace('\\', '"') + '\\", \\"bot_id\\" : \\"' + os.getenv('GROUPME_BOT_ID') + '\\"}" https://api.groupme.com/v3/bots/post'
    print('command string: ' + testcommand)
    os.system(testcommand)
    
