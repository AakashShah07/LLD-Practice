class Question:
	def __init__(self, id, text, qType):
		self.questionId = id 
		self.text =  text
		self.qType =  qType
		self.options = []

	def add_option(self, option):
		self.options.append(option)
