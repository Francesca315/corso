class Pila:
  def __init__(self):
    self.Elementi = []

  def Push(self, Elemento) :
    self.Elementi.append(Elemento)

  def Pop(self):
    return self.Elementi.pop()

  def EVuota(self):
    return (self.Elementi == [])

 P = Pila()
 P.Push(54)
 P.Push(45)
 P.Push("numeri")
 while not P.EVuota() :
  print P.Pop()