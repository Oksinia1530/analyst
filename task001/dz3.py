# #Zadacha23(seminar): count element massiv, > antecedent element
# list_1=[0, -1, 5, 2, 3]
# count=0
# for i in range(len(list_1)-1):
#     if list_1[i]<list_1[i+1]:
#         count+=1
# print("count=",count)

# #Zadacha16(dz): Vichislit' skolko raz vstrechaetsa X v massiv(A)
# N=int(input("input N"))
# A=[]
# for i in range(N):
#     x=int(input("??????? ????? ??????"))
#     A.append(x)
# print("A: ",A)
# X=int(input("input X"))
# count=0
# for i in A:
#     if i==X:
#         count+=1
# print(count)

# #Zadacha18(dz): Naiti samiy blizkiy k X element iz massiva
# N=int(input("input N"))
# A=[]
# for i in range(N):
#     x=int(input("input number"))
#     A.append(x)
# print("A: ",A)
# X=int(input("input X"))
# A=sorted(A)
# print(A)
# for i in range(N-1):
#     if ((A[i]/X < 1) and (A[i+1]/X > 1) and (A[i]/X < A[i+1]/X))==True:
#         X1=A[i]
# print(X1)

# # Zadacha20(dz): Scrabble
# slovar={'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 
# 'D':2, 'G':2, 'B':3, 'C':3, 'M':3,'P':3, 'F':4, 'H':4, 'V':4, 'W':4,'Y':4,
# 'K':5, 'J':8, 'X':8,'Q':10, 'Z':10}
# slovo=(input("input slovo"))
# counter=0
# for char in slovo:
#     counter+=slovar[char]
# print(counter)