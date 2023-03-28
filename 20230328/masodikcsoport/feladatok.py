# 1)Szimuláljon egy pénzfeldobást,
# ahol azonos esélye van a fejnek és az írásnak is!

import random as rnd

feldobas=["F", "I"]
x=rnd.randint(0,1)
print(feldobas[x])

# 2) Kérjen be a felhasználótól egy tippet,
# majd szimuláljon egy pénzfeldobást! 
# Írassa ki a képernyőre a felhasználó tippjét
# és a dobás eredményét is, majd tájékoztassa
# a felhasználót az eredményről következő
# formában: 
# „Ön eltalálta.” vagy „Ön nem találta el.”!

import random as rnd

feldobas=["F", "I"]
#tipp=input("Tippelj: Fej vagy írás (F/I)!")
tipp="F"
x=rnd.randint(0,1)
dobottertek=feldobas[x]
print(f"felhasználó tippje: {tipp}")
print(f"dobott érték: {dobottertek}")
if tipp==dobottertek:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

#print("Ön eltalálta." if tipp==dobottertek else "Ön nem találta el.")

# 3) Állapítsa meg, hány dobásból állt
# a kísérlet (forrasok.txt), és a választ
# a mintának megfelelően írassa ki a képernyőre!

f=open("20230328/masodikcsoport/forras.txt", "r")
c=0
for i in f:
    c+=1
f.close()
print(f"{c} számú kisérlet törént")

# f=open("20230328/masodikcsoport/forras.txt", "r")
# tartalom=f.readlines()
# print(len(tartalom))

# 4) Milyen relatív gyakorisággal dobtunk a kísérlet
#    során fejet? (A fej relatív gyakorisága a fejet
#    eredményező dobások és az összes dobás hányadosa.)
#    A relatív gyakoriságot a mintának megfelelően két
#    tizedesjegy pontossággal, százalék formátumban
#    írassa ki a képernyőre!
f=open("20230328/masodikcsoport/forras.txt", "r")
fejekszama=0
osszes=0
for i in f:
    if i=="F\n":
        fejekszama+=1
    osszes+=1
f.close()
gyakorisag= round(fejekszama/osszes *100,2)
print(f"{gyakorisag}% az F gyakorisága")

# 5) Hányszor fordult elő ebben a kísérletben,
# hogy egymás után pontosan két fejet dobtunk?
# A választ a mintának megfelelően írassa ki
# a képernyőre! 
# (Feltételezheti, hogy a kísérlet legalább
# 3 dobásból állt.) 
# Például az IFFFFIIFFIFFFIFF sorozatban
# kétszer fordult elő, hogy egymás után pontosan 
# két fejet dobtunk.


