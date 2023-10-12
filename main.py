class Livro:
  def _init_(self,titulo,autor,ano):
    self.titulo = titulo;
    self.autor = autor;
    self.ano = ano;
    self.disponivel = True;

  def emprestar(self):
    if self.disponivel:
        self.disponivel = False
        return True
    else:
        return False

  def _str_(self):
    return f'Livro:{livro.titulo},autor{livro.autor},ano:{livro.ano}'
     
class Usuario:
  def _init_(self,id,nome):
    self.id = id;
    self.nome = nome;
    self.livros_emprestados = []

  def _str_(self):
    return f'Usuario de nome:{usuario.nome} '

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

  def mostrar_livros(self):
    for livro in self.livros:
      print(livro.titulo)

  def remover_livro(self,livro):
    self.livros.remove(livro)

  def adicionar_usuario(self,usuario):
    self.usuarios.append(usuario)

  def remover_usuario(self,usuario):
    self.usuarios.remove(usuario)
  
  def verificar_disponibilidade(self,titulo):
    for livro in self.livros:
      if livro.titulo == titulo and livro.disponivel:
        return True
      return False

  def emprestar_livro(self,usuario,titulo):
    if not self.verificar_disponibilidade(titulo):
      print(f'Livro:{titulo},nao esta disponivel')

    for livro in self.livros:
      if livro.titulo == titulo and livro.disponivel:
        if usuario.pegar_emprestado(livro):
         print(f'O livro:{titulo} foi emprestado para {usuario.nome}')
         return True
        
  def receber_livro_devolvido(self,usuario,titulo):
    for livro in usuario.livros_emprestados:
      if livro.titulo == titulo:
        if usuario.devolver(livro):
          print(f'O livro {titulo} foi devolvido')
          return True
    print(f'Livro:{titulo} nao foi encontrado')
