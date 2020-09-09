def esPalindromo(texto):
    igual = 0
    j = 0

    for i in reversed(range(0, len(texto))):
        if texto[i].lower() == texto[j].lower():
            igual += 1
        j += 1
    if len(texto) == igual:
        print("El texto es palíndromo")
        return True;
    else:
        print("El texto no es palindromo")
        return False;

def main():
    texto = input("Ingrese una palabra o frase: ")
    esPalindromo(texto)

if __name__ == '__main__':
    main()