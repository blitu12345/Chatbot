import base64
import json
import httplib2

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def get_speech_service():
	credentials = GoogleCredentials.get_application_default()
	http = httplib2.Http()
	credentials.authorize(http)
	return discovery.build('speech','v1beta1',credentials=credentials)

def recognise_speech(speech_file):
	with open(speech_file,'rb') as speech:
		speech_content = base64.b64encode(speech.read())

	service = get_speech_service()
	service_request = service.speech().syncrecognize(
		body={
			'config':{
			'encoding': 'LINEAR16',
			'sampleRate': 16000,
			'languageCode': 'en-US',
			},
			'audio':{
			'content': speech_content.decode('UTF-8')
			}

		})
	response = service_request.execute()
	return response

if __name__=='__main__':
	print recognise_speech('audio.raw')

'''
	to listen .raw audio file by giving it headers  manaually because it is basic one and doesnot ha
	ve one of its own

	-> play --channels=1 --bits=16 --rate=16000 --encoding=signed-integer --endian=little test.raw
'''

'''
			r = sr.Recognizer()
		with sr.Microphone() as source:
			print "Say Something"
			audio = r.record(source,duration=3)

		with open("test.raw","wb") as f:
			f.write(audio.get_raw_data())

		self.query = speech.recognise_speech("test.raw")#['results'][0]['alternatives'][0]['transcript']
		print self.query
'''