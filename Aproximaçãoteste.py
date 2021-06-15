baixo = int(input("Limite inferior da sequência de números desejada para a aproximação: "))   #Sugestão:1
alto = int(input("Limite superior da sequência de números desejada para a aproximação: "))    #Sugestão:1024 (2^10 = 1024)
                                                                                              #Máximo 10 tentativas serão necessárias.
print("Pense em um número entre {} e {}".format(baixo, alto))
input("Aperte qualquer tecla desejada para que a aproximação começe!")

tentativa = 1 #Tentativas serem contabilizadas corretamente

while True:  #loop infinito
    print("As tentativas estão sendo calculadas com limite inferior= {} e superior {}". format(baixo, alto))
    print()
    suposicao = baixo + (alto - baixo) // 2   #Primeira tentativa é o ponto médio da sequência
    print("Minha suposição é = {}, acertei...?Se não, seu número é maior, menor ou igual? ".format(suposicao))
    maioroumenor = (input("Por favor digite + - OU = "))

    if maioroumenor == "+":
        baixo = suposicao + 1  #Limite inferior se torna maior que a tentativa
    elif maioroumenor == "-":
        alto = suposicao - 1   #Limite superior se torna menor que a tentativa
    elif maioroumenor == "=":
        print("Que legal, eu acertei na {} tentativa! ".format(tentativa))
        break
    else:
        print("Por favor digite + - OU =")

    tentativa += 1