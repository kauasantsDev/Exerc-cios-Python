print("="*20)
print(">>> LOJA PCISTA <<<")
print("="*20)
continuar = barato = ""
tot = caro = menor = cont = 0            #declarando variáveis

while continuar != "N":                  #enquanto quiser continuar for igual(==) "S" (Sim):
    produto = input("Nome do produto: ")
    preco = float(input("Preço: R$"))
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    cont += 1                            
    tot += preco                         #total de toda compra, recebe(=) soma de qualquer valor informado dentro do while
    if preco > 1000:                     
        caro += 1
    if cont == 1:                        #enquanto for informado apenas 1 produto, ele é o menor (e maior),
        menor = preco                    #menor recebe(=) preco, porque é o único informado
        barato = produto                 #barato recebe(=) produto, porque é o único informado
    else:
        if preco < menor:                #se tiver mais de um produto informado, e o próximo do laço for menor, o próximo passa a ser o menor.
            menor = preco                #o preço desse produto passa recebe(=) menor
            barato = produto             #o nome do produto recebe(=) barato

print("------- FIM DO PROGRAMA -------")
print(f"O total da compra foi R${tot:.2f}")
print(f"Temos {caro} produto (s) custando mais que R$1000,00.")
print(f"O produto mais barato é o (a) {barato} que custa {menor:.2f}.")
