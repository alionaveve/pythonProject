numerele=list(range(int(input("Introdu numarul: "))))
numar_par=numerele[::2]
numar_impar=numerele[1::2]
print("Lista numerelor pare:", numar_par)
print("Lista numerelor impare:", numar_impar)

print("Suma numerelor pare:",sum(numar_par))
print('Suma numerelor impare:',sum(numar_impar))