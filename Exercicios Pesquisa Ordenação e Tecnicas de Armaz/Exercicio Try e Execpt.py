import numpy as np #Para instalar o numpy no pc vá no seu terminal do windows e digite pip install numpy.

#Criando arrays com Numpy
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
array3 = np.array([3, 5, 1, 5, 2])

#Operações matemáticas com arrays /Troque os simbolos para alterar a operação + - * /
soma = array1 + array2 + array3

print("Array1:", array1)
print("Array2:", array2)
print("Array3:", array3)
print("Soma", soma)

def divisao(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Não existe divisão por zero!") #O except captura o `ZeroDivisionError` e imprime uma mensagem de erro informando: “Erro: Não é possível dividir por zero”.
        #raise serve para abrir uma 'exceção', ou seja exceto se for 0 vai continuar caso contrario vai dar a mensagem acima.
        return (x + y) ** 2
    except ZeroDivisionError as e: #as é basicamente para dar um apelido a 'e' que por fim é o nosso denominador que será digitado. Abreviou basicamente.
        print(e)
        return None

r = np.double(input("Digite o numerador: "))
e = np.double(input("Digite o denominador: "))
resultado = divisao(r, e)
if resultado is not None: #Essa bagaça não funciona sem essa linha, NÃO MEXE, NÃO TOCA, NEM PENSA NESSA LINHA.
    print("O resultado é:", resultado)

#Duvidas vá na fonte: https://www.w3schools.com/python/python_try_except.asp