list=['a','b','c','d']
#for loop
print(list[0])
for items in list:
    print(items)


#list of list
list1=[["sourabh",20],["Abhisheks",30],["mangesh",80],["Umesh",39]]
for items, ages in list1:
    print (items,"Having \"age\"", ages)

#dictionary
dict1=dict(list1)
print(dict1)

# dict2=dict(list)  ValueError: dictionary update sequence element #0 has length 1; 2 is required
# print(dict2)

print(2,2,2,2,2)

colors=["green","blue","yellwo"]
for items in colors:
    print (items)
    for i in items:
        print(i)


for k in range(10):
    if(k%2==0):
        print(k)

for k in range(1,10):# 1 to 9
    if(k==5):
        break#continue
    print (k)

for k in range (1,12,2):# diff of 2
    print(k)