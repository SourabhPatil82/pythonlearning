#store multiple items in single variable
#muttable
#store diff datatypes
#ordered collection 


list=[1,'2','a',True]
list.append(False)
print(list)
print(list[3])
print(len(list))


#use of in keyword

if '2' in list:
    print("2 is present")
else:
    print("not present")

#same for string
if 'sou' in 'sourabh':
  print("present")

#list[start:end:jumpindex]
#methds

l=[22,2,211,1,12,3,33]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

print(l.index(211))#1st occurence of index

print(l.count(211))

l2=l.copy()
print(l2)

l.insert(1,333)
print(l)

l.extend(l2)

print(l)