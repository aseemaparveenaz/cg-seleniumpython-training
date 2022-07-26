#question 1
from itertools import permutations

input1=input("")
p=permutations(input1)
for i in list(p):
    print(i)