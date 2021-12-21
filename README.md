# GroupMe Village Bot

Setup a GroupMe bot that uses the names of the people in your group!

## Commands

Beep Boop. Here is what I can do!

Start all commands with a forward slash (/). Commands are not case sensitive. You can use all commands in the middle of a sentence except for the /start and /stop commands.

| COMMAND          | ALTERNATIVES          | DESCRIPTION |
| :--------------- | :-----------          | :----------- |
| /8ball           |                       | Magic Eight Ball response |
| /clue            |                       | Discover whodunit! |
| /dadjoke         |                       | Random dad joke, with a random eye roll image |
| /eyeroll         |                       | Random eye roll image |
| /finger or /f*** |                       | Curated middle finger photo |
| /fortune         |                       | See someone's fortune |
| /help            |                       | See this Village Bot commands |
| /hi              |                       | Say hi to Village Bot |
| /ryanjoke        |                       | This is what Village Bot calls a dad joke. Eye roll is always Christine of course. |
| /start           |                       | Activate Village Bot |
| /stop            |                       | Kill Village Bot |
| /who             |                       | Returns a random Villager |
| /which2          |                       | Returns 2 random villager names |
| /which3          |                       | Returns 3 random villager names |

## Local Development

NOTE, APP NOT ON 3.9.9 yet.

### Get on Python 3.9.9

1. Run `python --version` to see what version of Python you have. We want it to be `3.9.9` for this project.
1. Run `brew update`
1. Run `brew upgrade pyenv`
1. Run `pyenv install 3.9.9`
3. Run `Pyevn global 3.9.9`
4. Run `python --version` and make sure you're now on Python 3.9.9.

## Deployment to Heroku

### Heroku Config Vars

1. GROUPME_BOT_ID
1. IMAGE_PATH
