print ("Ten program znajduje miejsca zerowe trójmianu kwadratowego.")
print ("Jeśli twój trójmian zapisany jest w postaci: a * x^2 + bx + c = 0")
print ("Podaj a:")
a=int(input())

print ("Podaj b:")
b=int(input())

print ("Podaj c:")
c=int(input())

delta = (b**2) - 4*a*c

if (delta > 0):
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print ("X1: {0} X2: {1}". format(x1,x2))
elif (delta==0):
    x = (-b) / (2 * a)
    print ("X1: {0}".format(x))
else:
    print (" Brak miejsc zerowych. ")

input()