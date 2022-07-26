def fun1(a):
    c = 0
    b = str(a)

    if (len(b) == 3):
        l = list(b)
        if (abs(int(l[0]) - int(l[1])) == 1):
            c = c + 1
        elif (abs(int(l[1]) - int(l[2])) == 1):
            c = c + 1
        elif (abs(int(l[2]) - int(l[0])) == 1):
            c = c + 1
    if (c == 1):
        return "True"
    else:
        return "False"


