
"""
line_lis = list(line)
nuevo = list()
line_lis = [x.lower() for x in line_lis]
line_lis.sort()
for i in xrange(len(line_lis)):   #length of the line


    if line_lis[i] not in nuevo:        #check if the letter exists
        nuevo.append(line_lis[i])          #add letter
        nuevo.append("1")                  #add ocurrance

    elif line_lis[i] in nuevo:
        index_ = nuevo.index(line_lis[i])    #find index of value
        current_val = nuevo[index_+1]            #number of ocurrances
        num = int(current_val)
        num += 1
        nuevo[index_+1] = str(num)
    print nuevo
car = ''.join(nuevo)
print car,


line = "hello"

line_lis = list(line)
nuevo = list()
line_lis = [x.lower() for x in line_lis]
line_lis.sort()
for i in xrange(0, len(line_lis)):          #length of the line

    if line_lis[i] not in nuevo:            #check if the letter exists
        nuevo.append(line_lis[i])           #add letter
        nuevo.append("1")                   #add ocurrance

    elif line_lis[i] in nuevo:
        index_ = nuevo.index(line_lis[i])   #find index of value
        current_val = nuevo[index_+1]       #number of ocurrances
        num = int(current_val)
        num += 1
        nuevo[index_+1] = str(num)

line = ''.join(nuevo)
print line,
"""

car = ["carros","hello","blanco","mmmmmMMMMmmm","AndRomeda"]
for line in car:

    line_lis = list(line)                       #the list is including an extra character at the beggining
    nuevo = list()
    line_lis = [x.lower() for x in line_lis]
    line_lis.sort()
    for i in xrange(0, len(line_lis)):          #length of the line

        if line_lis[i] not in nuevo:            #check if the letter exists
            nuevo.append(line_lis[i])           #add letter
            nuevo.append("1")                   #add ocurrance

        else:
            index_ = nuevo.index(line_lis[i])   #find index of value
            num = int(nuevo[(index_)+1]) + 1
            nuevo[index_+1] = str(num)

    line = ''.join(nuevo)
    print line
