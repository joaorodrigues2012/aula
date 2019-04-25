import time

def calcula_tempo_decorator(funcao):
    def calcula_tempo():
        t0 = time.time()
        funcao()
        t1 = time.time()
        return t1-t0
    return calcula_tempo

@calcula_tempo_decorator
def demorada():
    for i in range (5):
        time.sleep(2)
        print(i)

print(demorada())