class Carro:

    def __init__(self, marca: str, modelo: str, ano: int):
        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já estava ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0 
            print("O carro está desligado.")
        else:
            print("O carro já estava desligado.")

    def acelerar(self, valor: float):
        
        if self.ligado:
            if valor > 0:
                self.velocidade += valor
                print(f"Acelerando... Nova velocidade: {self.velocidade:.1f} km/h")
            else:
                print("O valor para acelerar deve ser positivo.")
        else:
            print("ERRO: O carro precisa estar ligado para acelerar.")

    def frear(self, valor: float):
        
        if valor > 0:
            if self.velocidade - valor >= 0:
                self.velocidade -= valor
                print(f"Freando... Nova velocidade: {self.velocidade:.1f} km/h")
            else:
                 
                self.velocidade = 0
                print(f"Freando... O carro parou. Velocidade: {self.velocidade:.1f} km/h")
        else:
            print("O valor para frear deve ser positivo.")

    def exibir_informacoes(self):
        
        estado = "ligado" if self.ligado else "desligado"
        print("-" * 30)
        print("INFORMAÇÕES DO CARRO:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Status: {estado}")
        print(f"Velocidade Atual: {self.velocidade:.1f} km/h")
        print("-" * 30)
meu_carro = Carro("Ford", "Mustang", 1969)
meu_carro.exibir_informacoes()
meu_carro.acelerar(50)
meu_carro.ligar()
meu_carro.acelerar(30)
meu_carro.acelerar(45.5)
meu_carro.exibir_informacoes()
meu_carro.frear(20)
meu_carro.frear(100)
meu_carro.desligar()
meu_carro.exibir_informacoes()