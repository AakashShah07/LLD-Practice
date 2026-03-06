class Response:
	def __init__(self, id, form_id):
		self.response_id = id 
		self.form_id =form_id
		self.answers = []

	def add_answer(self, answer):
		self.answers.append(answer)