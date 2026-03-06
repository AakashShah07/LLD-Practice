class Form:
	def __init__(self, form_id, title, ownerId):
		self.form_id =form_id
		self.title = title
		self.ownerId =  ownerId
		self.questions  = []
		self.response  = []


	def addQues(self, question):
		self.questions.append(question)

	def addRes(self.res):
		self.response.append(res)