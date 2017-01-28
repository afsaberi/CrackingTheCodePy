def isUnique(string):
    string=string
    list=[]
    for i in string:
        if i in list and i !=" ":
            print "not unique"
            return False
        else:
            list.append(i)
    print "Is unique"
    return True
isUnique("This a et")