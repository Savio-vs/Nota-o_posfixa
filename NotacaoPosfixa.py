class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Pilha:
    def __init__(self):  ## metodo especial. **Pesquisar metodos disponiveis**
        self.head = None
        self._size = 0  ## armazena o tamanho da pilha

    def push(self, elem):  # função de adicição
        item = Node(elem)
        item.next = self.head
        self.head = item
        self._size += 1

    def pop(self):          #função de desempilhamento.
        if self.head:
            item = self.head
            self.head = item.next
            self._size -= 1
            return item.data
        else:
            print("erro fatal 1")
            exit()
    def __sizeof__(self):
        return self._size
    def verif (self):
        item = self.head
        return item.data

parentese = Pilha()
numero = Pilha()
op = Pilha()

expressao = "( ( (2+2) * 5) / (6+1) )"
operando = ""
for i in expressao:
    if i != ' ':
       if i == '(':
           parentese.push(i)
       elif i == ')':
           parentese.pop()
           if operando:
               numero.push(operando)
               operando=""
           v = op.pop()
           numero.push(v)

       elif '0' <= i <= '9' or i == '.':
           operando += i

       elif i == '+' or i == '-' or i == '/' or i == '*':
           op.push(i)
           if operando:
               numero.push(operando)
               operando = ""
    elif operando:
        numero.push(operando)
        operando = ""

lista=[]
if parentese.head == None:
    while(numero.head):
        lista.append(numero.pop())

    lista = list(reversed(lista))
    for cont in lista:
        print(cont, end=" ")
else:
    print("Erro fatal 2")
    exit()

# calculo da notação posfixa
for cont in lista:
    if cont == '+' or cont == '-' or cont == '/' or cont == '*':
        verificar = cont
        if verificar == '+':
            nu2 = parentese.pop()
            nu1 = parentese.pop()
            valor = nu1 + nu2
            #print(valor)
            parentese.push(valor)
        elif verificar == '-':
            nu2 = parentese.pop()
            nu1 = parentese.pop()
            valor = nu1 - nu2
            #print(valor)
            parentese.push(valor)
        elif verificar == '*':
            nu2 = parentese.pop()
            nu1 = parentese.pop()
            valor = nu1 * nu2
            #print(valor)
            parentese.push(valor)
        elif verificar == '/':
            nu2 = parentese.pop()
            nu1 = parentese.pop()
            valor = nu1 / nu2
            #print(valor)
            parentese.push(valor)
    else:
        valor = int(cont)
        parentese.push(valor)

print("\nResultado da Equação é :",end=" ")
print(parentese.pop())
