import unittest
import production

class TestProduction(unittest.TestCase):

    def test_remove_dublicates(self):
        input = [1,1,2,2]
        output = [1,2]
        self.assertEqual(output,production.remove_dublicates(input),)

if __name__ == "__main__":
    unittest.main()