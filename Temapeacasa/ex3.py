lista=[]
nume=str(input("Introdu numele: "))
prenume=str(input('Introdu prenumele: '))
varsta=str(input("Introdu varsta: "))
inaltimea=str(input('Introdu inaltimea: '))
ocupatia=str(input("Introdu ocupatia: "))
lista=lista[:len(lista)]+[nume]+[varsta]+[inaltimea ]+[ocupatia]
print(lista)