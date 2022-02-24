# CALCULADORA BASICA
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------

# FUNCAO CALCULADORA
def calculadora(args):
    operando = ""
    numeros = []
    for i in args:
        if type(i) == str:
            operando = i
        else:
            numeros.append(i)
    # ADIÇÃO
    if operando == "+":
        soma = numeros[0]
        for num in numeros[1:]:
            soma = soma + float(num)
        return (f'O resultado da adição é {soma:.2f}')
    # SUBTRACAO
    elif operando == "-":
        subtracao = numeros[0]
        for num in numeros[1:]:
            subtracao = subtracao - float(num)
        return (f'O resultado da subtração é {subtracao:.2f}')
    # DIVISAO
    elif operando == "/":
        divisao = numeros[0]
        for num in numeros[1:]:
            divisao = divisao / float(num)
        return (f'O resultado da divisao é {divisao:.2f}')
    # MULTIPLICAÇÃO
    elif operando == "*":
        multiplicacao = numeros[0]
        for num in numeros[1:]:
            multiplicacao = multiplicacao * float(num)
        return (f'O resultado da multiplicação é {multiplicacao:.2f}')
    else:
        return ("Operando não esta na lista...") 

# GLOBAIS MAIN                
if __name__=="__main__":
    colecao = []
    operador = input("Digite o operador (+ , - , *, /): ")
    colecao.append(operador)
    total_numeros = int(input(f"Digite quantos numeros na operaçõ de -> {operador} :"))
    inicio_total = 0
    while total_numeros != inicio_total:
        numeros = float(input(f"Digite o numero {inicio_total + 1}: "))
        colecao.append(numeros)
        inicio_total += 1
    colecao = tuple(colecao)
    print(calculadora(colecao))