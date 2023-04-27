##Zadacha30: arifmprogress
# a1=int(input("input a1"))
# d=int(input("input d"))
# n=int(input("input n"))
# an=0
# set_an=[]
# for i in range(n):
#     an=(a1+((i+1)-1)*d)
#     set_an.append(an)
# print(set_an)

#Zadacha32: Indeks elementa
from random import randint
set_n=[randint(-20,20) for i in range(20)]
set_ind=[]
print(set_n)
a_min=int(input("input a_min"))
a_max=int(input("input a_max"))
for i in set_n:
    if a_min<=i<=a_max:
        set_ind.append(set_n.index(i))
print(set_ind)