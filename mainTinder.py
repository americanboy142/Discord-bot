import maya
from datetime import date
import time
#import config
#import tinder_api_sms

gender = 1 #set to 1 or 0 // 1 = female, 0 = male
age = 23 #set age to max age

def getInfo():
    import tinder_api_sms
    info = []
    persons = tinder_api_sms.get_recs_v2()['data']['results']
    person_id = persons[0]['user']['_id']                           #id
    photoDeal = persons[0]['user']['photos']
    photos = []
    for photo in photoDeal
    photos.append(photo['url'] )                            #photo
    name = persons[0]['user']['name']                         #name
    birth_year = maya.parse(persons[0]['user']['birth_date']).datetime().year
    age = date.today().year - birth_year                     #age
    bio = persons[0]['user']['bio']                         #bio

    return (photos, name , age , bio ,person_id)

def checkIfMatch(person):
    import tinder_api_sms
    matches = tinder_api_sms.all_matches()['data']['matches']
    thing = False
    for match in matches:
        match_id = match['_id']
        match_person_id = match['person']['_id']
        if (person == match_person_id):
            thing = True
            return(match_id,thing)
    return(match_id,thing)

            
def getMatchs():
    import tinder_api_sms
    matches = tinder_api_sms.all_matches()['data']['matches']
    for match in matches:
        match_photos = []
        photos = match['person']['photos']
        for photo in photos:
            match_photos.append(photo['url'])
        match_id = match['_id']
        match_name = match['person']['name']
        match_bio = match['person']['bio']
        return(match_photos,match_name,match_bio,match_id)




'''
canSwipe = True
while canSwipe:
    persons = tinder_api_sms.get_recs_v2()['data']['results']
    for person in persons:
        person = person['user']
        person_id = person['_id']
        person_bio = person['bio']
        person_name = person['name']
        photos = []
        photos = person['photos']
        gender = person['gender']

        person_photo = []
        person_photo = photos

        birth_year = maya.parse(person['birth_date']).datetime().year
        person_age = date.today().year - birth_year



        if (canSwipe and person_age <= age and gender == gender):
            result = tinder_api_sms.like(person_id)
            print(person_name, person_bio, person_age)
            canSwipe = result.get('likes_remaining')
            print(canSwipe)

        time.sleep(3)
        break
    break
'''

