import random
 #n1 = int(input("Digite um numero:"))
 #n2 = int(input("Digite outro Numero"))
 #n3 = int(input("Digite outro Numero"))
 #lista [n1, n2, n3]
 #print("O maior valor foi: {}".format(random.radiant(>)))
a1 = str(input("Digite o nome do aluno:"))
a2 = str(input("Digite outro nome do aluno:"))
a3 = str(input("Digite outro nome do aluno:"))
a4 = str(input("Digite outro nome do aluno:"))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem das apresentações é {}".format(lista))