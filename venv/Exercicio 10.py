# # def gera_primos():
# #     return i
# #
# # i = 0
# # while i < 10:
# #     print(gera_primos())
# #     i += 1
#
#
#
#
# t = 'a','b','c'
#
# for e in t:
#     print(e)
# #-------------------------------------------------------------------------------------
# i =iter(t)
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))
# #------------------------------------------------------------------------------------------
# i = iter(t)
# while True:
#     try:
#         e = next(i)
#     except StopIteration:
#         break
#     print(e)
#
# #--------------------------------------------------------------------------------------------------

# import random
#
# class RandomIterator:
#     def __init__(self, *elements):
#         self._elements = list(elements)
#     def __iter__(self):
#         random.shuffle(self._elements)
#         self._cursor = 0
#         return self
#     def __next__(self):
#         if self._cursor >= len(self._elements):
#             raise StopIteration()
#         e =self._elements[self._cursor]
#         self._cursor += 1
#         return e
#
# meu_objeto = RandomIterator(1,2,3)
#
# for elemento in meu_objeto:
#     print(elemento)



# def meu_gerador():
#     print("comecando...")
#     yield 1
#     print("continuando...")
#     yield 2
#     print("mais um pouco...")
#     yield 3
#     print("quase lá...")
#     yield 4
#     print("Acabou...")
#
# valor = meu_gerador()
# print(next(valor))
# print(next(valor))
# print(next(valor))
# print(next(valor))


# def inverte(uma_string):
#     lenght = len(uma_string)
#     for i in range(lenght -1,-1,-1):
#         print("Vai fazer yield")
#         yield uma_string[i]
#
# for c in inverte("USJT"):
#     print(c)


# class PotenciaDeDois:
#     def __init__(self,maximo = 0):
#         self.maximo = maximo
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n > self.maximo:
#             raise StopIteration()
#         resultado = 2 ** self.n
#         self.n += 1
#
# iterador = PotenciaDeDois(16)
# for i in iterador:
#     print(i)

    #----------------------------------------------------------------------


# def potencia_de_dois(max = 0):
#     n = 0
#     while n <= max:
#         yield 2 ** n
#         n += 1
#
# for c in potencia_de_dois(16):
#     print(c)
#

#---------------------------------------------------------------------

i = 0

def gera_primos():
    n = 2
    yield n
    i=3


    while n <= 10:
        if (n % 2 != 0):
            print( n)
            i+=1
        else:
            pass
        n += 1



for c in gera_primos():
    print(c)