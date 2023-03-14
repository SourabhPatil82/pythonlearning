# r=read(default) ---> if file not exists then gives error


# w=write------>If file not present the creates

# a=append ----->If file not present the creates

f=open("myfile.txt","r")#rt or rb depends on text and binary file

content=f.read()

print(content)

f.close()


# f=open("myfile.txt","r")
# while True:
#     line=f.readlines()
#     if not line:
#         break
#     print(line)