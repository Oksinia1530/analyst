# Zadacha 34: Vinni-Puh

# stih = 'paro-ry-rem pam-pam-papam pa-ra-pa-dam'

# def ritm(stih):
#     print(stih)
#     stih = stih.split()
#     print(stih)
#     list_1=[]
    
#     for word in stih:
#         sum_glas = 0
#         for i in word:
#             if i in "aeioyu":
#                 sum_glas +=1
#         list_1.append(sum_glas)
#         print(list_1)
#     return len(list_1) == list_1.count(list_1[0])
    
# if ritm(stih):
#     print('param pam pam')
# else:
#     print ('pam param')
    
#Zadacha 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1,num_rows+1):
        for j in range(1,num_columns+1):
            print(*list(map(operation,[i],[j])), end="\t")
            print()
            
print_operation_table(lambda x,y: x*y)