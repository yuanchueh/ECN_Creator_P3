import path as path
import os
import csv
# 2017.01.10 This code is a conversion from the original code written by
# Jim West for Matlab.
# This is written on 2018.01 for the purpose of getting the WO number from a list of files into a spreadsheet

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
    #file_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.121,share=development/_Quality System/BMDK (New) 2017.08.25/_TO ECN"
    file_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.121,share=development/Customers/01-Novian Health/Log Items/WO Work Orders"
    return file_path

def getFileList(patternStr='WO*.*', file_path=None):
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
        number = tail_noext.split(' ')
        print("Split: ", number[1])
        #print("File: ", tail_noext)
        file_return.append([tail_noext])
        #test = tail_noext
        #rint("Split: ", test)
        # print counter, '-', f
        # print os.path.split(f)
        # head, tail = os.path.split(f)
        # print 'head', head
        # print 'tail', tail
        counter = counter + 1
    return number[1], file_path


filename = 'work order list.csv'
print filename

extension_type = '*.doc'
filelist, filepath = getFileList(extension_type)
# filepath = '/home/yuanchueh/Documents/git/ECN_Creator'
fullfilename = filepath + '/' + filename
print '  Save Directory:', fullfilename
with open(fullfilename, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(filelist)
print "File created successfully:", fullfilename
