sentence="Hi how are you"
inlist=sentence.split(" ")
#print(inlist)
outlist=[]

for word in inlist:
    tmp=''
    for letter in reversed(word):
        #print(letter)
        tmp=tmp+letter
    outlist.append(tmp)

print(" ".join(outlist))
