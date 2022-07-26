def sumofthedigthree(j):
    j = str(j)
    j1 = j[0]
    j2 = j[1]
    if (int(j1) % 3 == 0 and int(j2) % 3 == 0):
        return int(j)
    else:
        return -1

num1 = int(input())
num2 = int(input())
if (num2 > num1):
    l = []
    l2 = []
    for i in range(num1, num2 + 1):
        a = int(input())
        l.append(a)
    for j in range(len(l)):
        length = str(l[j])
        if (len(length) == 2):
            sum = sumofthedigthree(l[j])
            if (sum % 5 == 0):
                l2.append(sum)
else:
    print("Exit")
if (len(l2) == 0):
    print("-1")
else:
    print(max(l2))