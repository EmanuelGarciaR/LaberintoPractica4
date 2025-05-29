# from logic.TheMazeOfTerror_logic import Laberinto, Movimientos

import random
import sys
sys.path.append("src")
from model.maze_terror import Laberinto, Movimientos, Arbol, Nodo

random.seed(42)

def obtener_datos():
    n = input("\n🧮 Ingrese el valor de n: ")
    if n.isdigit() and int(n) > 0:
        return int(n)
    else: 
        print("\n⚠️ Ingrese un valor válido\n")
        return obtener_datos()

def obtener_matriz_manual(n):
    print("\nIntroduce la matriz manualmente, fila por fila, separando los valores por espacio (usa ⬜, 🏁, 💥, 🐌, ❌):")
    matriz = []
    for i in range(n):
        fila = input(f"Fila {i+1}: ").split()
        matriz.append([[celda] for celda in fila])
    return matriz

def show_menu_principal():
    print("\n-------- MENÚ PRINCIPAL --------")
    print("\n1️⃣  Iniciar Laberinto")
    print("2️⃣  Visualizar estado actual del laberinto")
    print("3️⃣  Calcular la siguiente iteración")
    print("4️⃣  Ver detalles de la simulación")
    print("5️⃣  Agregar obstaculo aleatorio")
    print("6️⃣  Agregar bloqueo al laberinto")
    print("7️⃣  Agregar bloqueo al laberinto")
    print("8️⃣  Salir del juego\n")

def show_menu_secundario():
    print("\n-------- SEGUNDO MENÚ --------")
    print("\n🧠 Para más información de la simulación, elija una de las siguientes opciones:")
    print("\n1️⃣  Ver las posiciones recorridas por cada persona")
    print("2️⃣  Ver graficamente las posiciones recorridas por cada persona\n")
    print("3️⃣  Ver ruta más corta por persona")
    print("4️⃣  Ver las posibilidades de movimiento por persona")
    print("5️⃣  Mostrar estado actual del laberinto")
    print("6️⃣  Ver rutas que llegan a la salida por persona\n")
    print("7️⃣  Volver al menú principal 🔙")

def menu_principal():
    simulacion_iniciada = False 
    laberinto = None
    print("\n========================================")
    print("🎮 BIENVENIDO A THE MAZE OF TERROR 🧟‍♂️")
    print("========================================\n")

    while True:
        input("\n🔽 Presiona Enter para mostrar el menú... \n")
        show_menu_principal()
        opcion = input("\n🤔 Seleccione una opción: ")
        if opcion == "1":
            if simulacion_iniciada == True:
                print("\n🚫 La simulación ya fue iniciada. Salga de la simulación para iniciar una nueva.\n")
                return 
            n = obtener_datos()
            laberinto = Laberinto(n)
            laberinto.ubicar_salida()
            laberinto.generar_personas()
            laberinto.ubicar_persona()
    
            simulacion_iniciada = True
            print("\n🧩 Laberinto inicial 🧩\n")
            print(laberinto)
            print(f"\n🚪 La posición de las salidas es: {laberinto.salida_a} y {laberinto.salida_b}")
        elif opcion == "2":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            print("\n🧭 Estado actual del laberinto: \n")
            print(laberinto)
            print(f"\n🚪 La posición de la salida es: {laberinto.salida_a} y {laberinto.salida_b}")
        elif opcion == "3":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            elegir_ataques_random(laberinto)
            ejecutar_simulacion(laberinto)
            print("\n🔁 Estado del laberinto después de la simulación:\n")
            print(laberinto)
            print(f"\n🚪 La posición de la salidas es: {laberinto.salida_a} y {laberinto.salida_b}")
        elif opcion == "4":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            menu_secundario(laberinto)
        elif opcion == "5":
            print("Agregando trampa al laberinto...")
            opcion = elegir_ataques_random(laberinto)
            print(opcion)
            print(laberinto)
        elif opcion == "6":
            print("Agregando bloqueo al laberinto...")
            laberinto.ubicar_bloqueo
            print(laberinto)
        elif opcion == "7":
            print("Agregando retraso al laberinto...")
            laberinto.ubicar_retraso
            print(laberinto)
        elif opcion == "8":
            print("\n👋 Saliendo del juego... ¡Hasta la próxima!\n")
            break
        else:
            print("\n❌ Opción no válida, intente nuevamente.\n")
            continue

