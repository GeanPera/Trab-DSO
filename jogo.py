from usuario import Usuario

class Jogo():
    def __init__(self, titulo: str, genero, desenvolvedora, faixa_etaria: int, descricao: str, preco: int, qntd_vendida: int):
        self.__titulo = titulo
        self.__genero = genero
        self.__desenvolvedora = desenvolvedora
        self.__faixa_etaria = faixa_etaria
        self.__descicao = descricao
        self.__preco = preco
        self.__qntd_vendida = qntd_vendida

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def desenvolvedora(self):
        return self.__desenvolvedora

    @desenvolvedora.setter
    def desenvolvedora(self, desenvolvedora):
        self.__desenvolvedora = desenvolvedora

    @property
    def faixa_etaria(self):
        return self.__faixa_etaria

    @faixa_etaria.setter
    def faixa_etaria(self, faixa_etaria):
        self.__faixa_etaria = faixa_etaria

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def qntd_vendida(self):
        return self.__qntd_vendida

    @qntd_vendida.setter
    def qntd_vendida(self, qntd_vendida):
        self.__qntd_vendida = qntd_vendida

    def comprar(self, usuario):
        if usuario.perfil.descontar_saldo(self.__preco):
            self.__qntd_vendida += 1
            usuario.biblioteca.adicionar_jogo(self)
            print(f'Compra realizada com sucesso! O jogo {self.__titulo} está disponível em sua biblioteca. Seu saldo atual é R${usuario.perfil.saldo}')

    def presentear_amigo(self, usuario, Usuario):
        if usuario.perfil.descontar_saldo(self.__preco):
            Usuario.biblioteca.adicionar_jogo(self)
            print(f'Compra realizada com sucesso! Você presenteou {Usuario.nickname} com o jogo {self.__titulo}. Seu saldo atual é R${usuario.perfil.saldo}')
