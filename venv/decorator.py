def hello_world_decorator (funcao):
    def aux():
        print ("Só decorando, não faço nada útil")
        funcao()
    return aux

@hello_world_decorator
def f ( ):
    print ("Uma função qualquer")
f ( )
