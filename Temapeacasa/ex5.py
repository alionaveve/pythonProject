nume=str(input('Introdu numele: '))
lista_numelor = nume.split(",")
list_of_marks = []
for names in lista_numelor:
    mark = int(input(f"Introduceți nota pentru {names}: "))
    list_of_marks.append(mark)
print("Lista de nume:", lista_numelor)
print("Lista de note:", list_of_marks)

marks_sum=0
for mark in list_of_marks:
    marks_sum+= mark

    print(f"Suma notelor: {marks_sum}")
    print(f"Media notelor: {marks_sum / 2}")