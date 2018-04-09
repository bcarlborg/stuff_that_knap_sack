import unittest
import knap_sack

class generate_random_item_list_test( unittest.TestCase ):
	"""tests for the item list generator"""

	def test_item_list_lenght( self ):
		"""is the length of the output list 5"""
		item_list = knap_sack.generate_random_item_list( list_length = 5, max_weight = 10, max_value = 10 )
		self.assertEqual( 5, len( item_list ) )

	def test_empty_list_length( self ):
		"""tests an empty input list"""
		item_list = knap_sack.generate_random_item_list( list_length = 0, max_weight = 10, max_value = 10 )
		self.assertEqual( 0, len( item_list ) )


class sort_item_list_test( unittest.TestCase ):
	"""tests for sorting the input array of items"""
	
	def test_sort_list_of_four_nodes( self ):
		input_items = [ knap_sack.knap_sack_item( weight = 4, value = 5 ), knap_sack.knap_sack_item( weight = 3, value = 6 ), knap_sack.knap_sack_item( weight = 2, value = 1), knap_sack.knap_sack_item( weight = 1, value = 4) ]
		expected_output = [ knap_sack.knap_sack_item( weight = 1, value = 4), knap_sack.knap_sack_item( weight = 2, value = 1), knap_sack.knap_sack_item( weight = 3, value = 6 ), knap_sack.knap_sack_item( weight = 4, value = 5 ) ] 
		output_list = knap_sack.sort_item_list( input_items )
		self.assertEqual( output_list, expected_output )


class construct_item_weight_array_test( unittest.TestCase ):
	"""test for the construct_item_weight_array_function"""

	def setUp( self ):
		self.input_items = [ knap_sack.knap_sack_item( weight = 10, value = 10 ), knap_sack.knap_sack_item( weight = 8, value = 8 ), knap_sack.knap_sack_item( weight = 6, value = 6) ]
		self.output_array = knap_sack.construct_item_weight_array( item_list = self.input_items, max_weight = 14 )

	def test_array_list_length( self ):
		self.assertEqual( 4, len( self.output_array ) )

	def test_zeroith_list_element_for_zeros( self ):
		self.assertEqual( ( [0] * ( 14 + 1 ) ), self.output_array[0] ) 

class find_optimal_packing_test( unittest.TestCase ):
	"""tests the optimal packing algorithm for expected results"""

	def setUp( self ):
		self.input_items_one = [ knap_sack.knap_sack_item( weight = 4, value = 5 ), knap_sack.knap_sack_item( weight = 3, value = 6 ), knap_sack.knap_sack_item( weight = 2, value = 1), knap_sack.knap_sack_item( weight = 1, value = 4) ]
		self.output_one = knap_sack.find_best_packing( input_list = self.input_items_one, max_weight = 10 )

		self.input_items_two = [ knap_sack.knap_sack_item( weight = 1, value = 10), knap_sack.knap_sack_item( weight = 3, value = 5), knap_sack.knap_sack_item( weight = 5, value = 5) ]
		self.output_two = knap_sack.find_best_packing(input_list = self.input_items_two, max_weight = 8)

	def test_find_optimal_value_for_4_elements( self ):
		self.assertEqual(16, self.output_one[0])

	def test_find_optimal_pairing_for_4_elements( self ):
		self.assertEqual(self.input_items_one, self.output_one [1])



if __name__ == '__main__':
	unittest.main()
