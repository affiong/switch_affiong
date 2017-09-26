
def calculateArea(length,breath):
        if str.isdigit(length)and str.isdigit(breath):
            return length*breath
        else:
            print("please enter a value")
            return False
##calculateArea(5,7)



def calcarea():
    length = input ("enter length: ")
    
    breath = input ("enter breath: ")
    #check values
    while not str.isdigit(length)and not str.isdigit(breath):
        length = input("enter length: ")
        breath = input("enter breath: ")
        print("===please enter a value: ===")
    else:
        length = int(length)
        breath = int(breath)
        Area = length*breath
        print("the are of the shape is", Area)

calcarea()
