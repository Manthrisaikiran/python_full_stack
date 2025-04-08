'''what is file handling:
    
pytho, file operation such as opening a file,reading from it,writing into it,closing it,renaming a file, deleting a file,and various file methods

Modes of Files:

r: open an existing file for a read operation.

w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.

a: open an existing file for append operation. It won't override existing data.

r+: In r+ mode, we can read and write the file, but the file pointer position is at the beginning of the file; if we write the file directly, it will overwrite the beginning content.

w+: To write and read data. It will override existing data'''


""" File Methods

read() Returns the file content.readline()

Read single line readlines() Read file into a list

write() Writes the specified string to the file.

writelines() Writes a list of strings to the file.

close() Closes the opened file.

seek() Set file pointer position in a file

tell() Returns the current file location."""



'''  read links on 8.1file.txt  line no 1 . read reads total data   '''
# file=open("8.1file.txt",mode="r")
# c=file.read()
# print(c)
# file.close()

'''readline reads only single line'''
# file=open("8.1file.txt",mode="r")
# c=file.readline()
# print(c)
# file.close()

'''readlines convert data into list'''
# file=open("8.1file.txt",mode="r")
# c=file.readlines()
# print(c)
# file.close()



# file=open("8.1file.txt",mode="r")
# c=file.read(7)
# print(c)
# file.close()


'''note: if we want access only single bnbn word first we want to convert into list and use index what is want to access'''
'''this write function replace the data so previus data will lose inorder to over come use append function'''
# file=open("8.1file.txt",mode="w")
# c=file.write('this is write function')
# file.close()


'''using append data will not loss'''
# file=open("8.1file.txt",mode="a")
# c=file.write('this is append mode')
# file.close()




'''reading file in r+ mode:'''

# with open('8.1file.txt',"r+") as fd:
#  print(fd.tell())
#  print(fd.read())
#  print(fd.tell())


'''first read then after write so we can able to know where is pointer start and reads'''
# with open('8.1file.txt',"w+") as fd:
#  print(fd.tell())
#  c=fd.write("this is w+")
#  print(fd.read())
#  print(fd.tell())


'''write file in 'r+' mode '''
# with open('8.1file.txt','r+') as fd:
#     fd.write("new 23text.")


''' note: 
in r+ mode  first we want to read and after write
in w+ mode  first we want to write and after read '''


'''creating file with 'w+' mode when it does not existed in file'''
# with open ('8.2file.txt','w+')as fd:
#     pass



'''seek() function is used to change the position of thhe file handle to given specific  position.
file handle is like a cursor,which defines from where the data has to be read or written in the file.
f.seek(0)
move file pointer to the beginning of a file.
tell will tells the position.
seek will change the position.
'''

# fd=open('8.1file.txt','r')
# print(fd.tell())
# fd.read(2)
# #position handling
# print(fd.tell())
# fd.seek(0)
# print(fd.tell())
# #closing file
# fd.close()



''' string-split-list-join-string'''
"""string-readlines->list-writeliness->string"""
# file=open('8.1file.txt',mode='r+')
# content=file.read()
# v=str(content)
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'manthri')
# print(file.tell())
# file.close()
# file=open('8.1file.txt',mode='w')
# print(f)
# for i in f:
#     file.writelines([i])

"""file handling functions:

read: used for read total data
writ:write data
writelines: list to string convert
readline: only first line reads
readlines: string to list
seek: changes the position
tell: current position
close: file close
open: file open
"""