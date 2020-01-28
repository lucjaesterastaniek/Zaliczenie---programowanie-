#Zadanie 2.
#Utwórz funckję, która na zadanej macierzy zapisze wzór ustalonych struktur (blok, ul, bochenek, łódka, światła uliczne, żaba, latarnia).
import numpy as np
import matplotlib.pyplot as plt

def macierz (n):
    x = np.random.choice([255,0],100,p=[0.2,0.8]).reshape (10,10)
    return (x);

mac=np.zeros(10*10).reshape(10,10)
plt.imshow(mac)
    
    
def addblok (i,j,grid):
    blok = np.array ([[0,255,255],[0,255,255],[0,0,0]])
    
    rx=blok.shape[0]
    ry=blok.shape [1]
    
    grid [i:i+rx, j:j+ry] = blok
    plt.imshow(grid)
    return grid
   
def addul (i,j,grid):
    ul = np.array ([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
    
    rx=ul.shape[0]
    ry=ul.shape [1]
    grid [i:i+rx, j:j+ry] = ul
    plt.imshow(grid)
    return grid

def addbochenek (i,j,grid):
    bochenek = np.array ([[0,255,255,0],[255,0,0,255],[0,255,0,255], [0,0,255,0]])
    
    rx=bochenek.shape[0]
    ry=bochenek.shape [1]
    
    grid [i:i+rx, j:j+ry] = bochenek
    plt.imshow(grid)
    return grid
    
def addlodka (i,j,grid):
    lodka= np.array ([[255,255,0],[255,0,255],[0,255,0]])
    
    rx=lodka.shape[0]
    ry=lodka.shape [1]
    
    grid [i:i+rx, j:j+ry] = lodka
    plt.imshow(grid)
    return grid

def addzaba (i,j,grid):
    zaba = np.array ([[0,255,255,255],[255,255,255,0]])
    
    rx=zaba.shape[0]
    ry=zaba.shape [1]
    
    grid [i:i+rx, j:j+ry] = zaba
    plt.imshow(grid)
    return grid


def addswiatla (i,j,grid):
    swiatla = np.array ([[0,255,0],[0,255,0],[0,255,0]])
    
    rx=swiatla.shape[0]
    ry=swiatla.shape [1]
    
    grid [i:i+rx, j:j+ry] = swiatla
    plt.imshow(grid)
    return grid

def addlatarnia (i,j,grid):
    latarnia = np.array ([[255,255,0,0],[255,0,0, 0],[0,0,0,255], [0,0,255,255]])
    
    rx=latarnia.shape[0]
    ry=latarnia.shape [1]
    
    grid [i:i+rx, j:j+ry] = latarnia
    plt.imshow(grid)
    return grid

# wywołujesz - np.funkcja(2,3,mac)