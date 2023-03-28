# 1) add meg, hogy a lista hanyadik eleme az 5!

lista= [8,7,4,7,5,2,5]

i=0
while i != 5:
    i+=1

valasz="A lista "+str(i)+". eleme az 5"
print(valasz)

# Add meg a lista elemeinek összegét!

osszeg=0
i=0
while i< len(lista):
    osszeg+=lista[i]
    i+=1
print("Az elemek összege:", osszeg)

