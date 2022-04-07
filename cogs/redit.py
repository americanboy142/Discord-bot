from discord.ext.commands import Cog,command
import requests
import json
#import pandas as pd
import random

class Redit(Cog):
    CLIENT_ID = ''
    SECRET_KEY = ''
    data = {
        'grant_type': 'password',
        'username': '',
        'password': ''
        }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    host = 'https://oauth.reddit.com/r'

    def __init__(self,bot):
        self.bot = bot
        self.images = []
        self.auth = requests.auth.HTTPBasicAuth(self.CLIENT_ID,self.SECRET_KEY)
        self.res = requests.post('https://www.reddit.com/api/v1/access_token',
                                 auth= self.auth, data= self.data, headers= self.headers)
        self.TOKEN = self.res.json()['access_token']
        self.headers['Authorization'] = f'bearer {self.TOKEN}'

    @command(name= "gonewild")
    async def gonewild(self,ctx):
        self.images = []
        self.res = requests.get(f'{self.host}/gonewild/hot',
                                headers=self.headers)
        for post in self.res.json()['data']['children']:
            try:
                self.images.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            '''
            try:
                self.images.append(post['data']['preview']['images'][0]['source']['url'])
            except:
                pass
            '''
        num = random.randint(0,len(self.images))
        await ctx.send(str(self.images[num]))


    @command(name= "redit", aliases = ["image"])
    async def redit(self,ctx,subredit):
        self.images = []
        try:
            self.res = requests.get(f'{self.host}/{str(subredit)}/hot',
                                    headers=self.headers)
            for post in self.res.json()['data']['children']:
                try:
                    self.images.append(post['data']['url_overridden_by_dest'])
                except:
                    pass
            num = random.randint(0,len(self.images))
            await ctx.send(str(self.images[num]))
        except:
            await ctx.send('not valid subredit')

        
def setup(bot):
    bot.add_cog(Redit(bot))
