# def exibir(a, b, c):
#     print(a, b, c)
#
#
# # fixa o valor de a
# def exibir5(b, c):
#     exibir(5, b, c)
#
#
# # fixa o valor de c
# def exibir54(c):
#     exibir5(4, c)
#
#
# # chama
# exibir54(2)

# ------------------------------------------------------------------------------

# def equacao_terceiro_grau(a, b, c, d, x):
#     print( a * (x ** 3) + b * (x ** 2) + c * x + d)
#
#
# def equacao_terceiro_grau5(b, c, d, x):
#     return equacao_terceiro_grau(5, b, c, d, x)
#
#
# def equacao_terceiro_grau52(c, d, x):
#     return equacao_terceiro_grau5(2, c, d, x)
#
#
# def equacao_terceiro_grau524(d, x):
#     return equacao_terceiro_grau52(4, d, x)
#
#
# def equacao_terceiro_grau5241(x):
#     return equacao_terceiro_grau524(1, x)
#
#
# equacao_terceiro_grau5241(7)
# ------------------------------------------------------------------------------
# # fixa o primeiro valor, essa função está aplicando a técnica de currying
# def exibir(a):
#     def aux(b, c):
#         print(a, b, c)
#
#     return aux
#
#
# # ajusta o ponteiro
# exibir = exibir(1)
# # ajusta o ponteiro
# exibir(2, 3)

# ------------------------------------------------------------------------------
# def exibir(a):
#     def aux1(b):
#         def aux2(c):
#             print(a, b, c)
#
#     return aux2
#     return aux1
#
#
# exibir(1)(2)(3)

# ------------------------------------------------------------------------------


# def exibir(a):
#     def aux(b):
#         def aux2(c):
#             print(a,b,c)
#         return aux2
#     return aux
#
# f = exibir(2)
# g = f(3)
# g(4)
#
# exibir(2)(3)(4)

# ------------------------------------------------------------------------------
#from functools import partial
#
#
# def soma(a, b, c):
#     return a + b + c
#
#
# # sem vincular parâmetros
# print(soma(10, 100, 1000))
# # vinculando parâmetros
# soma_10 = partial(soma, 10)
# soma_10_100 = partial(soma_10, 100)
# print(soma_10_100(1000))

# ------------------------------------------------------------------------------
# from inspect import signature
#
#
# def curry(fnc):
#     def inner(arg):
#         if (len(signature(fnc).parameters) == 1):
#             return fnc(arg)
#
#         return curry(partial(fnc, arg))
#     return inner
#
#
# @curry
# def produto(a, b, c):
#     return a * b * c
#
#
# print(produto(10)(20)(30))

# ------------------------------------------------------------------------------

#--------------------------------Memoization------------------------------------

def fibo(n):
    if n == 1 or n == 2:
        return 1;
    return fibo(n-1) + fibo(n-2)


#print(fibo(50))

# -------------------

# cache = {}
# cache[1] = 1
# cache[2] = 1
#
# def fibo_memoized(n):
#     if n in cache:
#         return cache[n]
#     cache[n] = fibo_memoized(n-1) + fibo_memoized(n - 2)
#     return cache[n]
#
# print(fibo_memoized(50))
# ------------------------------------------------------------------------------




