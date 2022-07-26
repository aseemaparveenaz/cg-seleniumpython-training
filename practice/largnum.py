n=int(input("enter num:"))
li=[]
for i in range(n):
    m=int(input("enter num"))
    li.append(m)
li.sort(reverse=True)
largnumstr=""
for i in li:
    largnumstr+=str(i)
ans=int(largnumstr)
print(ans)