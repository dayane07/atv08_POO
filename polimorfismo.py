import csv

class ExportadorDeDados:
    
    def __init__(self, caminho_arquivo: str):
        
        if not caminho_arquivo:
            raise ValueError("O caminho_arquivo não pode ser vazio.")
        self.caminho_arquivo = caminho_arquivo

    def exportar(self, dados: list):
       
        raise NotImplementedError("O método 'exportar' deve ser implementado pelas classes filhas.")

class ExportadorParaCSV(ExportadorDeDados):
    
    def exportar(self, dados: list):
        
        if not dados:
            print(f"Aviso: Lista de dados vazia. O arquivo '{self.caminho_arquivo}' não será criado ou será vazio.")
            return

        chaves = dados[0].keys()

        try:
            with open(self.caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=chaves)

                escritor.writeheader()

                escritor.writerows(dados)

            print(f" Dados exportados com sucesso para CSV em: {self.caminho_arquivo}")

        except IOError as e:
            print(f"Erro escrever o arquivo CSV: {e}")

class ExportadorParaTXT(ExportadorDeDados):
    
    def exportar(self, dados: list):
        
        if not dados:
            print(f"Aviso: Lista de dados vazia. O arquivo '{self.caminho_arquivo}' não será criado ou será vazio.")
            return

        try:
            with open(self.caminho_arquivo, mode='w', encoding='utf-8') as arquivo_txt:
            
                chaves = list(dados[0].keys())
                cabecalho = ' | '.join([str(k).upper() for k in chaves])
                separador = '-' * len(cabecalho)

                arquivo_txt.write(cabecalho + '\n')
                arquivo_txt.write(separador + '\n')

                for i, registro in enumerate(dados):
                    valores = [str(registro.get(chave, 'N/A')) for chave in chaves]
                    linha = f"{' | '.join(valores)}"
                    arquivo_txt.write(linha + '\n')

            print(f" Dados exportados com sucesso para TXT em: {self.caminho_arquivo}")

        except IOError as e:
            print(f" Erro ao escrever o arquivo TXT: {e}")

def gerar_relatorios(exportadores: list[ExportadorDeDados], dados: list):
    
    print("\n--- INICIANDO GERAÇÃO DE RELATÓRIOS ---")
    if not exportadores:
        print(" Nenhuma estratégia de exportação fornecida.")
        return

    for exportador in exportadores:
        
        exportador.exportar(dados)

    print("--- GERAÇÃO DE RELATÓRIOS CONCLUÍDA ---\n")

dados_usuarios = [
    {"id": 101, "nome": "Alice Souza", "email": "alice.s@empresa.com", "idade": 30},
    {"id": 102, "nome": "Bruno Costa", "email": "bruno.c@empresa.com", "idade": 24},
    {"id": 103, "nome": "Carla Lima", "email": "carla.l@empresa.com", "idade": 45},
]
exportador_csv = ExportadorParaCSV("usuarios_relatorio.csv")
exportador_txt = ExportadorParaTXT("usuarios_relatorio.txt")

lista_de_exportadores = [
    exportador_csv,
    exportador_txt,
]
gerar_relatorios(lista_de_exportadores, dados_usuarios)
