# if else egyszerűsítése

x=3
if x<5:
    print("kisebb")
else:
    print("nagyobb")

valasz="kisebb" if x<5 else "nagyobb"
print(valasz)
print("kisebb" if x<5 else "nagyobb")
#print("kisebb" if int(input("Adj meg egy számot!"))<5 else "nagyobb")

# file-ba írás ciklusból
f=open("20230328/output.txt", "a", encoding="utf-8")
for i in range(2,9):
    f.write(i)
f.close()
