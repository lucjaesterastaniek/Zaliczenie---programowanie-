import json, time, sys

class English_Test:

	dictionaryPath = "dictionary.json"

	logPath = "log.json"

	def __init__(self):
		self.currentTime = time.time()

		if(self.checkLastSessionDone()):
			self.dictionary = self.getJSON(self.dictionaryPath)
		else:
			self.dictionary = self.getJSON(self.logPath)

		self.questionSystem()
		self.checkCurrentSession()
		self.saveJSON(self.dictionary, self.logPath)

	def questionSystem(self):
		try:
			for key, value in list(self.dictionary.items()):
				self.askQuestion(key, value)

		except Exception as e:
			print("ERROR: Wrong structure of dictionary file")
			sys.exit()

	def askQuestion(self, key, value):
		print("przetlumacz '" + value["pl"] + "' na jezyk angielski:")
		translated = input()

		if(translated == value["en"]):
			print("Brawo!")

			self.dictionary.pop(key)
		else:
			print("Niestety - to nie jest poprawna odpowiedz")

	def checkLastSessionDone(self):
		session = self.getJSON(self.logPath)

		if("time" in session):
			if((float(session["time"]) + 604800) > self.currentTime):
				print("Ukończyles wszystkie zadania, kolejna sesja dostępna od: {0}".format(time.ctime(float(session["time"]) + 604800)))
				sys.exit()

		if(len(session) == 0 or (len(session) == 1 and "time" in session)):
			return True
		else:
			return False

	def checkCurrentSession(self):
		if(len(self.dictionary) == 0):
			self.dictionary["time"] = self.currentTime

	def saveJSON(self, content, filePath):
		try:
			with open(filePath, 'w') as f:
				json.dump(content, f)
				
		except Exception as e:
			print("Unable to save file: {0}".format(filePath))
			sys.exit()

	def getJSON(self, filePath):
		try:
			with open(filePath) as f:
				fileContent = json.load(f)

		except Exception as e:
			print("Unable to load file: {0}".format(filePath))
			fileContent = {}

		return fileContent
		
English_Test()