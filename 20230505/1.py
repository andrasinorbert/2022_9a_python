# x=5
# 
# print(type(x))
# y='j'
# print(type(y))
# 
# szam=7
# 
# i=0
# while szam>i:
#     print(i)
#     i+=1
#     
# for i in range(szam):
#     print(i)
#     
#     
#szam=8
#nemtalaltael=True
#while nemtalaltael:
#    inp=int(input("Adj meg egy számot:"))
#    if szam>inp:
#        print("Amit megadtál az kisebb, mint amire gondoltam!")
#    elif szam<inp:
#        print("Amit megadtál az nagyobb, mint amire gondoltam!")
#    else:
#        print("Eltaláltad! Gratulálok!")
#        nemtalaltael=False
#
#szam=8
#while True:
#    inp=int(input("Adj meg egy számot:"))
#    if szam>inp:
#        print("Amit megadtál az kisebb, mint amire gondoltam!")
#    elif szam<inp:
#        print("Amit megadtál az nagyobb, mint amire gondoltam!")
#    else:
#        print("Eltaláltad! Gratulálok!")
#        break
    
#    
#while True:
#    print(1)
#    print(2)
#    x=input("Adj meg egy szöveget!")
#    if int(x)==5:
#        continue
#    print("hahaha nem talált!")
#

lista=[1,2,3,4,5,6]
print(lista)
print(lista[2:5])# 2-es indextől 5-ös indexig
print(lista[-1]) # utolso
print(lista[-2]) # utolso előtti
print(lista[::2]) # lépésköz, a 0. indextől minden 2. számot ir ki
print(lista[2:5:2]) #kezdő index, végső index, lépésszám
print(lista[:])

def kiir(a):
    print(a)
    
def f(x):
    return x*x+3

y=f(5)
print(y)

def listaatir(a):
    a[3]=10
    return a

lista2=listaatir(lista[:])
print(lista2)
print(lista)