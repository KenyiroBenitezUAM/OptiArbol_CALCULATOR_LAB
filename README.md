# OptiArbol CALCULATOR-LAB

**OptiArbol CALCULATOR-LAB** es una aplicación web interactiva diseñada para facilitar la toma de decisiones mediante el cálculo de valores esperados y la visualización de árboles de decisión. Desarrollada como proyecto final para la asignatura *Análisis de Decisiones Avanzado* en la Universidad Autónoma Metropolitana (UAM) Xochimilco, esta herramienta permite a los usuarios ingresar una matriz de rendimientos 4×4 y un vector de probabilidades, calcular los valores esperados y generar un árbol de decisiones visual que resalta la opción óptima.

## Características

- **Cálculo de Valores Esperados**: Calcula los valores esperados para cuatro opciones basadas en una matriz de rendimientos 4×4 y un vector de probabilidades normalizado automáticamente.
- **Visualización de Árbol de Decisión**: Genera un árbol de decisiones interactivo usando D3.js, destacando la opción con mayor valor esperado en verde.
- **Diseño Responsivo**: Construido con Tailwind CSS para una interfaz moderna, adaptable a dispositivos móviles y de escritorio.
- **Interfaz Intuitiva**: Incluye validación de entradas, normalización automática de probabilidades y una guía clara de uso.
- **Datos de Ejemplo**: Carga datos de muestra predefinidos para facilitar la demostración y el aprendizaje.
- **Estilo Inspirado en Apple**: Interfaz elegante con transiciones suaves, sombras y efectos de desenfoque para una experiencia visual premium.

## Uso

1. **Ingresar Datos**:
   - En el panel de "Datos de Entrada", completa la matriz de rendimientos 4×4 con los valores correspondientes a cada opción (filas) y escenario (columnas).
   - Ingresa las probabilidades de cada escenario en el vector de probabilidades. Si no suman 1, se normalizarán automáticamente.

2. **Calcular**:
   - Haz clic en el botón "Calcular Valores Esperados" para procesar los datos.

3. **Visualizar Resultados**:
   - Revisa los valores esperados de cada opción en el panel de resultados.
   - Observa la opción óptima (resaltada en verde) con su valor esperado.
   - Explora el árbol de decisiones visual en el panel derecho, que muestra nodos de decisión, opciones, probabilidades y rendimientos.

4. **Datos de Ejemplo**:
   - La aplicación carga automáticamente datos de muestra al iniciarse, los cuales puedes modificar según tus necesidades.

## Contexto Académico

**OptiArbol CALCULATOR-LAB** fue desarrollado como proyecto final para la asignatura *Análisis de Decisiones Avanzado* en la Universidad Autónoma Metropolitana, Unidad Xochimilco, División de Ciencias Sociales y Humanidades, en el área de Política y Gestión Social.

**Equipo**:
- Benítez Pérez Adán Kenyiro
- Mayte Martínez Mendoza
- Daniela Altamirano Medina
- Nayeli López Miranda

**Profesor**: Dr. David Guerrero Sánchez  
**Grupo**: S02G  
**Fecha**: 10 de junio de 2025  
**Ubicación**: Ciudad de México, México

## Metodología

1. **Multiplicación de Matriz por Vector**: La matriz 4×4 representa los rendimientos de cuatro opciones bajo cuatro escenarios. El vector de probabilidades se normaliza para sumar 1, y se calcula el valor esperado de cada opción.
2. **Normalización de Probabilidades**: Si las probabilidades ingresadas no suman 1, el sistema las ajusta automáticamente.
3. **Visualización**: El árbol incluye un nodo inicial, cuatro nodos de opciones con sus probabilidades y ramificaciones a los escenarios con sus rendimientos.
4. **Selección Óptima**: La opción con el mayor valor esperado se resalta automáticamente.

## Ventajas y Desventajas

### Ventajas
- Visualización clara y comprensible del proceso de decisión.
- Soporta datos numéricos y categóricos sin necesidad de preprocesamiento.
- Interfaz transparente y fácil de usar.

### Desventajas
- Riesgo de sobreajuste si no se aplican técnicas de optimización.
- Sensibilidad a variaciones en los datos de entrada.

### Optimizaciones
- Poda de ramas irrelevantes.
- Uso de conjuntos de árboles para mejorar la precisión.
- Selección cuidadosa de características para optimizar el rendimiento.

Agradecemos al Dr. David Guerrero Sánchez y a la Universidad Autónoma Metropolitana, Unidad Xochimilco, por el apoyo y la orientación en el desarrollo de este proyecto.
