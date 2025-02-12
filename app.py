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

eightBall = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

clueIntro = [
    'I think we all this coming.',
    'Rejoice!',
    'Oh no!',
    'I think Covid made them do it.',
    'I must sadly announce a tradegy!',
    'Sounds about right.',
    'THE HORROR!!!',
    'Well that ties a nice bow on the situation...'
]

clueLocation = [
    'kitchen',
    'ballroom',
    'conservatory',
    'billiard room',
    'library',
    'study',
    'hall',
    'lounge',
    'dining room'
]

clueWeapon = [
    'revolver',
    'dagger',
    'lead pipe',
    'rope',
    'candlestick',
    'wrench'
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
        
        userText = data['text'].upper()
        
        # timeout feature
        if userText == '/STOP':
            changeTimeout(True)
            send_message('Beep Boop. Village Bot shutting down...')
            return "ok", 200
        
        elif '/START' in userText or '/RUN' in userText:
            changeTimeout(False)
            send_message('Beep Boop. Village Bot ready to serve. Type \"\/" + "help\" to see what I can do!')
            return "ok", 200
        
        elif '/HELP' in userText or '/COMMANDS' in userText or '/LIST' in userText:
             send_message("Beep Boop. Here is what I can do!\\nStart all commands with a forward slash (\/)\\n##################################\\n8ball .......... Magic Eight Ball response\\nclue ........... Discover whodunit!\\nfinger or f*** . Curated middle finger\\nfortune ........ See someone's fortune\\nhelp ........... See this screen\\nhi ............. Say hi to Village Bot\\nryanjoke ....... Get ready to eye roll...\\nstart .......... Activate Village Bot\\nstop ........... Kill Village Bot\\nwho ............ Returns a random Villager\\nwhich2 ......... 2 random villager names\\nwhich3 ......... Returns 3 random villagers\\n##################################\\n")
                
        elif '/CLUE' in userText or '/MURDER' in userText:
            villager1 = random.choice(villagers)
            villager2 = random.choice(villagers)
            villager3 = random.choice(villagers)
            intro = random.choice(clueIntro)
            weapon = random.choice(clueWeapon)
            location = random.choice(clueLocation)
            msg = "{} {} killed {} with the {} in {}'s {}.".format(intro, villager1, villager2, weapon, villager3, location)
            send_message(msg)

        elif '/WHO' in userText or '/VILLAGER' in userText:
            villager = random.choice(villagers)
            send_message(villager)
            
        elif '/WHICH2' in userText or '/WHICH 2' in userText or '/WHICH TWO' in userText:
            villager1 = random.choice(villagers)
            villager2 = random.choice(villagers)            
            msg = "{} and {}".format(villager1, villager2)
            send_message(msg)
            
        elif '/WHICH3' in userText or '/WHICH 3' in userText or '/WHICH THREE' in userText:
            villager1 = random.choice(villagers)
            villager2 = random.choice(villagers)
            villager3 = random.choice(villagers)
            msg = "{}, {}, and {}".format(villager1, villager2, villager3)
            send_message(msg)
 
        elif '/8BALL' in userText or '/EIGHTBALL' in userText or '/EIGHT BALL' in userText:
            send_message(random.choice(eightBall))
            
        elif '/FINGER' in userText or '/FUCK' in userText or '/MIDDLE' in userText:
            number = random.randint(1, 15)
            imageUrl = "{}/thefinger/{}.jpg".format(os.getenv('IMAGE_PATH'),number)
            send_message(imageUrl)
        
        #uses default image
        elif '/RYAN' in userText: # captures /ryanjoke and /ryan joke
            send_dadjoke()
            defaultImage = "{}/eye/default.jpg".format(os.getenv('IMAGE_PATH'))
            send_message(defaultImage)
        
        # uses random image
        elif '/DAD' in userText: # captures /dad joke and /dadjoke
            send_dadjoke()
            eye_roll()
            
        elif '/EYEROLL' in userText:
            eye_roll()
            
        elif '/HI' in userText or '/HEY' in userText or '/HELLO' in userText or '/HEYO' in userText:
            greetStr = random.choice(randomGreetings)
            nameStr = random.choice(randomNames)
            msg = '{}, {}'.format(greetStr, nameStr)
            send_message(msg)
            
        elif '/FORTUNE' in userText:
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
    
def eye_roll():
    randomOne = random.randint(1, 2) # we need more!
    randomImage = "{}/eye/{}.jpg".format(os.getenv('IMAGE_PATH'), randomOne)
    send_message(randomImage)
    
