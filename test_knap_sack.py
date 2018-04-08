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
		self.assertEqual( 0, len(item_list) )




if __name__ == '__main__':
	unittest.main()
