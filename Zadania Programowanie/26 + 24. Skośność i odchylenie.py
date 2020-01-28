def odchylenie(x):
    l=0;
    for i in x:
        l += ((i - (sum(x)/len(x)))**2)
    return ((l/len(x))**0.5)

def skosnosc(x):
    l=0;
    for i in x:
        l += ((i - (sum(x)/len(x)))**3)
    return ((1/odchylenie(x))**3)*(l/len(x))
