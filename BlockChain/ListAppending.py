# -*- coding: utf-8 -*-
#   Used to solve : 
#       SyntaxError: Non-ASCII character '\xc3'

#   First BlockChains
#   Primeiras Blockchains

blockchain1  =    [[1]]
blockchain2  =    [[1]]

#   This Function receives the argument X , which is a Integer
#   A função recebe o argumento X , que é Integer

def add_new_value(x):
    blockchain1.append([blockchain1[-1],x])
    print(blockchain1)


add_new_value(1)
add_new_value(2)
add_new_value(3)

print('\n')

#   This Function receives no arguments, it means it will always add a static the value '111'
#   Essa função não recebe argumentos , por isso irá sempre adicionar a constante '111'


def add_new_value_1():
    blockchain2.append([blockchain2[-1],111])
    print(blockchain2)

add_new_value_1()
add_new_value_1()
add_new_value_1()

# It was tested to see if it was possible to Override a Function as easy as CSharp
# Foi testado para ver se era possivel Sobrecarregar uma Função tão fácilmente quanto no CSharp

#   OUTPUT

#   Blockchain1
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# [[1], [[1], 1]]
# [[1], [[1], 1], [[[1], 1], 2]]
# [[1], [[1], 1], [[[1], 1], 2], [[[[1], 1], 2], 3]]
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

#   Blockchain2
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# [[1], [[1], 111]]
# [[1], [[1], 111], [[[1], 111], 111]]
# [[1], [[1], 111], [[[1], 111], 111], [[[[1], 111], 111], 111]]
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#