def menu_secundario(laberinto):
    while True:
        input("\n🔽 Presiona Enter para mostrar el segundo menú... \n")
        show_menu_secundario()
        opcion = input("\n🤔 Seleccione una opción: ")
        if opcion == "1":
            for persona in laberinto.personas:
                print(f"\n🧍 Ruta de {persona.nombre}:")
                persona.ruta_realizada.print()
        elif opcion == "2":
            for persona in laberinto.personas:
                if persona.llego_a_salida:
                    print(f"\n✅ {persona.nombre} ya ha llegado a la salida.")
                    arbol_ruta_realizada = persona.ruta_realizada
                    matriz_ruta_realizada = []
                    for i in range(laberinto.n):
                        fila = []
                        for j in range(laberinto.n):
                            fila.append("⬜")
                        matriz_ruta_realizada.append(fila)

                    def recorrer_arbol(nodo):
                        if nodo is None:
                            return
                        fila, columna = nodo.value
                        matriz_ruta_realizada[fila][columna] = "🔴"
                        for hijo in nodo.children:
                            recorrer_arbol(hijo)
                    if laberinto.salida_a:
                        recorrer_arbol(persona.ruta_realizada.root)
                        matriz_ruta_realizada[laberinto.salida_a[0]][laberinto.salida_a[1]] = "🟢"
                        matriz_ruta_realizada[persona.fila][persona.columna] = "🧍"

                    elif laberinto.salida_b:
                        recorrer_arbol(persona.ruta_realizada.root)
                        matriz_ruta_realizada[laberinto.salida_b[0]][laberinto.salida_b[1]] = "🟢"
                        matriz_ruta_realizada[persona.fila][persona.columna] = "🧍"

                    print(f"\n🗺️  Mapa de la ruta realizada por {persona.nombre}:")
                    for fila in matriz_ruta_realizada:
                        print("  ".join(fila))
                    continue

                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                ruta_corta = Movimientos.buscar_ruta_mas_corta(laberinto, arbol)
                print(f"\n🔍  Calculando ruta más corta para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                if ruta_corta is None:
                    print(f"\n❌ No hay ruta posible para {persona.nombre} desde su posición actual.")
                    continue
                print(f"\n🧭  Ruta más corta para {persona.nombre}")
                matriz_ruta_corta = []
                for i in range(laberinto.n):
                    fila = []
                    for j in range(laberinto.n):
                        fila.append("⬜")
                    matriz_ruta_corta.append(fila)
                for fila, columna in ruta_corta:
                    matriz_ruta_corta[fila][columna] = "🔴"
                if laberinto.salida_a:
                    matriz_ruta_corta[laberinto.salida_a[0]][laberinto.salida_a[1]] = "🟢"
                    matriz_ruta_corta[persona.fila][persona.columna] = "🧍"
                    print("\n🗺️  Mapa de la ruta más corta:")
                    print(f"\n🚪 La posición de la salida es: {laberinto.salida_a}")
                    for fila in matriz_ruta_corta:
                        fila_str = "   ".join(str(celda) for celda in fila)
                        print(fila_str)
                        print()
                elif laberinto.salida_b:
                    matriz_ruta_corta[laberinto.salida_b[0]][laberinto.salida_b[1]] = "🟢"
                    matriz_ruta_corta[persona.fila][persona.columna] = "🧍"
                    print("\n🗺️  Mapa de la ruta más corta:")
                    print(f"\n🚪 La posición de la salida es: {laberinto.salida_b}")
                    for fila in matriz_ruta_corta:
                        fila_str = "   ".join(str(celda) for celda in fila)
                        print(fila_str)
                        print()

        elif opcion == "3":
            for persona in laberinto.personas:
                if persona.llego_a_salida:
                    print(f"\n✅ {persona.nombre} ya ha llegado a la salida.")
                    continue
                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_ruta_corta = Movimientos.generar_arbol_rutas_mas_corta(laberinto, arbol)
                print(f"\n🔍  Calculando ruta más corta para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🧭  Ruta más corta para {persona.nombre}")
                arbol_ruta_corta.print(arbol_ruta_corta.root)
        elif opcion == "4":
            for persona in laberinto.personas:
                if persona.llego_a_salida:
                    print(f"\n✅ {persona.nombre} ya ha llegado a la salida.")
                    continue
                arbol = Arbol()
                arbol_rutas_posibles = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                print(f"\n🔍  Calculando las rutas que puede tomar {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🔀  Posibilidades de movimiento para {persona.nombre}")
                arbol_rutas_posibles.print(arbol_rutas_posibles.root)
        elif opcion == "5":
            print("\n🧭 Estado actual del laberinto: \n")
            print(laberinto)
        elif opcion == "6":
            for persona in laberinto.personas:
                if persona.llego_a_salida:
                    print(f"\n✅ {persona.nombre} ya ha llegado a la salida.")
                    continue
                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_rutas_salida = Movimientos.generar_arbol_rutas_llegan_salida(laberinto, arbol)
                print(f"\n🔍  Calculando las rutas que llegan a la salida para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🛣️  Rutas que llegan a la salida para {persona.nombre}")
                arbol_rutas_salida.print(arbol_rutas_salida.root) 
        elif opcion == "7":
            break
        else:
            print("\n❌ Opción no válida.\n")

def ejecutar_simulacion(laberinto):
    hay_personas_en_laberinto = False
    for persona in laberinto.personas:
        if persona.llego_a_salida == False:
            hay_personas_en_laberinto = True
            persona.posicion_actual = (persona.fila, persona.columna)
            print(f"\n🧍 Simulando para {persona.nombre} en posición ({persona.fila}, {persona.columna})")
            arbol = Arbol()
            arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
            rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
            persona.simular_movimiento(laberinto, arbol)
    
    if hay_personas_en_laberinto == False:
        print("\n🚷 No hay personas en el laberinto. Fin de la simulación.\n")
        laberinto.limpiar_laberinto_TBR()
        return
    
def elegir_ataques_random(laberinto):
    ataques = [laberinto.ubicar_bloqueo]
    while ataques:
        accion = random.choice(ataques)
        resultado = accion()
        if resultado:
            break
        else:
            ataques.remove(accion)


    


def main():
    menu_principal()

if __name__ == "__main__":
    main()