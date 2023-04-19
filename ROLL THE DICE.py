import random
response="y"
while response =="y":
    no=random.randint(1,6)
    if no==1:
        print("1 is printed")
    if no==2:
        print("2 is printed")
    if no==3:
        print("3 is printed")
    if no==4:
        print("4 is printed")
    if no==5:
        print("5 is printed")
    if no==6:
        print("6 is printed")
    response=input("press y to roll again and n to exit")
    print("\n")
