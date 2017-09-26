the_list = ["James" ,75, ["first", "baby"],("football", "orange",),{"position": "first"}]

##def extract_list(item_list):
 ##   for item in item_list :
 ##       print(item)




##extract_list (the_list)





def extract_list(item_list):
    for item in item_list :
        if type(item)==list or type(item)== tuple:
            for item_b in item:
                print (item_b)
                
        elif type(item )==dict:
            ##for item_c in item:
                  ##print(item_c.key, item_c.value)
                for key, value in item_list:
                    print(key, value)
        else:
              print (item)



extract_list (the_list)


              






