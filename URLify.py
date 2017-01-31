def URLify(string,length):
    final=""
    count=0
    for i in string:
        if i !=" ":
            final+=i
            count+=1
        elif count<length:
            final+="%20"
            count+=3
    return final
print URLify("Mr John Smith  ",13)