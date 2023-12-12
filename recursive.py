def sumared(numero):

    if numero == 1:
        return 1

    else:
        return numero + sumared(numero -1)

print(sumared(5))
