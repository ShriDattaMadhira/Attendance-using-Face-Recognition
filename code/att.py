print 'Preparing camera...'

import sqlite3
from twilio.rest import Client
import cognitive_face as CF

import capture

SUBSCRIPTION_KEY = '<Your Subscription Key>'
BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = '<Group ID>'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)


print 'Uploading...'
response = CF.face.detect('/home/pi/Desktop/image.jpg')

identified_faces = []

try:
	face_ids = [d['faceId'] for d in response]
	identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
	print 'Identifying...'
except:
	print 'No faces detected'


identified_persons = []
for i in range(0, len(identified_faces)):
	if not identified_faces[i]['candidates']:
		print 'Face not in Database.'
		continue
	else:
		identified_persons.append(identified_faces[i]['candidates'][0]['personId'])
		

personsList = CF.person.lists(PERSON_GROUP_ID)

conn = sqlite3.connect('<DB Name>.db')
curs = conn.cursor()
print

account_sid = "<Account SID>"
auth_token = "<Auth Token>"
client =Client(account_sid,auth_token)

for person in personsList:
	for per in identified_persons:
		if(person['personId'] == per):
			name = person['name']
			curs.execute("insert into attendance(emp_id) select emp_id from emp_details where emp_name='%s'" %name)
			number_list = curs.execute("select phone from emp_details where emp_name='%s'" %name)
			print 'Attendance marked for ' + person['name']
			for row in number_list:
				print 'Sending message...'
				print
				message= client.messages.create(to=row,from_="",body="Your attendance has been marked.")
				break

#for row in curs.execute("select ed.emp_name, a.time from emp_details ed inner join attendance a on ed.emp_id=a.emp_id"):
#	print row

conn.commit()
conn.close()


