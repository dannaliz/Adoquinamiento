import random as r
#Colores ANSI
colores = [
    "\033[97m",  # Blanco
    "\033[91m",  # Rojo
    "\033[92m",  # Verde
    "\033[93m",  # Amarillo
    "\033[94m",  # Azul
    "\033[95m",  # Magenta
    "\033[96m",  # Cian
]

num_colores = len(colores)

#Imprime el tablero donde pondremos nuestros adoquines, si la casilla es x entonces no se colorea, de lo contrario se colorea
def imprimeTablero(tablero):
    for fila in tablero:
        for elem in fila:
            if elem == 'x': 
                print(f"{elem.rjust(3)}", end="")
            else:
                color = colores[elem % num_colores]
                print(f"{color}{str(elem).rjust(3)}\033[0m", end="") 
        print() 

# Crea la matriz de tamaño 2^n
def creaTablero(n):
    matriz = [[0]*(2**n) for _ in range(2**n)]
    return matriz

"""
Función recursiva que toma 6 argumentos, el tablero, x, y que es la casilla de donde empezaremos a buscar
y tomaremos como referencia, la marcax y marcay que es la casilla donde esta la marca a la que nos referiremos para 
saber como acomodar los adoquines y n, que es el tamaño de la sección donde trabajaremos
"""
contador=1
def Adoquinamiento(tablero, x,y,marcax, marcay, n):
    global contador
    if n == 1:
        return 

    mitad = n//2
    mitadx = x + mitad
    mitady = y+mitad
    
    tablero1x=mitadx-1
    tablero1y=mitady-1
    tablero2x=mitadx-1
    tablero2y=mitady
    tablero3x=mitadx
    tablero3y=mitady-1
    tablero4x=mitadx
    tablero4y=mitady
    #El eje x es el eje vertical, no? jafjjaj, 
    if marcax < mitadx and marcay < mitady: #Cuadrante superior izq -x-y
        tablero[mitadx-1][mitady] = contador
        tablero[mitadx][mitady-1] = contador
        tablero[mitadx][mitady] = contador
        tablero1x= marcax
        tablero1y= marcay
    elif marcax < mitadx and marcay >= mitady: #Cuadrante sup derecho -xy
        tablero[mitadx-1][mitady-1] = contador
        tablero[mitadx][mitady-1] = contador
        tablero[mitadx][mitady] = contador
        tablero2x= marcax
        tablero2y= marcay
    elif marcax >= mitadx and marcay < mitady: #Cuadrante inferior izq x-y
        tablero[mitadx-1][mitady-1] = contador
        tablero[mitadx-1][mitady] = contador
        tablero[mitadx][mitady] = contador
        tablero3x= marcax
        tablero3y= marcay
    elif marcax >= mitadx and marcay >= mitady: #Cuadrante inferior der xyx
        tablero[mitadx-1][mitady-1] = contador
        tablero[mitadx-1][mitady] = contador
        tablero[mitadx][mitady-1] = contador
        tablero4x= marcax
        tablero4y= marcay
    
    contador += 1 
    imprimeTablero(tablero)
    input()
    #recursivo
    Adoquinamiento(tablero,x,y,tablero1x, tablero1y,mitad)
    Adoquinamiento(tablero, x,y+mitad, tablero2x, tablero2y, mitad)
    Adoquinamiento(tablero, x + mitad, y, tablero3x,tablero3y, mitad)
    Adoquinamiento(tablero, x + mitad, y+mitad,tablero4x, tablero4y, mitad)

if __name__ == "__main__":
    try:

        n = int(input("Ingresa la potencia a la que será elevada 2 para crear el tablero: "))
        if n < 0:
            raise ValueError("El valor de n debe ser un entero positivo.")
        
        if n == 0:
            print(["x"])
        
        tablero = creaTablero(n)

        i, j = r.randrange(2**n), r.randrange(2**n)
        tablero[i][j] = "x"

        Adoquinamiento(tablero,0,0,i,j, 2**n)
    
    except ValueError as error:
        print(f"Error de valor: {error}")
    except Exception as e:
        print(f"Error: {e}")
    