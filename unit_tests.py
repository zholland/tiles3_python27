import unittest
import random
import tiles3 as tc


class TestBasicUse(unittest.TestCase):
    def setUp(self):
        random.seed(123)
        self.iht = tc.IHT(1024)

    def test_first_insert(self):
        indices = tc.tiles(self.iht, 8, [3.6, 7.21])
        self.assertEquals(indices, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_multiple_inserts(self):
        indices = tc.tiles(self.iht, 8, [3.6, 7.21])
        self.assertEquals(indices, [0, 1, 2, 3, 4, 5, 6, 7])
        indices = tc.tiles(self.iht, 8, [3.7, 7.21])
        self.assertEquals(indices, [0, 1, 2, 8, 4, 5, 6, 7])
        indices = tc.tiles(self.iht, 8, [4, 7])
        self.assertEquals(indices, [9, 10, 11, 8, 4, 12, 6, 7])
        indices = tc.tiles(self.iht, 8, [-37.2, 7])
        self.assertEquals(indices, [13, 14, 15, 16, 17, 18, 19, 20])

    def test_repeat_same_coords(self):
        indices1 = tc.tiles(self.iht, 8, [3.6, 7.21])
        tc.tiles(self.iht, 8, [4, 7])
        indices2 = tc.tiles(self.iht, 8, [3.6, 7.21])
        self.assertEquals(indices1, indices2)

if __name__ == '__main__':
    unittest.main()
