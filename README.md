# Nick Landreville Studios Twitter Bot

The Twitter bot used for the Nick Landreville Studios Moodboard
## Setup
Before using the bot, please go to [Twitter Developers](https://developer.twitter.com/en.html) and create an account. Apply for access to use the twitter API. Once the approval process is  complete, create a new app and get your secret info and API keys
## Installation

All you will need for this is Tweepy  
[Tweepy](http://www.tweepy.org/) - website  
[Tweepy](https://github.com/tweepy/tweepy/) - Github

```bash
pip install tweepy
```

## Usage
Here is the meat of the code:
```python
os.chdir('YOUR DIRECTORY')
for pics in os.listdir('.'):
    api.update_with_media(pics)
    time.sleep(10000)
```
The Nick Landreville Studios Twitter bot is used to post random pictures from our mood board to twitter. Where ever this file is located, make a folder with a name of your choice, it will change into that directory and post them. You can select a time interval of your choosing with time.sleep()

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
