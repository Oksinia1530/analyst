# # Zadacha22: naiti peresecenie mnojestv
# n=int(input("input n"))
# m=int(input("input m"))
# set_n=[]
# set_m=[]
# for i in range(n):
#     x=int(input("input nomber from n"))
#     set_n.append(x)
# print("set_n: ",set_n)
# for i in range(m):
#     x=int(input("input nomber from m"))
#     set_m.append(x)
# print("set_m: ",set_m)
# set_n=set(set_n)
# set_m=set(set_m)
# print(set_n, set_m)
# print(sorted(set_n.intersection(set_m)))

# Zadacha24: Karelskaya chernika
n=int(input("input n"))
from random import randint
set_n=[randint(1,20) for i in range(n)]
print(set_n)
sum_max=0
for i in range(n-2):
    if (set_n[i-2]+set_n[i-1]+set_n[i]) > sum_max:
        sum_max=(set_n[i-2]+set_n[i-1]+set_n[i])
print(sum_max)