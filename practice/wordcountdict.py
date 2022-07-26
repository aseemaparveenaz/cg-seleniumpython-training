s = "we dont need no education we dont need no thought control no we dont"
strlist = s.split()
mydict = dict()
i:str
temp=[]
for i in strlist:
    mydict.update({i:temp})
for j in mydict.keys():
    mydict[j]=[k for k in range(len(strlist)) if strlist[k]==j]
print(mydict)




