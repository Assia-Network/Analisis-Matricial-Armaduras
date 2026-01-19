import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math, Latex

def matriz_rigidez(A, E, xi, xf, yi, yf):
    delta_x = xf - xi
    delta_y = yf - yi
    longitud = np.sqrt(delta_x**2 + delta_y**2)
    sin = delta_y / longitud
    cos = delta_x / longitud
    
    k_local = (E*A/longitud)*np.array([[1, -1], [-1, 1]])

    Transf = np.array([[cos, sin, 0, 0], [0, 0, cos, sin]])

    k_global = Transf.T @ k_local @ Transf

    return k_local, k_global

def esambladora(coords, k_global, dict_GDL):
    dims = len(coords)*2
    matriz_global = np.zeros((dims, dims))
    Fuerzas_global = np.zeros((dims, 1))

    for k in k_global:
        indices = dict_GDL[k]
        rango = np.ix_(indices, indices)
        matriz_global[rango] += k_global[k]

    return matriz_global

def k_sistema_libre(k_sistema, GDL_res):

    # Reducciendo Filas
    k_red = np.delete(k_sistema, GDL_res, axis=0)

    # Reduciendo Columnas
    k_red = np.delete(k_red, GDL_res, axis=1)

    return k_red

def matriz_print_latex(pos, matriz, estadoz, name, int_dc, espec="k", notacion="f"):
    # Latex
    tex = "\\begin{bmatrix}"
    try:
        for fila in matriz:
            # Unimos los números con '&' y terminamos línea con '\\'
            tex += " & ".join([f"{x:.{int_dc}{notacion}}" for x in fila]) + " \\\\"
    except:
        tex += " & ".join([f"{x:.{int_dc}{notacion}}" for x in matriz]) + " \\\\"
    tex += "\\end{bmatrix}"

    # Mostramos
    display(Math(f"{pos}) \\quad {estadoz}({espec}_{{{name}}}) = {tex}"))
    
def formato_graficas():
    plt.rcParams.update({
    #Tipografía y tamaño de letra
    "font.size": 12,          #Tamaño general de la fuente
    "font.family": "serif",   #Fuente tipo "serif" (Times, etc.)
    
    #Ejes
    "axes.labelsize": 14,     #Tamaño de los labels de los ejes
    "axes.titlesize": 16,     #Tamaño del título del gráfico
    "axes.linewidth": 1.2,    #Grosor del borde de los ejes
    
    #Líneas
    "lines.linewidth": 2,     #Grosor de las líneas
    "lines.markersize": 6,    #Tamaño de los marcadores
    
    #Ticks
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "xtick.direction": "in",  #Hacer que las ticks vayan hacia dentro
    "ytick.direction": "in",
    "xtick.top": True,        #Mostrar ticks arriba
    "ytick.right": True,      #Mostrar ticks a la derecha
    
    #Leyenda
    "legend.fontsize": 12,
    "legend.frameon": False,  #Leyenda sin borde
    
    #Cuadrícula
    "grid.color": "gray",
    "grid.alpha": 0.3,
    "grid.linestyle": "--"
    })

