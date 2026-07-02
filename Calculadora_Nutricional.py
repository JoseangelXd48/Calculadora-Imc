"Hacer una Calculadora Para Calcular El IMC Y IGC De Una Persona"
"Con Funciones y un Menu Para Elegir Que Calcular"

historial = []
#Creamos una Funcion para Calcular El IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    #Regresa El Resultado 
    return imc
#Creamos una Funcion Para Calcular El IGC
def calcular_igc(imc, edad, sexo):
    if sexo == "masculino" or "MASCULINO":
        igc = (1.20 * imc) + (0.23 * edad) - 16.2
    else:
        igc = (1.20 * imc) + (0.23 * edad) - 5.4
    return igc
#Creamos una Funcion Para Clasificar el indice de masa corporal
def Clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
#Creamos La Funcion Para Ver el Menu y Las Opciones que tenemos disponibles 
def Menu():
    while True:
        print("Bienvenido a mi Calculadora Nutricional:")
        print("Opcion 1 = Calcular IMC:")
        print("Opcion 2 = Calcular IGC:")
        print("Opcion 3 = Ver Historia:")
        print("Opcion 4 = Salir:")
        opcion = int(input("Selecciona una Opcion: "))
        if opcion == 1:
            Peso = float(input("Por Favor Ingresa Tu Peso En Kilogramos: "))
            Altura = float(input("Por Favor Ingresa Tu Altura En Centimetros: "))
            imc = calcular_imc(Peso, Altura)
            Clasificacion = Clasificar_imc(imc)
            print(f"Tu IMC Es: {imc:.2f} y Tu Clasificacion Es: {Clasificacion}")
            historial.append(f"IMC: {imc:.2f}, Clasificacion: {Clasificacion}")
        elif opcion == 2:
            Edad = int(input("Por Favor Ingresa Tu Edad: "))
            Sexo = (input("Ingresa Tu Sexo Por Favor: "))
            igc = calcular_igc(imc, Edad, Sexo)
            print(f"Tu IGC Es: {igc:.2f}")
            historial.append(f"IGC: {igc:.2f}")
        elif opcion == 3:
            print("Historial De Calculos:")
            for item in historial:
                print(item)
        elif opcion == 4:
            print("Gracias Por Usar Mi Calculadora !Hasta Pronto¡")
            break
        else:
            print("Opcion No Valida, Por Favor Intenta De Nuevo.")
#Llamamos a la Funcion del Menu Para Empezar a Usar la Calculadora
Menu()
