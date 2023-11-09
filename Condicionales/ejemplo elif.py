# aún no -> 0 a 2
# kinder -> 3 a 5
# primaria -> 6 a 11
# secundaria -> 12 a 14
# preparatoria -> 15 a 17
# profesional -> 18 a 21
# posgrado -> 22 en adelante
edad = int(input("Ingresa tu edad: "))
if edad >= 0 and edad <= 2:
    print("Aún no está en edad de estudiar.")
else:
    if edad >= 3 and edad <= 5:
        print("Kinder.")
    else:
        if edad >= 6 and edad <= 11:
            print("Primaria")
        else:
            if edad >= 12 and edad <= 14:
                print("Secundaria.")
            else:
                if edad >= 15 and edad <= 17:
                    print("Preparatoria.")
                else:
                    if edad >= 18 and edad <= 21:
                        print("Profesional.")
                    else:
                        if edad >= 22:
                            print("Posgrado.")

if edad <= 2:
    print("Aún no está en edad de estudiar.")
elif edad <= 5:
    print("Kinder.")
elif edad <= 11:
    print("Primaria")
elif edad <= 14:
    print("Secundaria.")
elif edad <= 17:
    print("Preparatoria.")
elif edad <= 21:
    print("Profesional.")
else:
    print("Posgrado.")
        