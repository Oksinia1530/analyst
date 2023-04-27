# #Zadacha26: rekursia.vozvesti A v stepen B
a=int(input("input a"))
b=int(input("input b"))
def stepen(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    else:
        return stepen(a,b-1)*a
print(stepen(a,b))

# #Zadacha28: rekursia.sum(a, b)
# a=int(input("input a"))
# b=int(input("input b"))
# def sum(a, b):
#     if a<b:
#         a,b=b,a
#     if b==0:
#         return a
#     else:
#         return sum(a+1, b-1)
# print(sum(a, b))