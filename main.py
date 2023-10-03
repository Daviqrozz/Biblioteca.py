class Livro:
  def _init_(self,titulo,autor,ano):
    self.titulo = titulo;
    self.autor = autor;
    self.ano = ano;
    self.disponivel = True;


  def _str_(self):
    return f'Livro:{livro1.titulo},ano:{livro1.ano}'

  def emprestar(self):
    if self.disponivel:
        self.disponivel = False
        return True
    else:
        return False
     
class Usuario:
  def _init_(self,id,nome):
    self.id = id;
    self.nome = nome;
    self.livros_emprestados = []

    def _str_(self):
      return f'Usuario:{Usuario.nome}'


  def pegar_emprestado(self,livro):
    if livro.emprestar():
      self.livros_emprestados.append(livro)
      return True
    else:
      return False
      

  def devolver(self,livro):
    if livro in self.devolver_emprestado:
      livro.devolver();
      self.livros_emprestados.remove(livro)
      return True
    else:
      return False

class Biblioteca:

  def _init_(self):
    self.livros = []
    self.usuarios = []

  def adicionar_livro(self,livro):
    self.livros.append(livro)

  def remover_livro(self,livro):
    self.livros.remove(livro)

  def adicionar_usuario(self,usuario):
    self.usuarios.append(usuario)

  def remover_usuario(self,usuario):
    self.usuarios.remove(usuario)
  
  def verificar_disponibilidade(self,titulo):
    pass

  def emprestar_livro(self,titulo):
    pass
  def receber_usuario(self,titulo):
    pass