
#silnia
def silnia (x):
    s=1
    for i in range (1,x+1):
        s=s*i
    return s

# wzór Newtorna 
def newton (n,k):
    wynik = silnia(n)/ (silnia(k)*silnia (n-k))
    return wynik

print( "Wprowadz rząd:")
rz = int (input())

def pascal(rz):
    lista =[]
    for i in range (rz+1):
        lista.append(int(newton(rz,i)))
    return lista

wynik = pascal(rz)
print (wynik)

input()


 