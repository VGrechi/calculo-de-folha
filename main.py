from folhapagamento.fechamentomensal import FechamentoMensal
from decimoterceiro.decimoterceiro import DecimoTerceiro
from ferias.ferias import Ferias

print("Escolha a funcionalidade abaixo")
print("\t (1) Folha de Pagamento")
print("\t (2) 13º Salário")
print("\t (3) Férias")
print("\t (0) SAIR")

try:
    opcao = int(input("Opção: "))
except:
    print("Erro: Para selecionar uma opção, informe um número inteiro.")
    exit()

if(opcao == 1):
    FechamentoMensal.run()
elif(opcao == 2):
    DecimoTerceiro.run()
elif(opcao == 3):
    Ferias.run()
elif(opcao == 0):
    exit()
else:
    print("Valor incorreto.")
    exit()