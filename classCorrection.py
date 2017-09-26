print("===AreaTriangle===")
print()


height = input("please enter height of the triangle: ")
if str.isdigit(height)==True:
    height = int(height)
else:
    print("please enter a digit")
base = input ("please enter base of the triangle: ")
if str.isdigit(base)==True:
    base = int(base)
else:
    print("please enter a digit")    

print()

area = (base * height)/2

print ("area of a triangle is", area)



