def checkPerm(first,second):
    dict={}
    dict1={}
    for i in first:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in second:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print dict
    print dict1
    if len(dict)==len(dict1):
        for i in dict:
            if dict[i]==dict1[i]:
                pass
            else:
                print "Not a Permutation"
                return False
    else:
        print "Not a Permutation"
        return False
    print "is a Permutation"
    return True
checkPerm("Aerate pet area","cab")