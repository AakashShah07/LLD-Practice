class PricingService:
	def calculatePrice(self, cart, coupon=None):
		total =  sum(item.get_total_price() for item in cart.items.values())
		if coupon:
			dis  = total * coupon.discount / 100
			total -=dis

		return total