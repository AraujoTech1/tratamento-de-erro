import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from cadastro import validar_nome
from exceptions import ErroValidacao

def test_validar_nome_vazio():
    with pytest.raises(ErroValidacao):
        validar_nome("")

def test_validar_nome_valido():
    try:
        validar_nome("Fernanda")
    except ErroValidacao:
        pytest.fail("ErroValidacao não esperado para nome válido")

