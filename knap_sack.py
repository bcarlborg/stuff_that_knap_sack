import random

def generate_random_item_list(list_length, max_weight, max_value):
	item_list = []
	for item in range(list_length):
		new_item = knap_sack_item( weight = random.randint(1, max_weight + 1), value = random.randint( 1, max_value + 1 ) )
		item_list.append( new_item ) 
	return item_list


def find_best_packing( input_list, max_weight ):
	
	memoized_list = construct_item_weight_array( item_list = input_list, max_weight = max_weight ):
	current_node = 1
	for node in input_list:
		current_weight = 0
		for weight in range( 0, ( max_weight + 1 ) ):
			value_without_curr_node = memoized_list[ (current_node - 1), current_weight ]
			if ( node.weight < current_weight ):
				memoized_list[ current_node, current_weight ] = value_without_curr_node
			else:
				value_with_curr_node = memoized_list[ (current_node - 1), (current_weight - node.weight) ] + node.value 
				memoized_list[current_node, current_weight] = value_with_current_node if (value_with_current_node > value without current_node) else value_without_current_node 


def construct_item_weight_array( item_list, max_weight ):
	output_array = []
	for item in range( 0, len( item_list ) + 1 ):
		output_array.append( [0] * (max_weight + 1) )
	return output_array


class knap_sack_item():
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value
