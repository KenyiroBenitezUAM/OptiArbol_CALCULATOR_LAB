import os
from graphviz import Digraph
from IPython.display import Image

def solicitar_matriz():
    print("\nIngrese los valores de la matriz 4x4 (rendimiento):")
    matriz = []
    for i in range(4):
        fila = []
        for j in range(4):
            while True:
                try:
                    valor = float(input(f"Valor para la posición [{i+1},{j+1}]: "))
                    fila.append(round(valor, 3))
                    break
                except ValueError:
                    print("Por favor ingrese un número válido.")
        matriz.append(fila)
    return matriz

def solicitar_vector():
    print("\nIngrese los valores del vector de probabilidades (4 elementos):")
    vector = []
    for i in range(4):
        while True:
            try:
                valor = float(input(f"Probabilidad {i+1}: "))
                if valor < 0 or valor > 1:
                    print("La probabilidad debe estar entre 0 y 1")
                    continue
                vector.append(round(valor, 3))
                break
            except ValueError:
                print("Por favor ingrese un número válido.")

    suma = sum(vector)
    if abs(suma - 1.0) > 0.0001:
        print(f"\nLas probabilidades suman {suma:.3f}. Normalizando...")
        vector = [round(v/suma, 3) for v in vector]
        print("Probabilidades normalizadas:", vector)

    return vector

def multiplicar_matriz_vector(matriz, vector):
    resultado = []
    for fila in matriz:
        suma = 0
        for m, v in zip(fila, vector):
            suma += m * v
        resultado.append(round(suma, 3))
    return resultado

def generar_arbol_decisiones(matriz, vector, valores_esperados, opcion_optima):
    dot = Digraph(comment='Árbol de Decisiones', format='png')
    dot.attr(rankdir='LR')
    dot.node('A', 'Decisión Inicial', shape='box', style='filled', fillcolor='lightblue')

    for i in range(4):
        opcion_id = f'O{i+1}'
        color = 'lightgreen' if i + 1 == opcion_optima else 'white'
        dot.node(opcion_id, f'Opción {i+1}\\nValor esperado: {valores_esperados[i]:.3f}',
                 shape='box', style='filled', fillcolor=color)
        dot.edge('A', opcion_id, label=f'p={vector[i]:.3f}')

        for j in range(4):
            escenario_id = f'E{i+1}{j+1}'
            dot.node(escenario_id, f'Escenario {j+1}\\nRendimiento: {matriz[i][j]:.3f}', shape='ellipse')
            dot.edge(opcion_id, escenario_id)

    if os.path.exists('arbol_decisiones.png'):
        os.remove('arbol_decisiones.png')
    dot.render('arbol_decisiones', view=False)
    return Image('arbol_decisiones.png')

def main():
    while True:
        print("\n" + "="*50)
        print("PROGRAMA DE MULTIPLICACIÓN DE MATRIZ POR VECTOR")
        print("="*50)

        matriz = solicitar_matriz()
        vector = solicitar_vector()
        resultado = multiplicar_matriz_vector(matriz, vector)
        opcion_optima = resultado.index(max(resultado)) + 1

        print("\n" + "="*50)
        print("RESULTADOS FINALES")
        print("="*50)
        print("\nMatriz ingresada:")
        for fila in matriz:
            print([round(v, 3) for v in fila])
        print("\nVector de probabilidades ingresado:")
        print([round(v, 3) for v in vector])
        print("\nResultado de la multiplicación (rendimiento esperado):")
        print([round(r, 3) for r in resultado])

        generar_arbol_decisiones(matriz, vector, resultado, opcion_optima)

        if input("\n¿Desea realizar otra operación? (S/N): ").upper() != 'S':
            print("\nPrograma terminado.")
            break

if __name__ == "__main__":
    main()
