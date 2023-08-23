def es_palindromo(palabra):
    palabra = palabra.lower()
    inversa = palabra[::-1]
    return palabra == inversa

def main():
    palabra = input("Ingrese una palabra: ")
    
    if es_palindromo(palabra):
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")

if __name__ == "__main__":
    main()