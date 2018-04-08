from random import randint


def make_random_node_list(size):
	return_list = []
	for i in range(size):
		return_list.append( Node(randint(1,10), randint(1,10) ) )
	return return_list

class Node:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

	def __str__(self):
		return "Value: ${self.value} Weight: ${self.weight}"



