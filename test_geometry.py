import unittest
from geometric_lib import circle, rectangle, square, triangle

class TestRectangle(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_square(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
        
    def test_area_normal(self):
        res = rectangle.area(5, 7)
        self.assertEqual(res, 35)
        
    def test_perimeter_zero(self):
        res = rectangle.perimeter(1, 5)
        self.assertEqual(res, 12) 
        
    def test_perimeter_normal(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
        
    def test_diagonal(self):
        res = rectangle.diagonal(3, 4)
        self.assertAlmostEqual(res, 5.0)
        
    def test_is_square_true(self):
        res = rectangle.is_square(5, 5)
        self.assertTrue(res)
        
    def test_is_square_false(self):
        res = rectangle.is_square(5, 4)
        self.assertFalse(res)

class TestCircle(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0.0)
        
    def test_area_normal(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.14159, places=4)
        
    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0.0)
        
    def test_perimeter_normal(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.28318, places=4)
        
    def test_diameter(self):
        res = circle.diameter(5)
        self.assertEqual(res, 10.0)
        
    def test_sector_area(self):
        res = circle.sector_area(10, 90)
        self.assertAlmostEqual(res, 78.5398, places=4)

class TestSquare(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)
        
    def test_area_normal(self):
        res = square.area(5)
        self.assertEqual(res, 25)
        
    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_perimeter_normal(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
        
    def test_diagonal(self):
        res = square.diagonal(1)
        self.assertAlmostEqual(res, 1.41421, places=4)
        
    def test_inscribed_circle_area(self):
        res = square.inscribed_circle_area(10)
        self.assertAlmostEqual(res, 78.5398, places=4)

class TestTriangle(unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)
        
    def test_area_normal(self):
        res = triangle.area(4, 3)
        self.assertEqual(res, 6)
        
    def test_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        
    def test_perimeter_normal(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
        
    def test_is_equilateral_true(self):
        res = triangle.is_equilateral(5, 5, 5)
        self.assertTrue(res)
        
    def test_is_equilateral_false(self):
        res = triangle.is_equilateral(3, 4, 5)
        self.assertFalse(res)
        
    def test_is_right_triangle_true(self):
        res = triangle.is_right_triangle(3, 4, 5)
        self.assertTrue(res)
        
    def test_is_right_triangle_false(self):
        res = triangle.is_right_triangle(3, 4, 6)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()