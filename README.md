# Análisis Matricial de Armaduras 2D

Este repositorio contiene una implementación en **Python** del **Método de la Rigidez** (Direct Stiffness Method) para el análisis de armaduras planas. El código está diseñado para ser modular y educativo, permitiendo visualizar paso a paso el cálculo matricial de estructuras reticulares.

## 📋 Características

El programa es capaz de resolver armaduras estáticamente determinadas e indeterminadas, calculando:

* **Matriz de Rigidez Global:** Ensamblaje automático a partir de las matrices locales.
* **Desplazamientos Nodales:** Resolución del sistema de ecuaciones $F = K \cdot u$.
* **Reacciones en los Apoyos:** Cálculo preciso de fuerzas en los vínculos.
* **Fuerzas Internas:** Identificación de elementos en tracción y compresión.
* **Deformaciones Unitarias ($\varepsilon$) y Esfuerzos ($\sigma$):** Análisis de integridad estructural basado en las propiedades del material.
* **Visualización:** Gráficos de la estructura deformada y códigos de colores para barras traccionadas/comprimidas.