dict={#ordered collection 

"key1":"value1",
"key2":"value2"

}

print(dict["key1"])

print(dict["key2"])#throwing err in key not present 

print(dict.get("key5"))#not throwing error 

dict["key3"]="value3"

for items in dict:
    print(items)


print(dict.keys())
print(dict.values())
print(dict.items())


dict2={"name":"sourabh","surname":"patil"}

dict.update(dict2)
print(dict)


dict2.pop('surname')

print(dict2)