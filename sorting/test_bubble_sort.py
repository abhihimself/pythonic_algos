import bubble_sort
import unittest

class test_bubble(unittest.TestCase):
    def setUp(self):
        self.test_list1 = [3, 2, 1]
        self.test_list2 = [1, 2, 3, 4, 5]
        self.test_list3 = [55, 89, 22, 34, 10000, 74]


    def test_reverse_list(self):
        out_list=bubble_sort.get_list(self.test_list1)
        self.assertListEqual(out_list,[1,2,3])

    def test_random_list(self):
        out_list=bubble_sort.get_list(self.test_list3)
        self.assertListEqual(out_list,[22,34,55,74,89,10000])