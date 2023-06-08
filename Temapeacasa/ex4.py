elev1 = []
elev2 = []
nume_elev1=str(input("Introdu numele elev1: "))
prenume_elev1=str(input("Introdu prenumele elev1: "))
nota_elev1=float(input("Introdu nota elev1: "))
elev1.extend([nume_elev1, prenume_elev1, nota_elev1])

nume_elev2 = input("Numele elevului 2: ")
prenume_elev2 = input("Prenumele elevului 2: ")
nota_elev2 = float(input("Nota elevului 2: "))
elev2.extend([nume_elev2, prenume_elev2, nota_elev2])
nume_elev1 = nume_elev1.upper()
prenume_elev1 = prenume_elev1.capitalize()
nume_elev2 = nume_elev2.upper()
prenume_elev2 = prenume_elev2.capitalize()

if nota_elev1 > nota_elev2:
    print(f"Elevul cu nota cea mai mare: {nume_elev1} {prenume_elev1}")
elif nota_elev1 < nota_elev2:
    print(f"Elevul cu nota cea mai mare: {nume_elev2} {prenume_elev2}")

if nota_elev1 < nota_elev2:
    print(f"Elevul cu nota cea mai mică: {nume_elev1} {prenume_elev1}")
elif nota_elev1 > nota_elev2:
    print(f"Elevul cu nota cea mai mică: {nume_elev2} {prenume_elev2}")





