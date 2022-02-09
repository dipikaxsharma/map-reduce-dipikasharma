#dipika Sharma
f = open("indian_food.csv","r")  # open file, read-only
o = open("foodprepmap.txt", "w") # open file, write
for line in f:  
    dataList = line.strip().split(",") 
    # print (dataList )
    # print (len(dataList ))
    if len(dataList) == 9:
        name,ingredients,diet,prep_time,cook_time,flavor_profile,course,state,region = dataList  #assign names
       #print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{3}\n".format(name, prep_time))
f.close()
o.close()