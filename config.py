host = 'https://api.gotinder.com'
#import discord
#import SusBot
#import user
import json




def setToken(user):
    with open('users.json',"r") as f:
        data = json.load(f)
        for i in data:
            if i['username'] == user.name:
                tinder_token = i['tinderToken']
                return tinder_token


def addToken(user,token):
    with open('users.json',"r+") as f:
        data = json.load(f)
        for i in data:
            if i['username'] == user.name:
                i['tinderToken'] = token
                f.seek(0)
                json.dump(data,f)
                
                


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