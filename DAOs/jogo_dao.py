from DAOs.dao import DAO
from entidade.jogo import Jogo

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogos.pkl')
        
    def add(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo) and isinstance(jogo.titulo, str)):
            super().add(jogo.titulo, jogo)

    def update(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Usuario) and isinstance(jogo.titulo, str)):
            super().update(jogo.titulo, jogo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)