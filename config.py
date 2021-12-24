host = 'https://api.gotinder.com'
#import discord
#import SusBot
#import user
import json


DEFAULT_TOKEN = 'b852cc05-2e8b-409e-92a4-3ddbb8634d0b'


def setToken(user):
    with open('users.json',"r") as f:
        data = json.load(f)
        for i in data:
            if data['username'] == user.name:
                tinder_token = data['tinderToken']

def addToken(user,token):
    with open('users.json',"r") as f:
        data = json.load(f)
        for i in data:
            if data['username'] == user.name:
                data['tinderToken'] = token

def check(user):
    with open('users.json',"r") as f:
        data = json.load(f)
        for i in data:
            if data['username'] == user and data['tokentinderToken'] != None:
                return True
            else:
                return False

'''
def getToken():
    if tinder_token == None:
        return DEFAULT_TOKEN
    else:
        return tinder_token
'''