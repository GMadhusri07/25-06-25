# Task: create text file, add some text , print first Character of every line
file=open("sample.txt","r")
lines=file.readlines()    #reads all lines into a list
word=""                  #initialize  empty string to collect first letters
for i in lines: #iterates lines in list
    if i.strip():
     letter=i[0]      #first character of each line stored in letter
     word+=letter      #J w G I G H R
print( word)
file.close()

# output---JwGIGHR