# Análisis Matricial de Armaduras 2D

Este repositorio proporciona una implementación computacional avanzada en **Python** basada en el **Método Directo de la Rigidez** (Direct Stiffness Method) para el análisis estructural de armaduras planas. La arquitectura del código prioriza la modularidad y la rigurosidad analítica, facilitando la trazabilidad sistemática durante la evaluación del comportamiento matricial en sistemas reticulares complejos.

## Características

El algoritmo de cálculo está optimizado para procesar topologías estáticamente determinadas e hiperestáticas, ejecutando la evaluación de:

- **Matriz de Rigidez Global:** Ensamblaje numérico automatizado mediante la superposición de matrices de rigidez locales afectadas por sus respectivas matrices de transformación de coordenadas.
- **Desplazamientos Nodales:** Resolución algebraica del sistema de ecuaciones de equilibrio estático $F = K \cdot u$ mediante la partición matricial de los grados de libertad libres y restringidos.
- **Reacciones en los Apoyos:** Cuantificación rigurosa de las fuerzas reactivas impuestas en los vínculos de frontera.
- **Fuerzas Internas:** Determinación precisa del estado de carga axial por componente, discriminando el régimen de solicitación estructural (tracción o compresión).
- **Deformaciones Unitarias ($\varepsilon$) y Esfuerzos ($\sigma$):** Verificación analítica del desempeño estructural fundamentada en las ecuaciones constitutivas del material y las propiedades de la sección geométrica.
- **Visualización:** Representación gráfica que contrasta la topología original con la configuración deformada, integrando mapeos cromáticos escalares para una interpretación analítica del flujo de esfuerzos axiales.
