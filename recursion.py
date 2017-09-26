the_list = ["James" ,75, ["first", "baby"],["me","myself"],["apple","grapes"],("football", "orange",),{"position": "first"}]

def extract_list(item_list):
    for item in item_list :
        if type(item)==list or type(item)== tuple:
            extract_list(item)
            print(item)


        if type(item)== dict:
            extract_list(item)
            print(item)
     
