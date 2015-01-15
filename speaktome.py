import sys
import subprocess
import re
def speak():
	print("Voices available:")
	print("Female - Agnes,Kathy,Princess,Vicki,Victoria")
	print("Male - Alex,Bruce,Fred,Junior,Ralph")
	print("Novelty voices - Albert,Bad News,Bahh,Bells,Boing,Bubbles,Cellos,Deranged,Good News,Hysterical,Pipe Organ,Trinoids,Whisper,Zarvox")
	while True:
		voice = raw_input("Select voice:")
		if not re.match("([a-z]*\s[a-z]*)|([a-z]*)",voice):
			print "Pay attention. Incorrect selection."
		else:
			break
	print("Press ^ to exit.")
	while True:
		input = raw_input("speak:")
		if not re.match("([a-z]*\s[a-z]*)|([a-z]*\'[a-z]*)|([0-9]*)",input):
			print "Only letters between a and z are allowed"
		elif(input=='^'):
			sys.exit("Bye.")
		else:
			subprocess.call(["say","-v",voice,input])

speak()	
