class AdicionalNoturno:

    @staticmethod
    def calcular(baseCalculo, cargaSemanal, quantHAN):
         valorHora = baseCalculo / (cargaSemanal * 5)
         return valorHora * quantHAN * 1.2