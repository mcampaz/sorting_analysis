import unittest
from merge_sort.mergesort import merge_sort


class MergeTestCase(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 2, 3, 4]
        merge_sort(arr1)
        arr2 = [4, 3, 2, 1]
        merge_sort(arr2)
        arr3 = [4, 3, 3, 2, 1]
        merge_sort(arr3)
        self.assertEqual([1, 2, 3, 4], arr1)
        self.assertEqual([1, 2, 3, 4], arr2)
        self.assertEqual([1, 2, 3, 3, 4], arr3)


if __name__ == '__main__':
    unittest.main()
