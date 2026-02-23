class Cart:
	def __init__(self):
		self.items = {} 


	def addItem(self, product, quantity):

		if product.product_id in self.items:
			self.items[product.product_id].quantity += quantity

		else:
			self.items[product.product_id] = CartItem(product, quantity) 


	def removeItem(self, product_id):
		self.item.pop(product_id, None)

	def updateQuantity(self, product_id, quantity):
		for product_id in self.items:
			self.items[product_id].quantity =  quantity
			

