def convert_temperature(temperature=None,unit=None):
    if temperature==F:
        return(unit-32.0)*(5.0/9.0)
    elif temperature==C:
        return"F",(unit*(9.0/5.0))+32.0
    else:
        print("Need to be (F)or (C)!")

temperature=input("Select (F) or (C): ")
unit=int(input("What is temperature now: "))
s,m=convert_temperature(temperature,unit)
print({unit}, "degrees", {temperature}, "is", {m}, "degrees", {s})

#ceva nu merge.....
