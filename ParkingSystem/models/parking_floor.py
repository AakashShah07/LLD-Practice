class ParkingFlor:
	"""docstring for ClassName"""
	def __init__(self, floorNo, spots):

		self.floorNo =  floorNo
		self.spots = spots

	def find_spot(self, vehicle):
		for spot in self.spots:
			if spot.vehicle is None and spot.can_fit(vehicle):
				return spot

		return None
		