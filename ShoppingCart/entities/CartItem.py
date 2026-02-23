class CartItem:
	def __init__(self, product, quantity):
		self.product  = product
		self.quantity  = quantity


	def calculate_price(self):
		return self.product.price * self.quantity
		