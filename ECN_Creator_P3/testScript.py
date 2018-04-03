# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:57:54 2018

@author: yuanchueh
"""
#import path
import re

filename = '01-01-VER-1006, Rev. C - Addendum Verification'
fileSearch = re.sub('[-]', ',', filename);
fileSearch = re.sub('[. ]', "", fileSearch).split(',');

def findRevision(filename):
    for x in filename:
        if not x.find('Rev'):
            revision = x[3:len(x)]
            return revision
            
rev = findRevision(fileSearch);
print(rev)