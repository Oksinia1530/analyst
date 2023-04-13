
# #Zadacha10: (monetki kotorie nado perevernut')

# n = int(input("vvod kolichestva monet n"))
# orel=0
# reshka=0
# for i in range(n):
#     x = int(input("input x"))      #moneta vvod 1&0 (orel&reshka)
#     if x==0:
#         reshka=reshka+1
#     if x==1:
#         orel=orel+1
# if orel>=reshka:
#     print("nado perevernut: ",reshka)
# elif orel<reshka:
#     print("nado perevernut: ",orel)


# #Zadacha 12: (naiti dva chisla esli izvestna ih summa i proizvedenie)
# #x+y=b
# #x*y=c
# b = int(input("input b"))
# c = int(input("input c"))
# x1=((b+(b*b-4*c)**0.5)/2)
# x2=((b-(b*b-4*c)**0.5)/2)
# print("x1=",x1)
# print("x2=",x2)


# #Zadacha 14: (vivod vseh tselih ctepeney "2" menishe "n")
# n = int(input("input n"))
# k=0
# i=0
# while k<n:
#     print(k, end= ", ")
#     k=2**i
#     i=i+1    
# else:
#     print("stop")