from common.holerite import Holerite

class DecimoTerceiro:

    @staticmethod
    def run():
        repetir = True
        while(repetir):

            holerite = Holerite()

            holerite.imprime()

            repetirStr = input("Deseja calcular novamente? (sim/nao) ")
            if(repetirStr == "nao"):
                repetir = False
