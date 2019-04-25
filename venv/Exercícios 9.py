# 1. A seguinte função calcula o valor de uma equação do segundo grau no ponto x,
# dados os coeficientes a, b e c.

def equacao_segundo_grau(x, a, b, c):
    return a * x * x + b * x + c


def equacao_segundo_grau5(x, b, c):
    return equacao_segundo_grau(x, 5, b, c)


def equacao_segundo_grau57(x, c):
    return equacao_segundo_grau5(x, 7, c)


def equacao_segundo_grau574(x):
    return equacao_segundo_grau57(x, 4)


print(equacao_segundo_grau574(2))

# -----------------------------------------------------------------------------

# 1.2 Refaça o Exercício 1.1 usando o operador partial.

from functools import partial


def equacao_segundo_grau_partial(a, b, c, x):
    return a * x * x + b * x + c


equacao_segundo_grau_partial_5 = partial(equacao_segundo_grau_partial, 5)

equacao_segundo_grau_partial_5_7 = partial(equacao_segundo_grau_partial_5, 7)

equacao_segundo_grau_partial_5_7_4 = partial(equacao_segundo_grau_partial_5_7, 4)

print(equacao_segundo_grau_partial_5_7_4(2))

# -----------------------------------------------------------------------------

# 1.3 Escreva uma função recursiva para calcular a seguinte relação de recorrência:
# f(n) =
# 1 se n >= 1 e n <= 5
# 2 * (n – 1) + 3 caso contrário


def funcao_recursiva(n):
    if n >= 1 and n <= 5:
        return 1;
    return funcao_recursiva()
