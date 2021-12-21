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

villagers = [
    'Melanie',
    'April',
    'Christine',
    'Colby',
    'Daniel',
    'Dave',
    'Elissa',
    'Gio',
    'Heather',
    'Kim',
    'Mark',
    'Nate',
    'Price',
    'Rob',
    'Russ',
    'Ryan',
    'Sarah',
    'Tim',
    'Wesley'
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
        if userText.upper() == '/STOP':
            changeTimeout(True)
            send_message('Beep Boop. Village Bot shutting down...')
            return "ok", 200
        
        elif userText.upper() == '/START' or userText.upper() == '/RUN' or userText.upper() == '/BOT' or userText.upper() == '/VILLAGEBOT':
            changeTimeout(False)
            send_message('Beep Boop. Village Bot ready to serve. Type \"\/help\" to see what I can do!')
            return "ok", 200
        
        elif userText.upper() == '/HELP':
             send_message('help text will go here!') #TODO
                
        elif userText.upper() == '/WHO'  or userText.upper() == '/2 VILLAGERS' or userText.upper() == '/1':
            villager = random.choice(villagers)
            send_message(villager)
            
        elif userText.upper() == '/WHICH 2' or userText.upper() == '/WHICH2' or userText.upper() == '/WHICH TWO' or userText.upper() == '/2VILLAGERS' or userText.upper() == '/2 VILLAGERS' or userText.upper() == '/2':
            villager1 = random.choice(villagers)
            villager2 = random.choice(villagers)            
            msg = "{} and {}".format(villager1, villager2)
            send_message(msg)
            
        elif userText.upper() == '/WHICH 3' or userText.upper() == '/WHICH3' or userText.upper() == '/WHICH THREE' or userText.upper() == '/3VILLAGERS' or userText.upper() == '/3 VILLAGERS' or userText.upper() == '/3':
            villager1 = random.choice(villagers)
            villager2 = random.choice(villagers)
            villager3 = random.choice(villagers)
            msg = "{}, {}, and {}".format(villager1, villager2, villager3)
            send_message(msg)
 
        elif '/DADJOKE' in userText.upper() or '/DAD JOKE' in userText.upper() or '/RYANJOKE' in userText.upper():
            send_dadjoke()
            
        elif '/HI' in userText.upper() or '/HEY' in userText.upper() or '/HELLO' in userText.upper() or '/HEYO' in userText.upper():
            greetStr = random.choice(randomGreetings)
            nameStr = random.choice(randomNames)
            msg = '{}, {}'.format(greetStr, nameStr)
            send_message(msg)
            
        elif '/FORTUNE' in userText.upper():
            send_fortune()

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
    
