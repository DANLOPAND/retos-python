# Decorador para obtener la el par mas cercano
def getPar():
    def decorator(func):
        def wrapper(*args, **kwargs):
            puntos_cercanos = None
            #cogemos la lista 
            cordenadas = args[0]
            for idx,punto1 in enumerate(cordenadas):
                #una lista nueva, que va a ser modificada, el copy es para que no modifique la lista cordenadas
                nueva_lista = cordenadas.copy()

                #se quita el punto 1 de la lista de cordenadas
                nueva_lista.pop(idx)
                for idx2,punto2 in enumerate(nueva_lista):
                    #operacion para obtener la distancia entre puntos
                    distancia = (abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1]))
                    if distancia < 2:
                        
                        puntos_cercanos = (punto1, punto2)
            print(puntos_cercanos)
            return puntos_cercanos
        return wrapper
    return decorator


@getPar()
def pares_cercanos(lista_de_cordenadas):
    return ""

lista_de_cordenadas = [(1,2),(2,4),(1,2)]
    

pares_cercanos(lista_de_cordenadas)
