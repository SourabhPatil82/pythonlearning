var="""fjfhjdgfhsfhgfhfhfdfgggggggg/ngggggggggggggggggggggg
ggggg"""

print(var)
name="mango"
print(name[1])
print(name[2:5])
print(name[:])#0 to 4
print(name[:4])
print(name[0:-3])#0:len(name)-3  sour
print(name[-3:-1])#2:4

name1="harry  hjj>>>>>>>>>>>>>>>>>>>>>"
print(name1[-4:-2])#5-4:5-2====>1:3



print(name1.upper())
print(name1.lower())
print(name1.strip())
print(name1.rstrip(">"))#only trailing values removed
print(name1.replace("hjj","kss"))
print(name1.split(" "))#split in lista
print(name1.capitalize())
print(name1.endswith(">>"))
print(name1.count("hl"))