import unittest
from unittest.mock import patch
from metaclass import CustomMeta
from custom_list import CustomList


class TestList(unittest.TestCase):

    def test_add(self):
        Ob1 = CustomList([1, 2, 3])
        Ob2 = CustomList([2, 4, 5])
        Ob3 = Ob1 + Ob2
        Ob4 = Ob1 + [2]
        Ob5 = [1, 4] + Ob1
        self.assertEqual(Ob3, [3, 6, 8])
        self.assertEqual(Ob4, [3, 2, 3])
        self.assertEqual(Ob5, [2, 6, 3])

    def test_sub(self):
        Ob1 = CustomList([1, 2, 3])
        Ob2 = CustomList([2, 4, 5])
        Ob3 = Ob1 - Ob2
        Ob4 = Ob1 - [2]
        Ob5 = [1, 4] - Ob1
        self.assertEqual(Ob3, [-1, -2, -2])
        self.assertEqual(Ob4, [-1, 2, 3])
        self.assertEqual(Ob5, [0, 2, -3])

    def test_compare(self):
        Ob1 = CustomList([1, 2, 3])
        Ob2 = CustomList([2, 4, 5])
        Ob3 = CustomList([6])
        self.assertTrue(Ob1 < Ob2)
        self.assertFalse(Ob1 > Ob2)
        self.assertTrue(Ob1 != Ob2)
        self.assertTrue(Ob1 <= Ob2)
        self.assertFalse(Ob1 >= Ob2)
        self.assertTrue(Ob1 == Ob3)


class TestMeta(unittest.TestCase):

    def test(self):
        class CustomClass(metaclass=CustomMeta):
            x = 50

            def line(self):
                return 100

        inst = CustomClass()

        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_line(), 100)

        with self.assertRaises(Exception):
            inst.x
            inst.line()



if __name__ == '__main__':
    unittest.main()
