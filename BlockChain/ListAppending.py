#   First BlockChains

blockchain1  =    [[1]]
blockchain2  =    [[1]]

def _lastValue():
    return  blockchain1[-1]

def add_new_value(x):
    """Receives and appens a new value to the BlockChain"""
    blockchain1.append([_lastValue(),x])
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