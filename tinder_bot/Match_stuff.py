#import tinder_api_sms
import random

messages = ["If you where a transformer you would be optimus fine",
            "Guess what you and my dog have in common?",
            "you remind me of a hot tub on a winter day.",
            "Hey good lookin",
            "How much does a polar bear weigh?"]
#things = [" sc"," SC"," Sc"," insta"," Insta"," Snap"," snap"," snapchat"," Snapchat", "@"]
#things = ["boat","Boat"]

matches = tinder_api_sms.all_matches()['data']['matches']
jew = 0
daybe = 0
sam = 0
Mrs_cat=0
blake = 0

for match in matches:
    match_id = match['_id']
    match_name = match['person']['name']
    try:
        match_bio = match['person']['bio']
    except:
        match_bio = "No Bio"

    message = random.choice(messages)
    if message == messages[0]:
        jew += 1
    if message == messages[1]:
        daybe += 1
    if message == messages[2]:
        sam += 1
    if message == messages[3]:
        blake += 1
    if message == messages[4]:
        Mrs_cat += 1
    try:
        tinder_api_sms.send_msg(match_id,message)
    except:
        print("not sent")

print("Justin:"+ str(jew) + "\nDaybe:" + str(daybe) + "\nSam:" + str(sam) + "\nBlake:" + str(blake) + "\nMrs.Cat:" + str(Mrs_cat))
