import os, os.path
import re
from stat import *

def find(where='.*', content=None, start='.', ext=None, logic=None):
    print("begin")
    context = {}
    context['where'] = where
    context['content'] = content
    context['return'] = []
    os.path.walk(start, find_file, context)
    return context['return']
    
def find_file(context, dir, files):
    for file in files:
        print("starting to find")
        # Find out things about this file.
        path = os.path.join(dir, file)
        path = os.path.normcase(path)
        try:
           ext = os.path.splitext(file)[1][1:]
        except:
           ext = ''
        stat = os.stat(path)
        size = stat[ST_SIZE]
        
        # Don't treat directories like files
        if S_ISDIR(stat[ST_MODE]): continue
        
        # Do filtration based on the original parameters of find()
        if not re.search(context['where'], file): continue
        
        # Do content filtrat last, to avoid it as much as possible
        if context['content']:
            f = open(path, 'r')
            match = 0
            for l in f.readlines():
                if re.search(context['content'], l):
                     match = 1
                     break
            f.close()
            if not match: continue  
            
    # Build the return value for any files that passed the filtration test.
    file_return = (path, file, ext, size)
    context['return'].append(file_return)               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                  