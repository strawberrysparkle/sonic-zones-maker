
import tracery
import future
import requests
import requests_oauthlib
import tweepy
import os
import boto3
from tracery.modifiers import base_english
import time

#Create a zone
rules = {
    'origin': "#word1# #word2# Zone #act#",
    'word1': ["Sky","Cloud","Mystic","Magic","Mango","Strawberry","Palm","Bounce","Spring","Jump","Zoom","Star","Moon","Jungle","Undergound","Aqua","Gimmick","Gadget","Tricky","Secret","Crystal","Emerald","Tropical","Flying","Wing","Death","Rocket","Palm Tree","Wacky","Quartz","Stardust","Galaxy","Dazzle","Mecha","Electric","Sleeping","Nighttime","Grassy","Lava","Toxic","Chemical","Machine","Metal","Ice","Angel","Snow","Hydro","Hidden","Sand","Balloon","Sunset","Winter","Summer","Mushroom","Iron","Coconut","Sea","Dynamite","Silver","Radical","Toe-Tapping","Twinkle","Final","Chaos","Pumpkin","Wild","Slurpee","Bubble","Dragonfly","Speedy","Flash","Schadenfreude","Existential","Cool","Surf","Awesome","Bogus","Snack","Slime","Banana","Cake","Pie","Boing","Frantic","Homework","Octopus","Recycled"],
    'word2': ["City","Garden","Hill","Yard","Light","Brain","Tree","Island","River","Bridge","Labyrinth","Mystery","Cave","Base","Lake","Mountain","Egg","Ruins","Casino","Night","Ocean","Stream","Waterfall","Chase","Fortress","Volcano","Landslide","Tower","Speedway","Desert","Planet","Plant","Generator","Showdown","Snowboard","Carnival","Festival","Cruise Ship","Highway","Palace","Mine","Reef","Beach","Sanctuary","Valley","Panic","Party","Disco","Arena","Slide","Waterslide","Canyon","Castle","Forest","Field","Stadium","Hangar","Attitude","Factory","Warehouse","Circuit","Raceway","Utopia","Space","Train","Lagoon","Meadow","Woods","Ennui","Donut","Breakfast","Diner","Anarchy","Pinball","Spaceship","Computer"],
    'act': ["Act 1","Act 2","Act 3"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

#Twitter credentials
class TwitterAPI:
    """
    Class for accessing the Twitter API.
    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """
    def __init__(self):
        consumer_key = os.environ.get('consumer_key')
        consumer_secret = os.environ.get('consumer_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('access_token')
        access_token_secret = os.environ.get('access_token_secret')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

#Post a tweet and wait 3 hours till next post
    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(status=message)

while __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(grammar.flatten("#origin#"))
    time.sleep(10800)