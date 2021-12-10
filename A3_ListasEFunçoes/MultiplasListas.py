#Declarando arrays
inventario_equip = []
inventario_valor = []
inventario_serial = []
inventario_depto = []

#loop de inserção
resposta = 'S'
while resposta == 'S':
    inventario_equip.append(input("Nome do Equipamento:"))
    inventario_valor.append(float(input("Valor: ")))
    inventario_serial.append(int(input("Código Serial do Equipamento")))
    inventario_depto.append(input("Departamento: "))
    resposta = input("digite S/s caso deseje cadastrar mais!").upper

#chamada geral por array
for elemento in inventario_equip:
    print("nome do Equipamento:" , elemento)
print("#\n#\n?#")
#chamada por indíce
for indice in range(0,len(inventario_equip)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", inventario_equip[indice])
    print("Valor: ", inventario_valor[indice])
    print("Serial: ", inventario_serial[indice])
    print("Departamento: ", inventario_depto[indice])

#Exemplo de Busca
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(inventario_equip)):
  if busca==inventario_equip[indice]:
    print("Valor..: ", inventario_valor[indice])
    print("Serial.:", inventario_serial[indice])

#Situação 1 - Depreciação do Valor
busca=input("Digite o nome do equipamento a depreciar: ")
porcentagem=float(input("digite a porcentagem que o objeto será depreciado: "))
for indice in range(0,len(inventario_equip)):
  if busca==inventario_equip[indice]:
    inventario_valor[indice] = inventario_valor[indice] * (1-(porcentagem/100))

#Situação 2 - Deletar das Listas

busca=int(input("Digite o serial do equipamento a remover: "))
for indice in range(0,len(inventario_equip)):
     if busca == inventario_serial[indice]:
        del inventario_serial[indice]
        del inventario_depto[indice]
        del inventario_equip[indice]
        del inventario_valor[indice]
        break

