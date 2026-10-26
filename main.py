
# Curso: Fundamentos de Tecnología Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Jose Andre Mora Paredes

# BARCA SCOUT
# Sistema de reclutamiento del FC Barcelona



# Cantidad de jugadores evaluados
TOTAL_JUGADORES = 5


# Validar nombres y nacionalidades
def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        valido = True

        if texto == "":
            valido = False

        for letra in texto:
            if not ("a" <= letra.lower() <= "z" or
                    letra in " áéíóúüñÁÉÍÓÚÜÑ"):
                valido = False

        if valido:
            return texto
        else:
            print("ERROR: Solo puede ingresar letras y espacios.")
            print("Intente nuevamente.\n")


# Validar numeros enteros
def leer_entero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))

            if numero >= minimo and numero <= maximo:
                return numero
            else:
                print("ERROR: Numero fuera del rango permitido.")
                print("Debe estar entre", minimo, "y", maximo)

        except ValueError:
            print("ERROR: Debe ingresar un numero entero.")
            print("No se permiten letras ni decimales.")

        print("Intente nuevamente.\n")


# Seleccionar la posicion del jugador
def leer_posicion(numero):
    while True:
        print("\nJugador", numero, "- Seleccione la posicion:")
        print("1. Portero")
        print("2. Defensa")
        print("3. Mediocampista")
        print("4. Delantero")

        opcion = input("Ingrese una opcion (1-4): ").strip()

        if opcion == "1":
            return "Portero"

        elif opcion == "2":
            return "Defensa"

        elif opcion == "3":
            return "Mediocampista"

        elif opcion == "4":
            return "Delantero"

        else:
            print("ERROR: Seleccione una opcion del 1 al 4.")
            print("Intente nuevamente.\n")


# Evaluar requisitos del Barcelona
def evaluar_jugador(jugador):
    motivos = []

    if jugador["Edad"] < 18 or jugador["Edad"] > 30:
        motivos.append("Edad fuera del rango de 18 a 30.")

    if jugador["Partidos"] < 30:
        motivos.append("Necesita minimo 30 partidos jugados.")

    if jugador["Condicion fisica"] < 80:
        motivos.append("Condicion fisica inferior a 80.")

    if jugador["Habilidad tecnica"] < 85:
        motivos.append("Habilidad tecnica inferior a 85.")

    if jugador["Disciplina"] < 80:
        motivos.append("Disciplina inferior a 80.")

    if jugador["Posicion"] == "Delantero":
        if jugador["Goles"] < 15:
            motivos.append("Delantero con menos de 15 goles.")

    if jugador["Posicion"] == "Mediocampista":
        if jugador["Asistencias"] < 10:
            motivos.append("Mediocampista con menos de 10 asistencias.")

    return motivos


# Registrar los datos de cada jugador
def registrar_jugador(numero):
    print("\n" + "=" * 55)
    print("REGISTRO DEL JUGADOR", numero, "DE 5")
    print("=" * 55)

    jugador = {}

    jugador["Nombre"] = leer_texto(
        f"Jugador {numero} - Nombre completo: "
    )

    jugador["Edad"] = leer_entero(
        f"Jugador {numero} - Edad (18-35): ", 18, 35
    )

    jugador["Nacionalidad"] = leer_texto(
        f"Jugador {numero} - Nacionalidad: "
    )

    jugador["Posicion"] = leer_posicion(numero)

    jugador["Partidos"] = leer_entero(
        f"Jugador {numero} - Partidos jugados (0-1000): ",
        0, 1000
    )

    jugador["Goles"] = leer_entero(
        f"Jugador {numero} - Goles (0-1000): ",
        0, 1000
    )

    jugador["Asistencias"] = leer_entero(
        f"Jugador {numero} - Asistencias (0-1000): ",
        0, 1000
    )

    jugador["Condicion fisica"] = leer_entero(
        f"Jugador {numero} - Condicion fisica (0-100): ",
        0, 100
    )

    jugador["Habilidad tecnica"] = leer_entero(
        f"Jugador {numero} - Habilidad tecnica (0-100): ",
        0, 100
    )

    jugador["Disciplina"] = leer_entero(
        f"Jugador {numero} - Disciplina (0-100): ",
        0, 100
    )

    # Evaluar al jugador
    motivos = evaluar_jugador(jugador)

    jugador["Motivos"] = motivos

    if len(motivos) == 0:
        jugador["Resultado"] = "ACEPTADO"
    else:
        jugador["Resultado"] = "RECHAZADO"

    print("\nREGISTRO COMPLETADO")
    print("Jugador:", jugador["Nombre"])
    print("Resultado:", jugador["Resultado"])

    return jugador


# Mostrar todos los resultados
def mostrar_resumen(jugadores):
    print("\n" + "=" * 55)
    print("RESUMEN FINAL - RECLUTAMIENTO FC BARCELONA")
    print("=" * 55)

    aceptados = 0
    rechazados = 0

    for numero in range(TOTAL_JUGADORES):
        jugador = jugadores[numero]

        print("\n" + "-" * 55)
        print("JUGADOR", numero + 1, "-", jugador["Nombre"])
        print("-" * 55)

        print("Nombre:", jugador["Nombre"])
        print("Edad:", jugador["Edad"])
        print("Nacionalidad:", jugador["Nacionalidad"])
        print("Posicion:", jugador["Posicion"])
        print("Partidos jugados:", jugador["Partidos"])
        print("Goles:", jugador["Goles"])
        print("Asistencias:", jugador["Asistencias"])
        print("Condicion fisica:", jugador["Condicion fisica"])
        print("Habilidad tecnica:", jugador["Habilidad tecnica"])
        print("Disciplina:", jugador["Disciplina"])

        print("\nRESULTADO:", jugador["Resultado"])

        if jugador["Resultado"] == "ACEPTADO":
            aceptados = aceptados + 1
            print("Cumple todos los requisitos del FC Barcelona.")

        else:
            rechazados = rechazados + 1
            print("Motivos del rechazo:")

            for motivo in jugador["Motivos"]:
                print("-", motivo)

    print("\n" + "=" * 55)
    print("ESTADISTICAS FINALES")
    print("=" * 55)

    print("Total de jugadores:", len(jugadores))
    print("Jugadores aceptados:", aceptados)
    print("Jugadores rechazados:", rechazados)

    print("\nGracias por utilizar BARCA SCOUT.")


# Funcion principal
def main():
    print("=" * 55)
    print("BARCA SCOUT")
    print("SISTEMA DE RECLUTAMIENTO DEL FC BARCELONA")
    print("=" * 55)

    print("Bienvenido al sistema de reclutamiento.")
    print("Se evaluaran exactamente 5 jugadores.")
    print("Los requisitos utilizados son ficticios.")

    jugadores = []

    for numero in range(1, TOTAL_JUGADORES + 1):
        jugador = registrar_jugador(numero)
        jugadores.append(jugador)

    mostrar_resumen(jugadores)


# Iniciar el programa
if __name__ == "__main__":
    main()



        

