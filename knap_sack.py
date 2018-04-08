import random

def generate_random_item_list(list_length, max_weight, max_value):
	item_list = []
	for item in range(list_length):
		new_item = knap_sack_item( weight = random.randint(1, max_weight + 1), value = random.randint( 1, max_value + 1 ) )
		item_list.append( new_item ) 
	return item_list




class knap_sack_item():
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value
