def torres(n, origen, destino, auxiliar):
    if n == 1:
        print(f"mover disco de {origen} a {destino}")
    else:
        torres(n-1, origen, auxiliar, destino)
        print(f"mover disco de {origen} a {destino}")
        torres(n-1, auxiliar, destino, origen)

def insercion():
    torres(3, "origen", "destino", "auxiliar")


# insercion()