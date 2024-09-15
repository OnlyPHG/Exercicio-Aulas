#Exercicio 1 (ABC)/////////////////////////////////////////////////////////////////////////

#Importamos a bliblioteca itertools. Ela possui uma função chamada 'permutations'que gera todas as permutações possiveis. Fonte:https://docs.python.org/3/library/itertools.html(Estudar para prova mais tarde)

from itertools import permutations #Importando a itertools e a função 'permutations'

def permutar(string): #Vamos usar Def para simplificar a função, coloca o string entre parenteses para o programa saber o valor que ta recebendo, ou vai dar erro.(Sério)
    Qpermutacoes=list(permutations(string)) #Assim vai gerar uma lista de permutações.
    for p in Qpermutacoes: #Laço com o 'p' recebendo as astribuições das permutações.
        print(p) #Mostrar o resultado
    return Qpermutacoes #Vai retornar a lista de permutacoes acima.
    
resultadoABC = "ABC" #As permutações vão ocorrer com 'ABC'
permutar(resultadoABC) #Variavel para receber o resultadoABC que é 'ABC'
print("\n"f"Total de permutações: {len(permutar(resultadoABC))}""\n") #O len vai retornar as letras para a nossa lista lá na linha 6, sem ele vai dar erro a contagem.


#Exercicio 2(BITS) ////////////////////////////////////////////////////////////////////////
from itertools import product #O mesmo esquema da importação do código acima

def combinar_binarios(n): #Nossa variavel para as combinações.
    
    for combinaçoes in product("01", repeat=n): #O repeat faz parte da biblioteca itertools, não vai funcionar sem importar a função 'product', ela que vai fazer funcionar essa bagaça de repeat dar certo.
        print(combinaçoes) #Mostrar as combinações

#E aqui vamos contar quantos bits.

n = 3  #Se colocar número muito alto vai dar B.O, usei o 3 do exemplo mesmo.
k = 2  # Número específico de bits  /por algum mótivo se colocar 1 buga com o código do ABC acima.(Isso que da fazer 2 códigos diferentes em um só.)

combinar_binarios(n) #Aqui atribuimos n a variavel combinar_binarios.

def contarbits(n, k): #k é o numeros de bits que queremos contar.
    def contar(bitsk=""):
        if len(bitsk) == n: #É novamente o len para contar.
            return bitsk.count('1') == k #Estamos chamando duas vezes a contagem, uma vez adicionando “1"
        return contar(bitsk + "0") + contar(bitsk + "1") #Estamos chamando duas vezes a contagem, uma vez adicionando “0"

    return contar() #Vai retornar o final

total_combinacoes = contarbits(n, k)
print("\n"f"Total de combinações com exatamente {k} bits 1 em números binários de tamanho {n}: {total_combinacoes}""\n")

