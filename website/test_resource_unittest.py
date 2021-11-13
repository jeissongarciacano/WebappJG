import unittest
import resource

class Testroutes(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(resource.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] , "Should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")

    def test_factorial(self):
        self.assertEqual(resource.factorial(50), 30414093201713378043612608166064768844377641568960512000000000000, "30414093201713378043612608166064768844377641568960512000000000000")

    def test_triangulo(self):
        self.assertEqual(resource.APtriangulo(6,8,9),(23.525252389719434,23), "Should be (23.525252389719434,23)")

    def test_rectangulo(self):
        self.assertEqual(resource.APrectangulo(4,5), (20,18), "Should be (20,18)")
    
    def test_circulo(self):
        self.assertEqual(resource.APcirculo(5), (78.53981633974483,31.41592653589793), "Should be (78.53981633974483,31.41592653589793)")

if __name__ == '__main__':
    unittest.main()
