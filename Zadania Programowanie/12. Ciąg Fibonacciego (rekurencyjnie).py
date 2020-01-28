#Ciąg Fibonacciego 

#rekurencyjnie 
def fib_rek (n):
    if n==0 :
        return 0
    if n==1:
        return 1
    if n>1:
        return fib_rek(n-1) + fib_rek(n-2)
    
print ("Wpisz nr wyszukiwanego wyrazu ciągu:")
n = float(input())
wynik = fib_rek(n)
print (wynik)

input()
        
    
    
