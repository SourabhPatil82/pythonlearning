x=90

match x:
    case 0:
        print("x is 0")

    case 4:
        print("x is 4")
    case _ if x!=90:                  #when statisfies then stop
        print("x is  not 90")
    case _:
        print("defualt")