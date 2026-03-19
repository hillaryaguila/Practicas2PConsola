if __name__ == "__main__":
    from operacionesMatematicas import OperacionesMatematicas
    from holaMundo import Mensaje 
    from cuadrado import Cuadrado
    from rectangulo import Rectangulo
    

    print("Este es el menu principal")
    print("1. Operaciones matematicas")
    print("2. Hola Mundo")
    print("3. Edad de una persona")
    print("4. Figuras geometricas")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        operaciones = OperacionesMatematicas(0, 0)  # Inicializamos con valores por defecto
        print("Ingrese el primer número: ")
        numero1 = float(input())
        print("Ingrese el segundo número: ")
        numero2 = float(input())
        print(f"Suma: {operaciones.sumar(numero1, numero2)}")
        print(f"Resta: {operaciones.restar(numero1, numero2)}")
        print(f"Multiplicación: {operaciones.multiplicar(numero1, numero2)}")
        print(f"División: {operaciones.dividir(numero1, numero2)}")

    elif opcion == "2":
        mensaje = Mensaje("Hola, Mundo programacion con clases")
        mensaje.mostrar() 

    elif opcion == "3":   
        from persona import Persona
        print("Ingrese el nombre:  ")
        nombre = str(input())
        print("Ingrese el año de nacimiento: ")
        anio_nacimiento = int(input())
        print("Ingrese el año actual: ")
        anio_actual = int(input())
        edad = anio_actual - anio_nacimiento
        persona = Persona(nombre, edad, anio_nacimiento, anio_actual)
        print("La edad de la persona es: ", persona.edad)


    elif opcion == "4":   
        print("1. Cuadrado")
        print("2. Rectangulo")
        print("3. Triangulo Equilatero")
        figura_opcion = input("Seleccione una figura geométrica: ")

        if figura_opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)  # Inicializamos con valores por defecto
            print(f"Área del cuadrado: {cuadrado.area()}")
            print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")
            
        elif figura_opcion == "2":
            print("Ingrese la base del rectángulo: ")
            base = float(input())
            print("Ingrese la altura del rectángulo: ")
            altura = float(input())
            rectangulo = Rectangulo(base, altura)
            print(f"Área del rectángulo: {rectangulo.area()}")
            print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")

        elif figura_opcion == "3":
            print("Ingrese la base del triángulo equilátero: ")
            base = float(input())
            print("Ingrese la altura del triángulo equilátero: ")
            altura = float(input())
            triangulo = TrianguloEquilatero(base, altura)
            print(f"Área del triángulo equilátero: {triangulo.area()}")
            print(f"Perímetro del triángulo equilátero: {triangulo.perimetro()}")