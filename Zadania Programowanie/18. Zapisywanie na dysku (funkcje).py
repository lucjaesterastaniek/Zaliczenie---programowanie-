import matplotlib.pyplot as plt 
import csv

def f_liniowa (a,b):
    x=[]
    y=[]    
    for i in range (0,100):
         x.append (i-50)
         y.append (a * x[i] + b)
    return x,y


def f_kwadratowa (a,b,c):
     x=[]
     y=[]
     for i in range (0,100):
          x.append (i-50)
          y.append (a *x[i]*x[i] + b*x[i] + c)
     return x,y
    
def f_odwrotna (a,n):
     x=[]
     y=[]
     for i in range (100):
          x.append (i+1)
          y.append (a/x[i]**n)
     return  x,y

print ("Funkcja liniowa (1) Funkcja kwadratowa (2) Funkcja odwrotna (3):")
wybor = int(input())

if wybor ==1:
    print ("a:")
    a=int(input())
    print("b:")
    b=int(input())
    xy = f_liniowa (a,b)
    print ("X:{}".format(xy[0]))
    print ("Y:{}".format(xy[1]))
    print("Wywietl wykres (1) Nie wywietlaj (2):")
    decyzja = int(input())
    if decyzja==1:
        x,y = f_liniowa (a,b)
        plt.plot (x,y)
    if decyzja==2:
        print ("Koniec")
        
    with open('fliniowa.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(x)
        spamwriter.writerow(y)
        
if wybor ==2:
    print ("a:")
    a=int(input())
    print("b:")
    b=int(input())
    print("c:")
    c=int (input())
    xy = f_kwadratowa (a,b,c)
    print ("X:{}".format(xy[0]))
    print ("Y:{}".format(xy[1]))
    print("Wywietl wykres (1) Nie wywietlaj (2):")
    decyzja = int(input())
    if decyzja==1:
        x,y = f_kwadratowa (2,3,3)
        plt.plot (x,y)
    if decyzja==2:
        print("Koniec")
        
    with open('fkwadratowa.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(x)
        spamwriter.writerow(y)
        
if wybor ==3:
    print("a:")
    a=int(input())
    print("n:")
    n=int(input())
    xy = f_odwrotna(a,n)
    print ("X:{}".format(xy[0]))
    print ("Y:{}".format(xy[1]))
    print("Wywietl wykres (1) Nie wywietlaj (2):")
    decyzja = int(input())
    if decyzja==1:
        x,y = f_odwrotna (2,3)
        plt.plot (x,y)
    if decyzja==2:
        print("Koniec")
        
    with open('fodwrotna.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(x)
        spamwriter.writerow(y)

input()