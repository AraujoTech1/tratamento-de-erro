import json
import logging
from exceptions import ErroValidacao, ErroArquivo

def validar_nome(nome):
    if not isinstance(nome, str) or not nome.strip():
        raise ErroValidacao("O nome deve ser uma string não vazia.")

def salvar_dados(nome, arquivo='data/dados.json'):
    try:
        with open(arquivo, 'r+', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []

            dados.append({'nome': nome})
            f.seek(0)
            json.dump(dados, f, indent=4)
            f.truncate()
    except OSError as e:
        logging.error("Erro ao manipular o arquivo", exc_info=True)
        raise ErroArquivo("Não foi possível acessar o arquivo.") from e
