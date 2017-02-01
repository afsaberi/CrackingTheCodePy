def isPalinPerm(string):
    dict={}
    print len(string)-string.count(" ")
    for i in string:
        if i !=" ":
            if i.lower() in dict:
                dict[i.lower()]+=1
            else:
                dict[i.lower()]=1
    print dict
    count=0
    for i in dict:
        if i !=" ":
            if dict[i] % 2==0:
                pass
            else:
                count+=1
    if len(string)-string.count(" ") %2==0:
        if count==0:
            print count
            print "is palindrome permutation"
            return True
        else:
            print count
            print "is not palindrome permutation"
            return False
    else:
        if count>1:
            print count
            print "is not palindrome permutation"
            return False
        else:
            print count
            print "is palindrome permutation"
            return True

isPalinPerm("Emu love volume")