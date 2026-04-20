# model.py
class ModuloLivraria:
    def __init__(self):
        # Simula o banco de dados da imagem
        self.acervo = []

    def registrar_livro(self, titulo, autor):
        if titulo and autor:
            livro = {"titulo": titulo, "autor": autor}
            self.acervo.append(livro)

    def consultar_acervo(self):
        return self.acervo