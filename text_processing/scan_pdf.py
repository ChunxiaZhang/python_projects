import os, os.path
import re

def print_pdf(root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)   #lowercase
        if not re.search(r".*\.pdf", path): continue
        if re.search(r".*\.pdf", path):
            print(path)
  
# Use the os.walk function to traverse the file system            
for root, dirs, files in os.walk('.'):
    print_pdf(root, dirs, files)              
            
            
            
"""
Regular expression:
1. '.' any one character in a string. 'x.x' will match the strings 'xxx', 'xyx', 'x.x';
2. r"x\.x" matches 'x.x'
"""            