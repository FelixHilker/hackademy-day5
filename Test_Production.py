import unittest
import production

class TestProduction(unittest.TestCase):

<<<<<<< Updated upstream
    def test_remove_duplicates(self):
        input = [1,2,2,1]
        output = [1,2]
        self.assertListEqual(output,production.remove_duplicates(input))
=======
    def square(self):

        self.assertEqual(5,25)
        self.assertEqual(0,0)
        self.assertEqual(-2,'Error')
        self.assertEqual('a','Error')

>>>>>>> Stashed changes

if __name__ == '__main__':
    unittest.main()
    
