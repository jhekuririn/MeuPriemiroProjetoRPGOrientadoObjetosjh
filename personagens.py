import random 

#classe ou super classe pai
class Personagem():

  #construtor
  def  __init__(self, nome: str, classe: str, vida: int, ataque: int):
    self.nome: str = nome 
    self.classe: str =  classe
    self.vida: int = vida
    self.ataque: int = ataque
 
  def atacar(self, alvo):
    dano = random.randint(1, self.ataque)
    alvo.receber_dano(dano)
    print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")

  def receber_dano (self, dano: int):
    self.vida -= dano

  def estar_vivo(self):
    return self.vida > 0


class Paladino(Personagem):
  def __init__(self, nome):
    super().__init__(nome, "paladino", 100, 20)

class Mago(Personagem):
  def __init__(self, nome):
    super().__init__(nome, "Elfo", 90, 25)  

class Elfo(Personagem):
  def __init__(self, nome):
   super().__init__(nome, "Mago", 80, 30)  

class Humano(Personagem):
  def __init__(self, nome):
    super().__init__(nome, "Humano", 110, 18)

class Orc(Personagem):
  def __init__(self, nome):
    super().__init__(nome, "Orc", 150, 15)  