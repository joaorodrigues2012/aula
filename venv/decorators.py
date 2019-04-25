def meu_primeiro_decorator(func):
    def decorator():
        print("Antes de executar")
        func()
        print("Depois de executar")
    return decorator

def hello_decorators():
    print("Hello, decorators")

hello_decorators = meu_primeiro_decorator(hello_decorators)

hello_decorators()