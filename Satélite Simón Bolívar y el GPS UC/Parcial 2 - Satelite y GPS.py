def posicion_de_insercion(m1,m2):
    nf1 = len(m1)
    nc1 = len(m1[0])
    nf2 = len(m2)
    nc2 = len(m2[0])
    cont = 1
    v = [0]*(nf1 + nf2)
    for i in range(nf1):
        for j in range(nc1):
            if m1[i][j] != 0:
                cont += 1
        v[i] = cont
        cont = 1
        for i in range(nf2):
            for j in range(nc2):
                if m2[i][j] != 0:
                    cont += 1
            v[i+nf1] = cont
            cont = 1
    return v

def vector_nombre_arch_prueba(m):
    nf = len(m)
    v = [0]*(nf-1)
    for i in range(1,len(m)):
        v[i-1] = m[i][0]
    return v

def vector_nombre_arch_temporal(m):
    nf = len(m)
    v = [0]*(nf)
    for i in range(len(m)):
        v[i] = m[i][0]
    return v

def matriz_arch_prueba(m):
    nf = len(m) - 1
    nc = len(m[1]) - 1
    matriz = [[0]*nc for i in range(nf)]
    for i in range(nf):
        for j in range(nc):
            matriz[i][j] = int(m[i+1][j+1])
    return matriz

def matriz_arch_temporal(m):
    nf = len(m)
    nc = len(m[1]) - 1
    matriz = [[0]*nc for i in range(nf)]
    for i in range(nf):
        for j in range(nc):
            matriz[i][j] = int(m[i][j+1])
    return matriz

def insertar_fila_matriz(m,v,k):
    nv = len(v)
    if nv < len(m[0]):
        for i in range(len(m[0])-nv):
            v.append(0)
    for i in range(len(m[0])):
        m[k][i] = v[i]

def insertar_elemento_vector(v,k,valor):
    v[k] =  valor

archivo1 = open('PRUEBA.txt', 'r')
archivo2 = open('TEMPORAL.txt','r')
campos1 = archivo1.readlines()
campos2 = archivo2.readlines()
n = 0
n = len(campos1)
m = len(campos2)
lista1 = []
lista2 = []
for i in range(n):
    lista1.append(campos1[i].split(', '))

for i in range(m):
    lista2.append(campos2[i].split(', '))

cant_distancias_procesadas = lista1[0][0]

num_ciudades_con_distancia = lista1[0][0]
m1 = matriz_arch_prueba(lista1)
m2 = matriz_arch_temporal(lista2)
v1 = vector_nombre_arch_prueba(lista1)
v2 = vector_nombre_arch_temporal(lista2)
m_dist = m1 + m2
v_nombres = v1 + v2
v_posicion = posicion_de_insercion(m1,m2)

print(v_posicion)

cant_filas_matriz_arreglada = len(m_dist)
cant_columnas_matriz_arreglada = len(m_dist[0])
cant_elementos_vector_arreglado = len(v_nombres)

matriz_distancias_arregladas = [[0]*cant_columnas_matriz_arreglada for i in range(cant_filas_matriz_arreglada)]
vector_nombres_arreglado = [0]*cant_elementos_vector_arreglado

for i in range(cant_filas_matriz_arreglada):
    v_aux = m_dist[i]
    k = v_posicion[i]
    insertar_fila_matriz(matriz_distancias_arregladas,v_aux,k-1)
print(matriz_distancias_arregladas)

for i in range(cant_elementos_vector_arreglado):
    valor_aux = v_nombres[i]
    k2 = v_posicion[i]
    insertar_elemento_vector(vector_nombres_arreglado,k2-1,valor_aux)
print(vector_nombres_arreglado)

archivo3 = open('PRUEBA_CORREGIDA.txt','w')
archivo3.write(f'{cant_distancias_procesadas}')
for i in range(cant_filas_matriz_arreglada):
    archivo3.write('{0:8} '.format(vector_nombres_arreglado[i]))
    for j in range(cant_columnas_matriz_arreglada):
        archivo3.write('{0:5} '.format(str(matriz_distancias_arregladas[i][j])))
    archivo3.write('\n')