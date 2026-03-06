class FormController:

	def __init__(self, arg):
		self.forms = {}

	def create_form(self, formId, title, ownerId):
		form = Form(formId, title, ownerId)
		self.forms[formId] = form 
		return form 

	def add_questions(self, formId, question):
		form =  self.forms.get(formId)
		form.add_questions(question)

	def get_form(self, form_id):
		return self.forms.get(form_id)