import os
import re


def speak(txt):
	replaced = re.sub(" ","-",txt)
	os.system('espeak {}'.format(replaced))

if __name__=="__main__":
	speak("person sitting on a table")