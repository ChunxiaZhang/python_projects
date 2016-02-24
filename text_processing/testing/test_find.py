import unittest
import find
import os, os.path

def filename(ret):
    return ret[1]
    
class FindTest(unittest.TestCase):
       def setUp(self):
          os.mkdir("_test")
          print("create folder _test")
          os.mkdir(os.path.join("_test", "subdir"))
          f = open(os.path.join("_test", "file1.txt"), "w")
          f.write("""first line
          second line
          third line
          forth line""")    
          f.close()
       
          f = open(os.path.join("_test", "file2.py"), "w")
          f.write("""This is a test file. 
          It has many words in it. 
          This is the final line.""")
          f.close()
       
       def tearDown(self):
           os.unlink(os.path.join("_test", "file1.txt"))
           os.unlink(os.path.join("_test", "file2.py"))
           os.rmdir(os.path.join("_test", "subdir"))
           os.rmdir("_test")
           
       def test_01_SearchAll(self):
          res = find.find(r".*", start="_test")
          self.failUnless(map(filename,res) == ['file1.txt', 'file2.py'], 'wrong results')   
          
       def test_02_SearcheFileName(self):
          res = find.find(r"file", start="_test")
          self.failUnless(map(filename, res) == ['file1.txt', 'file2.py'], 'wrong results')  
          res = find.find(r"py$", start="_test")
          self.failUnless(map(filename,res) == ['file2.py'], 'Python file search incorrect')
          
       def test_03_SearchByContent(self):
          res = find.find(start="_test", content="first")
          self.failUnless(map(filename,res) == ['file1.txt'], "didn't fine file1.txt") 
          res = find.find(where="py$", start="_test", content="line")
          self.failUnless(map(filename, res) == ['file2.py'], "didn't find file2.py")
          res = find.find(where="py$", start="_test", content="second")
          self.failUnless(len(res) == 0, "found something that din't exist")
          
       def test_04_SearchByExtension(self):
          res = find.find(start="_test", ext='py')
          self.failUnless(map(filename, res) == ['file2.py'], "didn't find file2.py")
          res = find.find(start="_test", ext='txt')
          self.failUnless(map(filename, res) == ['file1.txt'], "didn't find file1.txt")
          
       def test_05_SearchByLogic(self):
          res = find.find(start="_test", logic=lambda x:(x['size'] < 50))
          self.failUnless(map(filename, res) == ['file1.txt'], "failed to find by size")
          
          
if __name__ == '__main__':
    unittest.main()                  
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          