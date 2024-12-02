from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, numero_matricula):
        self.nome = nome
        self.idade = idade
        self.numero_matricula = numero_matricula
    
    @abstractmethod
    def mostrar_informacoes(self):
        pass

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, numero_matricula):
        super().__init__(nome, idade, numero_matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.alterar_disponibilidade()
            print(f"Livro '{livro.titulo}' emprestado para {self.nome}.")
        else:
            print("Não é possível emprestar mais livros.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.alterar_disponibilidade()
            print(f"Livro '{livro.titulo}' devolvido.")
        else:
            print("Livro não está com este usuário.")

    def mostrar_informacoes(self):
        print(f"Usuário: {self.nome}, Livros emprestados: {[livro.titulo for livro in self.livros_emprestados]}")

class Administrador(Pessoa):
    def adicionar_livro(self, livro, biblioteca):
        biblioteca.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def remover_livro(self, livro, biblioteca):
        if livro in biblioteca:
            biblioteca.remove(livro)
            print(f"Livro '{livro.titulo}' removido da biblioteca.")

    def mostrar_informacoes(self):
        print(f"Administrador: {self.nome}")

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def alterar_disponibilidade(self):
        self.disponivel = not self.disponivel

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor, ano_publicacao)

biblioteca = []
admin = Administrador("Alice", 30, 1)
usuario = UsuarioComum("Bob", 20, 2)
livro1 = Livro("Python para Todos", "Autor A", 2021)

admin.adicionar_livro(livro1, biblioteca)
usuario.emprestar_livro(livro1)
usuario.mostrar_informacoes()
usuario.devolver_livro(livro1)
