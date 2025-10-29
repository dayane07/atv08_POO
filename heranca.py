class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")

class Aluno(Pessoa):
    
    def __init__(self, nome, idade, matricula):
    
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
        
        print("\n--- Dados do Aluno ---")
        
        super().exibir_dados()
        print(f"Matrícula: {self.matricula}")
        print("----------------------")

class Professor(Pessoa):
   
    def __init__(self, nome, idade, disciplina):
        
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_dados(self):
        
        print("\n--- Dados do Professor ---")
    
        super().exibir_dados()
        print(f"Disciplina: {self.disciplina}")
        print("--------------------------")

aluno1 = Aluno("Maria Silva", 16, "2023001A")
professor1 = Professor("João Souza", 45, "Matemática")
pessoa_generica = Pessoa("Carlos Lima", 30)

pessoa_generica.exibir_dados()
aluno1.exibir_dados()
professor1.exibir_dados()