#import path as path
import path
from path import path
import os
import csv
# 2017.01.10 This code is a conversion from the original code written by
# Jim West for Matlab.

def getFolder():
    # Get Current Folder Path to Work In
    # http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
    # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python

    # Bring up a dialog to select a folder path to use. Only called if a
    # folder path is not supplied.
    #import Tkinter as tk
    #import tkFileDialog
    #root = tk.Tk()
    #root.withdraw()
    #file_path = tkFileDialog.askdirectory()
    #file_path = "/home/yuanchueh/Documents/git/msWordReplaceImages"
    #file_path = '/home/yuanchueh/Documents/'
    #file_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.121,share=development/_Quality System/BMDK (New) 2017.08.25/_TO ECN"
    file_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.121,share=development/Customers/00-BMDK/AP Active Projects/ECNXXX AP-001 QMS Updates/Completed"
    return file_path


def getFileList(patternStr='*.*', file_path=None):
    # Get's a list of files matching a search expression in a series of nested folders.
    # Requires path.py
    import os
    # Initialize Variables
    file_return = []

    # Get Current Directory Path to Work In. If one was supplied, do nothing.
    if file_path == None:
        file_path = getFolder()

    file_list = path(file_path) #Get the root file path.
    # Get the list of files in the folder.
    # Walk through the file and get a list of matching files.
    # print "begin walking through directo
    counter = 1
    for f in file_list.walkfiles(pattern=patternStr):
        head, tail = os.path.split(f)
        tail_noext, ext = os.path.splitext(tail)
        #print(tail_noext)
        #file_return.append([tail_noext])
        print(tail)
        file_return.append([tail])
        counter = counter + 1
    #return file_return, file_path, file_detail
    return file_return, file_path

def deconstructFileName(fileStr):
    #filePart = {'customernum:','productnum:','documenttype:','revision:','docname:'}

    return

def documentTypeLookup(docAbbrev):

    #return docType
    return

def writeFile(filelist, savefile):
    with open(savefile, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(filelist)
        print('File created successfully:', savefile)

    return

#---------------Begin Program--------------#
extension_type = '*.pdf'
filename = 'file_list.csv'
print('File:', filename)

filelist, filepath = getFileList(extension_type)
#filelist, filepath, filedetail = getFileList(extension_type)

# filepath = '/home/yuanchueh/Documents/git/ECN_Creator'
#savefilename = '/home/yuanchueh/Documents/' + filename
savefilename = filepath + '/' + filename

writeFile(filelist, savefilename)
#print('  Save Directory:', savefilename)
#with open(savefilename, 'wb') as myfile:
    #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerows(filelist)
#print('File created successfully:', savefilename)
