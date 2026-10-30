registro_trabajador = []
seguro = 2
while (seguro == 2):
    print("1) Registrar paciente.")
    print("2) Registrar lista edad de los trabajadores.")
    print("3) Salir.")
    opcion =int(input("Ingrese una de las opciones del menu: "))

    while (opcion <1 or opcion >3):
        print("Ingrese una opcion valida.")
        opcion =int(input("Ingrese una de las opciones del menu: "))
    
    match opcion:
        case 1:
            print("---")
        case 2:
            for edad in range(5):
                edad_t = int(input(f"Ingrese la edad del trabajador {edad + 1} del hospital: "))
                if edad_t >= 15:
                    edad_registro = {edad_t}
                    registro_trabajador.append(edad_registro)
                    print(f"La edad del trabajador _____ fue registrada con exito.")
                else:
                    print("Edad invalida, ingrese una edad mayor o igual a 15.")
        case 3:
            seguro = int(input("Esta seguro(a) de querer salir? SI(1) / NO(2)."))
            if seguro == 1:
                print("Hasta pronto!!!")
                break
            else:
                continue
        case _:
            print("Error, intentelo denuevo.")