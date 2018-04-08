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

class construct_item_weight_array_test( unittest.TestCase ):
	"""test for the construct_item_weight_array_function"""

	def setUp( self ):
		self.input_items = [ knap_sack.knap_sack_item( weight = 10, value = 10 ), knap_sack.knap_sack_item( weight = 8, value = 8 ), knap_sack.knap_sack_item( weight = 6, value = 6) ]
		self.output_array = knap_sack.construct_item_weight_array( item_list = self.input_items, max_weight = 14 )

	def test_array_list_length( self ):
		self.assertEqual( 4, len( self.output_array ) )

	def test_zeroith_list_element_for_zeros( self ):
		self.assertEqual( ( [0] * ( 14 + 1 ) ), self.output_array[0] ) 

if __name__ == '__main__':
	unittest.main()
