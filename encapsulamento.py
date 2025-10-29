class ContaBancaria:

    def __init__(self, saldo_inicial: float):
       
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.__saldo = saldo_inicial
        print(f"Conta criada com sucesso. Saldo inicial: R$ {self.__saldo:.2f}")

    def depositar(self, valor: float):
        
        if valor <= 0:
            print(" Erro: O valor do depósito deve ser positivo.")
            return

        self.__saldo += valor
        print(f" Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.__saldo:.2f}")

    def sacar(self, valor: float):

        if valor <= 0:
            print(" Erro: O valor do saque deve ser positivo.")
            return
        
        if valor > self.__saldo:
            print(f" Erro: Saldo insuficiente. Saldo atual: R$ {self.__saldo:.2f}. Valor solicitado: R$ {valor:.2f}")
            return

        self.__saldo -= valor
        print(f" Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.__saldo:.2f}")

    def get_saldo(self) -> float:
        
        return self.__saldo

print("--- Criando uma conta ---")
minha_conta = ContaBancaria(saldo_inicial=500.00)
print("-" * 30)

minha_conta.depositar(150.50)

minha_conta.depositar(-10.00)
print("-" * 30)

minha_conta.sacar(200.00)

minha_conta.sacar(1000.00)
print("-" * 30)

saldo_atual = minha_conta.get_saldo()
print(f" O saldo final acessado via get_saldo() é: R$ {saldo_atual:.2f}")
print("-" * 30)

try:
    print(f"Tentativa de acesso direto (desencorajada): R$ {minha_conta.__saldo:.2f}")
except AttributeError as e:
    print(f" Erro ao acessar diretamente (como esperado): {e}")
