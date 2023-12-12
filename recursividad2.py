def factorial(numero): #Definimos una variable "Factorial" su dato "numero"
    if numero ==1:     #Preguntamos si numero es igual a 1 me devuelva 1
        return 1            
    else:               # si no vamos a multiplicar numero por las veces de numero en forma retroceso 54321
        return numero * factorial(numero-1)  # restandoile 1

print(factorial(5))  # Pintamos el numero y damos el "numero "en este caso seria el valor "Dado"