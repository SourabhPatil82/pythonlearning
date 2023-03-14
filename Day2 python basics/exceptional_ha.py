a=input("Enter the no")
try:
 for i in range(1,11):
    print(i*int(a))
#except:
  #print("error")
 l=[1,2]
 b=int(a)
 print(l[b])


except ValueError:
  print("I cathced specific value error")

except IndexError:
  print("Index error catched ")

  
except Exception as e:
  print("in catch block",e)

finally:
  print("In finally block to cleanup things")


# before function can retrun finally always runs
print("code is survived")