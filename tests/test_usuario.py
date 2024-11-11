import pytest

from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("joão", "peidão", "123")

def test_nome_invalido():
    with pytest.raises(TypeError, match="erro: o nome deve ser um texto"):
        Usuario(nome=13, email="peidão", senha="123")

def test_nome_vazio():
    with pytest.raises(TypeError, match="erro: o nome não pode estar vazio"):
        Usuario(nome="", email="peidão", senha= "123")

def test_email_invalido():
    with pytest.raises(TypeError, match="erro: o email deve ser um texto"):
        Usuario(nome="joão", email= 456, senha="123")

def test_email_vazio():
    with pytest.raises(TypeError, match="erro: o email não pode estar vazio"):
        Usuario(nome="joão", email= "", senha="123")

def test_senha_invalida():
    with pytest.raises(TypeError, match="erro: a senha deve ser um texto"):
        Usuario(nome="joão", email= "peidão", senha=123)

def test_senha_vazia():
    with pytest.raises(TypeError, match="erro: a senha não pode estar vazia"):
        Usuario(nome="joão", email= "peidão", senha="")