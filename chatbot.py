import system_see
import system_record
import system_speak
import os

class chatbot(object):


	def __init__(self,usr_name):
		self.usr_name = usr_name
		self.query = ""
		self.pic = ""
		self.reply = ""

	def speak(self):
		self.query = system_record.record()
		print "query said",self.query

	def sys_read(self):
		self.query = raw_input()

	def sys_see(self):
		os.system("streamer -f jpeg -o %s.jpeg"%self.usr_name)
		self.pic=self.usr_name+".jpeg"

	def sys_describe(self):
		self.reply = system_see.description(self.pic)

	def sys_speak(self):
		system_speak.speak(self.reply)

	def sys_text(self):
		print self.reply


if __name__=="__main__":
	user = chatbot("Shaakal")
	print "user started"
	#user.speak()
	user.sys_see()
	user.sys_describe()
	user.sys_speak()
	user.sys_text()