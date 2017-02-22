import speech_recognition as sr

def record():
	print "recording"
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print "say something"
		audio=r.record(source,duration=3)

	try:
		detected=r.recognize_google(audio,show_all=True)
		return detected['alternative'][0]['transcript']

	except sr.UnknownValueError:
		print("Google could not understand audio")
		return None

	except sr.RequestError as e:
		print("Google error={0}".format(e))
		return None
pirnt "Debug"
