import json
#import config
#import SusBot
#fileName = 'users.json'

def newUser(user): #done
	fileName = 'users.json'
	with open(fileName,"r") as f:
		data = json.load(f)
		entry = {
					'username': user.name,
					'credits': 0, 
					'tinderToken': None
				}
		data.append(entry)
	with open(fileName,"w") as f:
		json.dump(data,f)

def check(user): #done
	userExits = False
	with open('users.json',"r") as f:
		data = json.load(f)
		for i in data:
			if user.name == i["username"]:
				userExits = True
		if userExits == False:
			newUser(user)


def checkToken(user):
	Token = False
	with open('users.json','r') as f:
		data = json.load(f)
		for i in data:
			if user.name == i["username"]:
				if i['tinderToken'] == None:
					Token = False
				else:
					token = i['tinderToken']
					Token = True
		return(Token,token)


def getCredits(user):
	with open('users.json','r') as f:
		data = json.load(f)
		for i in data:
			if user.name == i["username"]:
				credit = i['credits']
	return credit


def giveCredits(user):
	with open('users.json','r+') as f:
		data = json.load(f)
		for i in data:
			if user.name == i["username"]:
				i['credits'] += 200
				f.seek(0)
				json.dump(data,f)
