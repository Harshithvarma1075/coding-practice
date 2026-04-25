#=============================================FILE HANDLING====================================================
#file handler is an object of file to maintain several functions of file such as creating reading ,writinig , and updating also deleting a file

#how to open a file:
'''
1.open()------------if we use this , we have to close it manuallu using close()
    -it takes 2 parameters, file name , mode (append-a,read-r,write-m,create-x,text-t)
    -1.to read the file we will use this mode and if the file doesnot exist it will throw the error ("r")
    -2.to write the text into the file we will use this mode ("w")
    -3.to add the text into the file , this is used and it will creaye the file it it doesnt exist
    -4.this is used to create the file ,but the file is already created then it throws error
2.with open()----------here it closes automatically
'''
'''
varma=open("demo.txt", "r")
print(varma.read())
varma.close()

hi= open("demo.txt","w")
hi.write("today is saturday")   #it is overwriting the contents inside the file
hi.close()

hi = open("demo.txt","a")
hi.write("hi man")
hi.close()

hi=open("demo.txt","x")
hi.close()
'''
#to read file we have three methods
#1.read()------>this method can read the entire file chunk by chunk,we can also specify the size of words to be read
#2.readline()---->this method can only read one line at a time 
#3.readlines()------->this method can read the entire file and return into list with each line as one element in the list




























