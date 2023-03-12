'''
The Amazing Race.
Equipos, de dos a cuatro miembros, corren alrededor del mundo en competencia
contra otros equipos. Durante la carrera se llevan indicadores de ruta que
se registran cada vez que un equipo logra culminar un reto, permitiendo así
estimar el avance de cada uno. El indicador puede tomar dos valores: 1 si el
reto fue logrado y 0 si el reto no ha sido alcanzado, si no se logra vencer
un reto, el resto de los siguientes se consideradan no alcanzados.

Dado un archivo de datos 'avances.txt' que almacena en cada linea la
identificación del grupo, y un conjunto de indicadores de avance durante la
carrera, desarrollar un programa que determine para cada grupo la cantidad de
retos culminados y además genere el archivo 'resultados.txt' que contenga los
tres equipos que van mas avanzados en la competencia.
'''
#sub-programas
def IniciarVector(columnas):
    vector = [0]*columnas
    return vector

def IniciarMatriz(fila,columna):
    matriz = [[0]*columna for i in range(fila)]
    return matriz

def MostrarMatriz(matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            if j == 0:
                print('{:<18}'.format(matriz[i][j]),end=' ')
            else:
                print(matriz[i][j], end=' ')
        print()

def InsertarVector(vector,valor):
    vector.extend([0])
    insertar = len(vector)
    vector[insertar-1] = valor
    
def VectorFila(matriz,fila,columna): #Sub-Programa 1
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j] == 1:
                vector = IniciarVector(vector,columnas=1)
                InsertarVector(vector,matriz[i][j])
    return vector

def PosicionMayor(vector): #Sub-Programa 2
    mayor_posicion,posicion = 0,0
    for i in range(len(vector)):
        if vector[i] > mayor_posicion:
            mayor_posicion = vector[i]
            posicion = i+1
    return posicion

def EliminarVector(vector,tamaño,k): #Sub-Programa 3
    vector.pop(k-1)
    return tamaño-1

def EliminarMatrizFila(matriz,fila,k): #Sub-Programa 4
    matriz.pop(k-1)
    return fila-1

def EquiposTop(matriz,fila,columnas,valor,posicion): #Sub-Programa 5
    matriz.extend([0])
    matriz[fila] = [0]*columnas
    for i in range(fila-1,posicion-2,-1):
        for j in range(columnas):
            matriz[i+1][j] = matriz[i][j]
    matriz[posicion-1] = valor
    return fila+1

def ModificarMatrizTop(matriz,columnas,valor1,valor2,valor3):
    for i in range(len(matriz)):
        for j in range(2,columnas):
            matriz[i].pop()
    matriz[0][1] = valor1
    matriz[1][1] = valor2
    matriz[2][1] = valor3
    columnas = 2
    return columnas

#inicializaciones
cont1,cont2 = 0,0
band1,linea = 0,0
mayor1,mayor2,mayor3 = 0,0,0

#programa raiz
#llenando datos de los participantes
with open('avances.txt') as file:
    campos = file.readlines()
    lista = campos[linea].split(', ')
    nTeam,mTeam = len(campos), len(lista)
    matriz_team = IniciarMatriz(nTeam,mTeam)
    for i in range(nTeam):
        lista = campos[linea].split(', ')
        linea+=1
        cont1 = 0
        for j in range(mTeam):
            if j == 0:
                matriz_team[i][j] = lista[cont1]
            else:
                matriz_team[i][j] = int(lista[cont1])
            cont1+=1
print('EQUIPOS')
MostrarMatriz(matriz_team,nTeam,mTeam)
print()

#llenando datos del top 3
nTop,mTop = 1, mTeam
matriz_top = IniciarMatriz(nTop,mTop)
for i in range(nTeam):
    for j in range(mTeam):
        if matriz_team[i][j] == 1:
            cont2+=1
    if band1 == 0:
        band1 = 1
        mayor1 = cont2
        lugar = 1
        nTop = EquiposTop(matriz_top,nTop,mTop,matriz_team[i],lugar)
    elif cont2 > mayor1:
        mayor2 = mayor1
        mayor1 = cont2
        lugar = 1
        nTop = EquiposTop(matriz_top,nTop,mTop,matriz_team[i],lugar)
    elif cont2 < mayor1 and cont2 > mayor2:
        mayor3 = mayor2
        mayor2 = cont2
        lugar = 2
        nTop = EquiposTop(matriz_top,nTop,mTop,matriz_team[i],lugar)
    elif cont2 < mayor1 and cont2 < mayor2 and cont2 > mayor3:
        mayor3 = cont2
        lugar = 3
        nTop = EquiposTop(matriz_top,nTop,mTop,matriz_team[i],lugar)
    cont2=0
    
print('MATRIZ RESULTANTE')
MostrarMatriz(matriz_top,nTop,mTop)
print()

#limpiando matriz top 3
while nTop > 3:
    delete = len(matriz_top)
    nTop = EliminarMatrizFila(matriz_top,nTop,delete)

print('MATRIZ RESULTANTE LIMPIA')
MostrarMatriz(matriz_top,nTop,mTop)
print()

#acomodando la matriz resultante:
mTop = ModificarMatrizTop(matriz_top,mTop,mayor1,mayor2,mayor3)
print('MATRIZ RESULTANTE MODIFICADA')
MostrarMatriz(matriz_top,nTop,mTop)

#imprimiendo en archivo 'resultados.txt'
with open('resultados.txt', 'w') as file2:
    file2.write('Los 3 equipos mas avanzados de la competencia son:\n')
    for i in range(nTop):
        for j in range(mTop):
            if j == 0:
                file2.write('{:<18}'.format(matriz_top[i][j]))
            elif j == 1 and i == nTop-1:
                file2.write(f'{matriz_top[i][j]} retos alcanzados')
            elif j == 1:
                file2.write(f'{matriz_top[i][j]} retos alcanzados\n')         