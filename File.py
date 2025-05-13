#r, #w, r+, w+
a=open("file.txt","r")
content=a.read()
a.close()
#Add text after position 4
content2=content[:4]+"Meow"+content[4:]
#a.seek(0) #Ставит указатель в начало
print(content2)