
def rigistrar_vendas (vendas):
  dia = int(input("digite o dia (1 a 30 ):"))
  valor = int(input("digite o valor da venda :")
vendas [dia - 1] = valor

def mostrar_vendas (vendas):
  for i in range(30)
    print("dai", i + 1,"=", vendas [i]

def media_venda (vendas):
  soma=0
  for i in range(0,30):
    soma += vendas [i]
    print("vendas:" , soma / 30)
    
  def maior_venda(venda):
    maior = vendas [0]
    for i in range (30):
      maior = vendas [i]
      print("maior venda:", maior )

def menu():
  print("1 - registra venda")
  print("2 - mostrar vendas")
  print("3 - media das vendas")
  print("4 - maior venda")
  print("5 - sair")
        
    return int(input("opção"))
    
  vendas = [0] * 30
  opcao = 0

while opcao != 5 
  opcao = menu()

  if opcao == 1:
    registrar_vendas (vendas)
    
elif opcao == 2:
  mostrar_vendas (vendas)

elif opcao == 3:
media_das_vendas(vendas)

elif opcao == 4:
maior_venda(vendas)

elif opcao == 5:
print("sair")

else:
print("erro")
    
  
