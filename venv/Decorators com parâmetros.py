def hello(msg):
    def hello_decorator (funcao):
        def fala():
            print(msg)
            funcao()
        return fala
    return hello_decorator

@hello('Antes')
def teste_pt():
    print("Executando teste...")

@hello("Before")
def test_en():
    print("Running test")


teste_pt()
test_en()