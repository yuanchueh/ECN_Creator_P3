                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    filename = '01-01-HA-1000-CE, Rev D - LTS-2 Hazard Analysis.xlsx'
print(filename)
filename_split = filename.split('-')
print(filename_split)

#Find Customer number
print('Customer Number:', filename_split[0])
cust_num = filename_split[0]

#Find Product number
print('Product Number:', filename_split[1])
prod_num = filename_split[1]

#Find Document Type
print('Document Type:', filename_split[2])
doc_type = filename_split[2]

#Find Revision
filename_rev = filename.replace('.','').replace(' ','').lower()
rev_index = filename_rev.find('rev')
rev = filename_rev[rev_index+3].upper()
print('Revision:', rev)
#print(filename.replace('.','').replace(' ','').lower())

#Find Document Number
print('Document Number')
docnum_iStart = filename.find(doc_type)+len(doc_type)+1
docnum_iStop = filename.find(',')
docnum_index = ''.join(filename_split[3:])
print('Document Number:', filename[docnum_iStart:docnum_iStop])

#Find Document Title
doc_title = ''.join(filename_split[5:])
ext_index = -doc_title[::-1].find('.')-1 #Reverse the string and find the first period.
doc_ext = doc_title[ext_index:]


doc_title = doc_title[:ext_index].strip()

print('Document Title:', doc_title)
print('Document Extension', doc_ext)
