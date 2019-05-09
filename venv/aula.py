# def dobra_cada_um (lista):
#     def dobra_um(x):
#         return 2 * x
#     return [dobra_um(j) for j in lista]
#
# def aplica_a_todos(lista,funcao):
#     return [funcao(x) for x in lista]
#
# def quadrado(x):
#     return x ** 2
#
# def cubo(x):
#     return x ** 3
#
# lista = [1,2,3]
#
# print(aplica_a_todos(lista, quadrado))
# print(aplica_a_todos(lista,cubo))
#
#
#
#



fun = lambda x : 0 if x == 0 else x+fun(x-1)
fun(5)
