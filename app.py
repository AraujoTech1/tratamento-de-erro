import logging
from cadastro import validar_nome, salvar_dados
from exceptions import ErroValidacao, ErroArquivo

# Configuração do logger
logging.basicConfig(filename='logs/app_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def cadastrar_usuario(nome):
    try:
        validar_nome(nome)
        salvar_dados(nome)
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    except ErroValidacao as e:
        print(f"[VALIDAÇÃO] {e}")
        raise
    except ErroArquivo as e:
        print(f"[ARQUIVO] {e}")
    except Exception as e:
        print("[ERRO INESPERADO]", e)
        logging.error("Erro inesperado no cadastro", exc_info=True)

def main():
    nome = input("Digite o nome do usuário para cadastro: ")
    try:
        cadastrar_usuario(nome)
    except ErroValidacao:
        print("Por favor, insira um nome válido.")

if __name__ == "__main__":
    main()
