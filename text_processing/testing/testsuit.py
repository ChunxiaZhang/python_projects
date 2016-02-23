import unittest

# subclass of TestCase
class ArithTest(unittest.TestCase):

# runTest performs the actual testing
    def runTest(self):
        """Test addition and succeed."""
        self.failUnless(1+1==2, 'one plus one fails!')
        self.failIf(1+1!=2, 'one pluse on fails again!')
        self.failUnlessEqual(1+1, 2, 'more trouble with one plus one!')
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ArithTest())
    return suite
    
class ArithTestFail(unittest.TestCase):
    def runTest(self):
       """Test addition and fail.""" 
       self.failUnless(1+1==2, 'noe plus one fails!')
       self.failIf(1+1!=2, 'one plus one fails again!')
       self.failUnlessEqual(1+1, 2, 'more trouble with one plus one!')
       self.failIfEqual(1+1, 2, 'expected failure here')
       self.failIfEqual(1+1, 2, 'second failure')
          
def suite_2():
    suite = unittest.TestSuite()
    suite.addTest(ArithTest())
    suite.addTest(ArithTestFail())
    return suite
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite_2()
    runner.run(test_suite)            