nomes = ('kaique', 'gabriel', 'roberto',
         'julia', 'edimilson',
         'maria', 'jessica', 'francisca',
         'daniela', 'heitor', 'fernanda',
         'douglas', 'emilly','pedro',
         'thiago', 'eduardo', 'antonio')

    #tupla com nomes específicos
    
for palavra in nomes:                                               #para cada palavra em nome
    print(f"\nA palavra {palavra}, contém as vogais ", end='')      #cita cada nome da tupla
    for letra in palavra:                                           #para cada letra em cada palavra (dentro da tupla nomes)
        if letra in 'aeiou':                                        #se a letra dentro das palavras contar uma vogal
            vogais = letra                                          #variável vogais = vogal
            print(f"{vogais}", end=' ')                             #imprima as vogais que aquela palavra contém

#funciona com qualquer tupla, uso do for aninhado e if
