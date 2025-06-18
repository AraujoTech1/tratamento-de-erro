class ErroAplicacao(Exception):
    """Exceção base para a aplicação."""
    pass

class ErroValidacao(ErroAplicacao):
    """Erro relacionado à validação de entrada do usuário."""
    pass

class ErroArquivo(ErroAplicacao):
    """Erro relacionado à leitura ou escrita em arquivos."""
    pass
