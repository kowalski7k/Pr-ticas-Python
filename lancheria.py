# Lancheria Kowalski - Python

# Importar "OS" para limpeza de tela
import os

# Início
print("==================================")
print ("⸙          Bem vindo a          ⸙ \n𝑳 𝒂 𝒏 𝒄 𝒉 𝒆 𝒓 𝒊 𝒂  𝑲 𝒐 𝒘 𝒂 𝒍 𝒔 𝒌 𝒊")
print("==================================")

# Mostrar MENU 
def mostrar_menu():
  ("\n         M   E   N   U ") 
  print("\n- PRATOS \n")
  print("1| Hamburguer R$25,00 \n2| Massa carbonara R$18,00 \n3| Strogonoff frango R$23,00 \n4| Strogonoff carne R$23,00 \n5| Batata frita R$15,00 \n")
  print("- BEBIDAS\n")
  print("6| Coca-cola 600ml R$7,00 \n7| Suco de laranja R$5,00 \n8| Água 600ml R$4,00 ")

# Função para calcular o valor total da compra
def calcular_pedidos(pedidos):
  total=0
  for item, quantidade in pedidos.items():
    total += menu[item] * quantidade
  return total

# Função da limpeza de tela
def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\n' * 100)

# Valores MENU
menu = {
  1: 25.00,
  2: 18.00,
  3: 23.00,
  4: 23.00,
  5: 15.00,
  6: 7.00,
  7: 5.00,
  8: 4.00
}
# Pedidos
while True :
  pedidos=  {}
  mostrar_menu()

  while True:
      try:
        escolha = int(input("\nEscolha um item do menu (1-8): "))
        quantidade = int(input("\nQual a quantidade desejada? "))
        if 1 <= escolha <= 8 and quantidade > 0:
          pedidos[escolha]=quantidade
        else :
          print("Escolha inválida. Tente novamente.")
      except ValueError:
        print("Digite um número/escolha válido!")

      mais_pedidos= input("\nDeseja fazer mais um pedido? (s/n): ").lower()
      if mais_pedidos != "s":
        break

# Calcular o valor total da compra
  total = calcular_pedidos(pedidos)
  print("===== TOTAL DO PEDIDO =====")
  print(f"\nTotal: R$ {total:.2f}")

# Fim, caso desejado
  continuar = input("Deseja realizar mais algum pedido? (s/n): ").lower()
  if continuar != "s":
    limpar_tela()
    print("\nObrigado pela sua presença! \nLancheria Kowalski agradece sua preferência!!! \nAté breve ;)")
    break
