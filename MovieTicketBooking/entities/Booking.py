import uuid

class Booking(object):
	"""docstring for Booking"""
	def __init__(self, show, seats):
		self.id  = str(uuid.uuid4())
		self,show  = show
		self.seats = seats