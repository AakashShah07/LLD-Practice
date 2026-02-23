class Show:
	def __init__(self, show_id, movie, screen, time):
		self.show_id = show_id
		self.movie = movie
		self.screen = screen
		self.time = time

	def get_available_seats(self):
		return [seat for seat in self.screen.seats is not seat.is_booked()]