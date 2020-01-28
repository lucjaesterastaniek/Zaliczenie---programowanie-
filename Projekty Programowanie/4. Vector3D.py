import numpy as np

class Vector3D():
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def wyswietlanie(self): #1
        return(self.x,self.y, self.z)
        
    def suma(self,b): #2 - a.suma(b)/c jest tylko przykładem - można podać więcej wektorów
        self.x = self.x + b.x
        self.y = self.y + b.y
        self.z = self.z + b.z
        print(self.x)
        print(self.y)
        print(self.z)
    
    def roznica(self,b): #3 
        self.x = self.x - b.x
        self.y = self.y - b.y
        self.z = self.z - b.z
        print (self.x)
        print (self.y)
        print (self.z)
    
    def iloczyn(self,c): #4
        self.x = self.x *c
        self.y = self.y *c
        self.z = self.z *c
        print (self.x)
        print (self.y)
        print (self.z)
        
    def iloczynwektor(self,b): #5
        self.x = self.x *b.x
        self.y = self.y *b.y
        self.z = self.z *b.z
        print (self.x)
        print (self.y)
        print (self.z)
        
    
    def modul (self,): #7
        return ((self.x**2 + self.y**2 + self.z**2)**0.5)
    
    def przeciwne (self): #8
        return (-self.x, -self.y, -self.z)
        
#Utworzyć metody:
#1. Wyswietlanie współrzędnych 
#2. Zwiększ o inny wektor (suma)
#3. odejmowanie drugiego wektora (różnica)
#4. wymnoz przez liczbę (iloczyn przez liczbę)
#5. iloczyn przez drugi wektor skalarnie
#6. obroc o dany kąt
#7. obliczanie modulu
#8. wyznaczanie wektora przeciwnego