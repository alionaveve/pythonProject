masa_corp=float(input("Introdu masa corporala: "))
inaltimea=float(input("Introdu inaltimea: "))
bmi=masa_corp/(inaltimea**2)
print("BMI tau e: ", bmi)
if bmi<18.5:
    print("Subponderal" )
elif bmi>=18.5 and bmi<24.9:
    print("Greutate normală")
elif bmi>25 and bmi<30:
    print("Supraponderal")
elif bmi>=30:
    print("Sunteti obez!")