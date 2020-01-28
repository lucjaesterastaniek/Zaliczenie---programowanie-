#Ciąg Fibonacciego 

#iteracyjnie
def fib_it (n):
    a=0
    b=1
    for i in range (0,n-1):
        a,b = b, a+b
    return b
 
    
   
    
print ("Wpisz nr wyszukiwanego wyrazu ciągu:")
n = int(input())
wynik = fib_it(n)
print (wynik)

input()
        