def calcularPoblacion(A,B,año):
    while A != B:
        A = A+(A*0.02)
        B = B+(B*0.03)
        año += 1

    print("El año en que la población es superada es: ",año)
    return año

def main():
    A = 35000000
    B = 19900000
    año = 2019
    calcularPoblacion()

if __name__ == '__main__':
    main()



