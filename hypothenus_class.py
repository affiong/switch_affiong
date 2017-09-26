def findside(side_unknown, known_a, known_b):
    '''hyp, adj or opp'''
    sidelist =["hyp","adj", "opp"]
    if side_unknown in sidelist:
        if side_unknown == "hyp":
            hyp =(known_a ** 2 + known_b ** 2)**0.5
            
            
        elif side_unknown == "adj":
            adj =(known_a ** 2 - known_b ** 2)**0.5
            
        else:
            opp =(known_a ** 2 - known_b ** 2)**0.5

    else:
        print("invalid input")
    return 



unknown = input("please enter hyp, adj opp: " )
known_1 = int(input("please enter a value for side b: " ))
known_2 = int(input("please enter a value for side c: " ))
             
print(findside(unknown,known_1,known_2))           
