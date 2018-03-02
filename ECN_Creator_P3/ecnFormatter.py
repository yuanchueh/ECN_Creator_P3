import path as path
import os
import csv
# 2017.01.10 This code is a conversion from the original code written by
# Jim West for Matlab.

#ECN Form Layout
# -- Column Requirements
# 1 Document number
# 2 Document Title / Description
# 4 Training Required
# 5 <BLANK>
# 6 Revision Level From
# 7 Revision Level To
# 8 <BLANK>
# 9 Effectivity-Immediate
# 10 Effectivity-Target Date
# 11 Effectivity-Lot Number
# 12 Effectivity-Other
# 13 <BLANK>
# 14 Change Class
# 15 <BLANK>
# 16 Disposition-On Order
# 17 Disposition-Receiving Inspection
# 18 Disposition-In Stock
# 19 Disposition-Work in Process
# 20 Disposition-Returned Goods

#File Name Requirements
#TYPE-NNNN, Rev. XX, Document Title



def getFolder():
    # Get Current Folder Path to Work In
    # http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
    # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python

    # Bring up a dialog to select a folder path to use. Only called if a
    # folder path is not supplied.
    ##import Tkinter as tk
    ##import tkFileDialog
    ##root = tk.Tk()
    ##root.withdraw()
    ##file_path = tkFileDialog.askdirectory()
    ##file_path = "/home/yuanchueh/Documents/git/msWordReplaceImages"
    file_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.121,share=development/_Quality System/BMDK (New) 2017.08.25/_TO ECN"
    return file_path


def getFileList(patternStr='*.*', file_path=None):
    # Get's a list of files matching a search expression in a series of nested folders.
    # Requires path.py
    import os
    # Initialize Variables
    file_return = []
    from path import path

    # Optional - Display input variables.
    # print 'Input pattern:   ', patternStr
    # print 'Input file path: ', file_path

    # Get Current Directory Path to Work In. If one was supplied, do nothing.
    if file_path == None:
        file_path = getFolder()
        # print 'file path outside =', file_path

    file_list = path(file_path) #Get the root file path.
    # Get the list of files in the folder.
    # Walk through the file and get a list of matching files.
    # print "begin walking through directory"
    counter = 1
    # for f in file_list.walk(pattern=patternStr):
    for f in file_list.walkfiles(pattern=patternStr):
        # print "..walk ", f
        head, tail = os.path.split(f)
        tail_noext, ext = os.path.splitext(tail)
        print("File: ", tail_noext)
        file_return.append([tail_noext])
        # print counter, '-', f
        # print os.path.split(f)
        # head, tail = os.path.split(f)
        # print 'head', head
        # print 'tail', tail
        counter = counter + 1
    return file_return, file_path

extension_type = '*.pdf'
customernum = raw_input("Enter customer number as a number (XX): ")
# customernum = 11
# projectnum = raw_input("Enter project number as a number (YY): ")
# projectnum = 01
ecnnum = raw_input("Enter ECN number as a three digit number (ZZZ): ")
# ecnnum = 001
filename = str(customernum).zfill(2) + '-' + \
    'ECN' + str(ecnnum).zfill(3) + '.csv'
print filename
# print

filelist, filepath = getFileList(extension_type)
# filepath = '/home/yuanchueh/Documents/git/ECN_Creator'
fullfilename = filepath + '/' + filename
print '  Save Directory:', fullfilename
with open(fullfilename, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(filelist)
print "File created successfully:", fullfilename
