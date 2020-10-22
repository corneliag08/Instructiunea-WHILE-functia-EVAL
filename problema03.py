nr=0
suma_p=0
while ((nr%3!=0)or(nr%2==0)):
    nr=eval(input("Introdu numarul : "))
    if nr%2==0:
        suma_p+=nr
print("Suma numerelor pare este  ",suma_p)