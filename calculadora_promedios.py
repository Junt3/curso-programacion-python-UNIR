
def ingresar_calificaciones():
    """
    Aqui solicita al usuario nombre de las materias y calificaciones, 
    tambien valida que los datos no esten vacios y que las notas esten en el rango,
    retorna dos listas: materias y calificaciones
    """
    materias = []
    calificaciones = []
    
    while True:
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            break
        
        # validacion de calificacion, que sea un numero valido
        while True:
            try:
                nota = float(input(f"Ingrese la calificacion para '{materia}' (0 - 10): "))
                if 0.0 <= nota <= 10.0:
                    break
                else:
                    print("Error: La calificacion debe estar en el rango de 0 a 10")
            except ValueError:
                print("Error: Ingrese un valor numerico valido")
        
        materias.append(materia)
        calificaciones.append(nota)
        
        # salida del bucle principal
        continuar = input("¿Quiere ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    return materias, calificaciones

# calculos basicos 

def calcular_promedio(calificaciones):
    """ calcula y retorna el promedio de la lista calificaciones """
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    """
    Aqui compara las califiaciones con el umbral y retorna dos listas
    con los indices de las materias aprobadas y reprobadas
    """
    indices_aprovados = []
    indices_reprovados = []
    
    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            indices_aprovados.append(i)
        else:
            indices_reprovados.append(i)
    
    return indices_aprovados, indices_reprovados

def encontrar_extremos(calificaciones):
    """ Busca y devuelve los indices de las calificaciones mas altas y bajas """
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    
    return indice_max, indice_min

def main():
    """
    Esta es la funcion principal, ejecuta el programa, obtiene los datos,
    realiza los calculos y muestra los reportes
    """
    print("== Calculadora de Promedios ==")
    
    # aqui obtenemos los datos llamando a la primera funcion
    materias, calificaciones = ingresar_calificaciones()
    
    # manejo de lista vacia
    if not materias:
        print("No se ingresaron datos... Finalizando...")
        return
    
    promedio = calcular_promedio(calificaciones)
    idx_aprobados, idx_reprovados = determinar_estado(calificaciones)
    idx_max, idx_min = encontrar_extremos(calificaciones)
    
    # muesta todos los datos
    print(f"\n-- Promedio General --")
    print(f"{promedio:.2f}")
    
    print("\n-- Estado de Materias (Umbral 5.0) --")
    print("Aprovadas:")
    if idx_aprobados:
        for i in idx_aprobados:
            print(f"- {materias[i]}: {calificaciones[i]}")
    
    print("\nReprobadas:")
    if idx_reprovados:
        for i in idx_reprovados:
            print(f"- {materias[i]}: {calificaciones[i]}")
    else:
        print("- Ninguna materia reprobada.")
        
    print("\n-- EXTREMOS --")
    print(f"Mejor calificación: {materias[idx_max]} con {calificaciones[idx_max]}")
    print(f"Peor calificación : {materias[idx_min]} con {calificaciones[idx_min]}")

    print("\n¡Gracias por usar la calculadora de promedios! Hasta pronto.")
if __name__ == "__main__":
    main()
