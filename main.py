from folhapagamento.fechamentomensal import FechamentoMensal
from decimoterceiro.decimoterceiro import DecimoTerceiro

print("Escolha a funcionalidade abaixo")
print("\t 1) Folha de Pagamento")
print("\t 2) 13º Salário")
print("\t 3) Férias")

try:
    opcao = int(input("Opção: "))
except:
    print("Erro: Para selecionar uma opção, informe um número inteiro.")
    exit()

if(opcao == 1):
    FechamentoMensal.run()
elif(opcao == 2):
    print("Funcionalidade em construção.")
    #DecimoTerceiro.run()
    exit()
elif(opcao == 3):
    print("Funcionalidade em construção.")
    exit()
else:
    print("Valor incorreto.")
    exit()