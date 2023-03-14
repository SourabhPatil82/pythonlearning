def welcome():
    print("im from myfile")
    print(__name__)  

if __name__=="__main__":#not to execute twice when impoted in otherr files
  welcome()