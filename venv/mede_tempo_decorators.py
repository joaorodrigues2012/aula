import time

def calcula_tempo_de_execucao_decorator(funcao):
    def calc_tempo():
        print(f'Decorando a função fatorial {funcao.__name__}')
        t0 = time.time()
        funcao()
        t1 = time.time()
        return t1 - t0
    return calc_tempo

def minha_funcao_rapidiunha():
    for i in range (10):
        print(i)


def minha_funcao_demorada():
    for i in range(10):
        print(i)
        time.sleep(1)

minha_funcao_rapidiunha = calcula_tempo_de_execucao_decorator(minha_funcao_rapidiunha)
minha_funcao_demorada = calcula_tempo_de_execucao_decorator(minha_funcao_demorada)
minha_funcao_rapidiunha()
minha_funcao_demorada()
