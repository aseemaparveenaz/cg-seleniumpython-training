def muli(a,b,bound):
    try:
        if(a*b<=bound):
            return a*b
        else:
            raise ValueError
    except ValueError:
        print("multiplication of {} and {} with bound {} is not possible".format(a,b,bound))
    return 0

muli(5,10,20)