def grafico_t0(coordenadas, barras, restricciones, Fuerzas, title, xlabel="x (u)", ylabel="y (u)", Nodos_v=True, Fuerzas_v=True, apoyos_v=True, ejes_locales_v=True, escala_ejes_l=15, tamaño_fig=(7, 7)):
    formato_graficas()
    plt.figure(figsize=tamaño_fig)
    for i, f, _, _ in barras:
        xi, yi = coordenadas[i]
        xf, yf = coordenadas[f]
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot([xi, xf], [yi, yf], '-')

        if ejes_locales_v:
            # Vector unitario
            L = np.sqrt((xf-xi)**2 + (yf-yi)**2)
            u_x = (xf-xi)/L
            u_y = (yf-yi)/L

            vx = -u_y
            vy = u_x

            x_m = (xi+xf)/2
            y_m = (yi+yf)/2

            # Eje local x
            plt.quiver(x_m, y_m, u_x, u_y, color='blue', scale=escala_ejes_l, width=0.005, headwidth=4, zorder=3)

            # Eje local y
            plt.quiver(x_m, y_m, vx, vy, color='red', scale=escala_ejes_l, width=0.005, headwidth=4, zorder=3)

    if Fuerzas_v:
        #Fuerzas
        # 1. Sacamos los datos del diccionario a listas (rápido)
        X = [coordenadas[k][0] for k in Fuerzas]
        Y = [coordenadas[k][1] for k in Fuerzas]
        U = np.array([Fuerzas[k][0] for k in Fuerzas]) # Fuerza X
        V = np.array([Fuerzas[k][1] for k in Fuerzas]) # Fuerza Y

        magnitudes = np.hypot(U, V)  
        fuerza_max = np.max(magnitudes) if len(magnitudes) > 0 else 1

        U_norm = U / fuerza_max
        V_norm = V / fuerza_max

        plt.quiver(X, Y, U_norm, V_norm, color='salmon', scale=8, width=0.005, headwidth=4, zorder=3, label='Fuerzas')

        plt.legend()

    if apoyos_v:
        for m in restricciones:
            if restricciones[m] == 0:
                plt.scatter(coordenadas[m][0], coordenadas[m][1], marker='>', color='b', s=50, zorder=3)
            elif restricciones[m] == 1:
                plt.scatter(coordenadas[m][0], coordenadas[m][1], marker='^', color='b', s=50, zorder=3)
            elif restricciones[m] == 2:
                plt.scatter(coordenadas[m][0], coordenadas[m][1], marker='s', color='b', s=50, zorder=3)

    if Nodos_v:
        for k in coordenadas:
            plt.text(coordenadas[k][0], coordenadas[k][1], k, fontsize=12, fontweight='bold', zorder=3)

    plt.axis('equal')
    plt.show()

def deformación_unitaria(xi, xf, yi, yf, desplazamiento):
    delta_x = xf - xi
    delta_y = yf - yi
    L = np.sqrt(delta_x**2 + delta_y**2)
    cos = delta_x / L
    sen = delta_y / L
    return (1/L)*np.array([-cos, -sen, cos, sen]) @ desplazamiento.T
        
def grafico_desf(coordenadas, barras, restricciones, dict_despl, escalada_def, dict_normal, title, xlabel="x (u)", ylabel="y (u)", Nodos_v=True, apoyos_v=True, est_or=True, tamaño_fig=(7, 7)):
    formato_graficas()
    plt.figure(figsize=tamaño_fig)
    for i, f, _, _ in barras:
        # Original
        xi, yi = coordenadas[i]
        xf, yf = coordenadas[f]
    
        # Desplazado
        xid, yid = dict_despl[i]*escalada_def + coordenadas[i]
        xfd, yfd = dict_despl[f]*escalada_def + coordenadas[f]
        
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if est_or:
            plt.plot([xi, xf], [yi, yf], '--', color='gray', alpha=0.5)
        if dict_normal[i+f] >0:
            plt.plot([xid, xfd], [yid, yfd], '-', color='blue', label='Tracción')
        elif dict_normal[i+f] <0:
            plt.plot([xid, xfd], [yid, yfd], '-', color='red', label='Compresión')
        else:
            plt.plot([xid, xfd], [yid, yfd], '-', color='green', label='Sin Carga')

    if apoyos_v:
        for m in restricciones:
            if restricciones[m] == 0:
                plt.scatter(coordenadas[m][0], coordenadas[m][1] + dict_despl[m][1]*escalada_def, marker='>', color='b', s=50, zorder=3)
            elif restricciones[m] == 1:
                plt.scatter(coordenadas[m][0]+ dict_despl[m][0]*escalada_def, coordenadas[m][1], marker='^', color='b', s=50, zorder=3)
            elif restricciones[m] == 2:
                plt.scatter(coordenadas[m][0], coordenadas[m][1], marker='s', color='b', s=50, zorder=3)

    if Nodos_v:
        for k in coordenadas:
            plt.text(coordenadas[k][0] + dict_despl[k][0]*escalada_def, coordenadas[k][1] + dict_despl[k][1]*escalada_def, k, fontsize=12, fontweight='bold', zorder=3)

    # Etiquetas de las barras
    handles, labels = plt.gca().get_legend_handles_labels()

    # Usar diccionario para eliminar duplicados
    by_label = dict(zip(labels, handles))

    # Mostrar solo una vez cada etiqueta
    plt.legend(by_label.values(), by_label.keys())
    

    plt.axis('equal')
    plt.show()    