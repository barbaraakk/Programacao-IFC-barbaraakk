from pessoa import *

lista = []

p1 = Pessoa(nome = "aloi", email = "aloi123@gmail.com", telefone = "123123123")

lista.append(p1)

p2 = Pessoa(nome = "ai", email = "a123@gmail.com", telefone = "13123")

lista.append(p2)

for p in lista:
    print(p)