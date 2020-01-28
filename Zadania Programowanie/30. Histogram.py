#30. Wynegeruj listę 1000 liczb losowych o rozkładzie normalnym. Wykreśl histogram oraz średnią, medianę, dominantę, odchylenie standardowe, wariancję, skośność i kurtozę 

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import kurtosis
from collections import Counter 

def skosnosc(lista):
    avg=np.mean(lista)
    return 1/len(lista)*sum((lista-avg)**3)/(np.std(lista))**3

def dominanta (x):
    dom = Counter(x)
    return dom.most_common(1)[0][0]

liczby=np.random.normal(size=1000)

plt.hist(liczby)

print("Srednia: {}".format(np.mean(liczby)))
print("Mediana: {}".format(np.median(liczby)))
print("Dominanta: {}".format(dominanta(liczby)))
print("Odchylenie standardowe: {}".format(np.std(liczby)))
print("Wariancja: {}".format(np.var(liczby)))
print("Skosnosc: {}".format(skosnosc(liczby)))
print("Kurtoza: {}".format(kurtosis(liczby)))



