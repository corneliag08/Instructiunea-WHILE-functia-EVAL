suma_nr=0
produs_nr=1
nr=1
n=eval(input("n= "))
while nr<=n:
    suma_nr+=nr
    produs_nr*=nr
    nr+=1
print("Suma numerelor este egala cu : ",suma_nr)
print("Produsul numerelor este egal cu : ",produs_nr)
print("Media aritmetica a numerelor este egala cu : ",suma_nr/n)