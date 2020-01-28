#Zadanie 3. 
#Utwórz funkcję zależną od numeru wiersza i kolumny macierzy (i, j), która będzie obliczać liczbę "żywych" komórek sąsiadujących względem komórki (i, j). Funkcja powinna mieć zaimplementowane periodyczne warunki brzegowe.
import numpy as np # jako skrót od numpy 

def macierz (n):
    x = np.random.choice([255,0],n*n,p=[0.2,0.8]).reshape (n,n)
    return (x);

def zywe (i, j,macierz):
    def liczba_zywych(i,j):
        return 0 <= i < len(macierz) and 0 <= j < len(macierz) and macierz[i][j]
        
    sasiedzi = 0

    if liczba_zywych(i-1, j-1) != 0:
        sasiedzi += 1
    if liczba_zywych(i-1, j) != 0:
        sasiedzi += 1
    if liczba_zywych(i-1, j+1) != 0:
        sasiedzi += 1
    if liczba_zywych(i, j-1) != 0:
        sasiedzi += 1
    if liczba_zywych(i, j+1) != 0:
        sasiedzi += 1
    if liczba_zywych(i+1, j-1) != 0:
        sasiedzi += 1
    if liczba_zywych(i+1, j) != 0:
        sasiedzi += 1
    if liczba_zywych(i+1, j+1) != 0:
        sasiedzi += 1
    print (sasiedzi)