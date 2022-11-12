import unittest

import calculator as calc


class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-10,5),-5)
        self.assertEqual(calc.add(10,-5),5)
        self.assertEqual(calc.add(-10,-5),-15)


    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(-10,5),-15)
        self.assertEqual(calc.sub(10,-5),15)
        self.assertEqual(calc.sub(-10,-5),-5)


    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)
        self.assertEqual(calc.mul(-10,5),-50)
        self.assertEqual(calc.mul(10,-5),-50)
        self.assertEqual(calc.mul(-10,-5),50)


    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(-10,5),-2)
        self.assertEqual(calc.div(10,-5),-2)
        self.assertEqual(calc.div(-10,-5),2)
        self.assertRaises(ValueError,calc.div,10,0)


if __name__ == '__main__':
    unittest.main()