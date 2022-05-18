import cognitive_face as CF

SUBSCRIPTION_KEY = '<your subscription key>'
BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = '<Group ID>'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
'''
#Create person group
##CF.person_group.create(PERSON_GROUP_ID, '<Group ID>')

#Delete person group
##CF.person_group.delete(PERSON_GROUP_ID)

#Add person
name = "<Your Name>"
response = CF.person.create(PERSON_GROUP_ID, name)
person_id = response['personId']
print person_id

#Get person name from list
#print CF.person.lists(PERSON_GROUP_ID)[0]['name']

#Get personId from list
#person_id = CF.person.lists(PERSON_GROUP_ID)[2]['personId']
#print person_id

#Add face images to train
CF.person.add_face('/home/pi/Downloads/image.jpg', PERSON_GROUP_ID, person_id)
print 'Faces Added...'
'''

##print CF.person.lists(PERSON_GROUP_ID)

#Train
CF.person_group.train(PERSON_GROUP_ID)

#Training status
response = CF.person_group.get_status(PERSON_GROUP_ID)
status = response['status']
if(status == 'succeeded'):
	print 'Trained'
else:
	print 'Still Training...'
'''

person_list = CF.person.lists(PERSON_GROUP_ID)
for person in person_list:
	if(person['name'] == '<Person Name>'):
		person_id = person['personId']
		print person_id
		CF.person.add_face('/home/pi/Downloads/image2.jpg', PERSON_GROUP_ID, person_id)
		break
'''