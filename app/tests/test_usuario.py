import pytest

from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("joão", "peidão", "123")

def test_nome_invalido(usuario_valido):
    with pytest.raises(TypeError, match="o nome deve ser um texto"):
        Usuario(13, "peidão", "123")