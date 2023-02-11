import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right')
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(8,15,17 ), 'Right')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 2),'Isoceles')
    
    def testIsocelesTriangleB(self):     
        self.assertEqual(classifyTriangle(4, 5, 5),'Isoceles')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 5, 1),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,1, 5),'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()