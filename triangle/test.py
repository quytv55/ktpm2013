import unittest
import math

from triangle import detect_triangle

class test(unittest.TestCase):
    def testEquilateral(self):
        result = detect_triangle(2, 2, 2)
        self.assertEquals(result, 'equilateral triangle.')

    def testIsoceles_ab(self):
        result = detect_triangle(2, 2, 1)
        self.assertEquals(result, 'isoceles triangle.')
    
    def testIsoceles_ac(self):
        result = detect_triangle(2, 1, 2)
        self.assertEquals(result, 'isoceles triangle.')
     
    def testIsoceles_bc(self):
        result = detect_triangle(1, 2, 2)
        self.assertEquals(result, 'isoceles triangle.')

    def testSquare_ab(self):
        result = detect_triangle(3, 4, 5)
        self.assertEquals(result, 'square triangle.')
        
    def testSquare_bc(self):
        result = detect_triangle(5, 4, 3)
        self.assertEquals(result, 'square triangle.')
        
    def testSquare_ac(self):
        result = detect_triangle(3, 5, 4)
        self.assertEquals(result, 'square triangle.')

    def testIsoceles_square_ab(self):
        result = detect_triangle(1, 1, math.sqrt(2))
        self.assertEquals(result, 'isoceles square triangle.')
        
    def testIsoceles_square_bc(self):
        result = detect_triangle(math.sqrt(2), 1, 1)
        self.assertEquals(result, 'isoceles square triangle.')

    def testIsoceles_square_ac(self):
        result = detect_triangle(1, math.sqrt(2), 1)
        self.assertEquals(result, 'isoceles square triangle.')
        
    def testScalene(self):
        result = detect_triangle(3, 6, 5)
        self.assertEquals(result, 'scalene triangle.')
        
    def testNot_triangle_ab(self):
        result = detect_triangle(1, 1, 10)
        self.assertEquals(result, 'not triangle.')

    def testNot_triangle_ac(self):
        result = detect_triangle(1, 10, 1)
        self.assertEquals(result, 'not triangle.')

    def testNot_triangle_bc(self):
        result = detect_triangle(10, 1, 1)
        self.assertEquals(result, 'not triangle.')
        
    def testData_notvalid_a(self):
        result = detect_triangle(-1, 2, 1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_b(self):
        result = detect_triangle(1, -2, 1)
        self.assertEquals(result, 'data not valid.')
        
    def testData_notvalid_c(self):
        result = detect_triangle(1, 2, -1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_ab(self):
        result = detect_triangle(-1, -2, 1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_ac(self):
        result = detect_triangle(-1, 2, -1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_bc(self):
        result = detect_triangle(1,- 2, -1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_abc(self):
        result = detect_triangle(-1, -2, -1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_a1(self):
        result = detect_triangle(2**32, 2, 1)
        self.assertEquals(result, 'data not valid.')

    
    def testData_notvalid_b1(self):
        result = detect_triangle(2, 2**32, 1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_c1(self):
        result = detect_triangle(2, 1, 2**32)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_a2(self):
        result = detect_triangle('q', 2**32, 1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_b2(self):
        result = detect_triangle(2, 'q', 1)
        self.assertEquals(result, 'data not valid.')

    def testData_notvalid_c2(self):
        result = detect_triangle(2, -2, 'q')
        self.assertEquals(result, 'data not valid.')  

if __name__== '__main__':
    unittest.main()