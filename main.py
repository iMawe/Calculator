from divison import div

print("Bienvenido")


opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Módulo de los dos números
    6) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        n1 = int(input("Introduce tu primer número: ") )
        n2 = int(input("Introduce tu segundo número: ") )
        #n3 =  add(n1,n2)
        #print("La respuesta es: ", n3)
        #print("Regresando al menu ")
    elif opcion == 2:
        n1 = int(input("Introduce tu primer número: ") )
        n2 = int(input("Introduce tu segundo número: ") )
        #n3 = sub(n1,n2)
        #print("La respuesta es: ", n3)
        #print("Regresando al menu ")
    elif opcion == 3:
        n1 = int(input("Introduce tu primer número: ") )
        n2 = int(input("Introduce tu segundo número: ") )
        #n3 = mul(n1,n2)
        #print("La respuesta es: ", n3)
        #print("Regresando al menu ")
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        n3 = div(n1,n2)
        print("La respuesta es: ", n3)
        print("Regresando al menu ")
    elif opcion == 5:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        #n3 = mod(n1,n2)
        #print("La respuesta es: ", n3)
        #print("Regresando al menu ")
    elif opcion == 6:
        break
    else:
        print("Opción incorrecta. Intente otra vez.")

    