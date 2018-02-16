import unittest
import production

class TestProduction(unittest.TestCase):

    def TestThreenumbers(self):
        input = [1,57,7]
        output = 8
        self.assertEqual(output,Threenumbers.threenumbers(input))
        input = [-10,10,2]
        output = 10
        self.assertEqual(output,Threenumbers.threenumbers(input))
        input = [-7.8,2,1.5]
        output = 6
        self.assertEqual(output,Threenumbers.threenumbers(input))
        input = [2,-7.8,1.5]
        output = 7
        self.assertEqual(output,Threenumbers.threenumbers(input))

if __name__ == '__main__':
    unittest.main()
