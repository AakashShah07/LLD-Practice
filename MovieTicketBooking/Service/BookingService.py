class BookingService(self):
	def __init__():
		self.bookings  = []

	def book_service(self, show, seat_ids):
		seleted_seat = []

		for seat in show.screen.seats:
			if seat.seat_id in seat_ids:
				if seat.is_booked():
					return None

				seleted_seat.append(seat)


		for i in seleted_seat:
			i.is_booked = True

		booking  = Booking(show, seleted_seat)

		self.bookings[bookings.booking_id] =  booking

		return booking 

