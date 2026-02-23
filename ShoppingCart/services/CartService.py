class  CartService:
	def __init__(self):
		self.carts = {}
		self.coupons = {
			"10SAVE":Coupon("10SAVE", 10),
			"20SAVE":Coupon("20SAVE", 20)
		}


	def get_carts(self, userId):
		if userId not in self.carts:
			self.carts[userId] = Cart()

		return self.carts[userId]

	def add_items(self, userId, product, quantity):
		cart = self.get_carts[userId]
		cart.add_items(product, quantity)

	def removeItem(self, userId, productId):

		self.get_carts(userId).remove_item(productId)


	def apply_coupon(self, user_id, coupon_code):
        return self.coupons.get(coupon_code)

    def checkout(self, user_id, coupon_code=None):
        cart = self.get_cart(user_id)
        coupon = self.coupons.get(coupon_code) if coupon_code else None
        return PricingService().calculate_total(cart, coupon)



