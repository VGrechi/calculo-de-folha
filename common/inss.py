class INSS:

    FAIXAS = [1045, 2089, 3134]

    @staticmethod
    def calcular(baseCalculo):
        FAIXAS = INSS.FAIXAS
        teto = 854.15
    
        imposto = 0
        
        if baseCalculo <= FAIXAS[0]:
            imposto = baseCalculo * 0.07
        elif (baseCalculo > FAIXAS[0] and baseCalculo <= FAIXAS[1]):
            imposto =  baseCalculo * 0.09
        elif (baseCalculo > FAIXAS[1] and baseCalculo <= FAIXAS[2]):
            imposto =  baseCalculo * 0.12
        else:
            imposto =  baseCalculo * 0.14

        if imposto > teto: 
            imposto = teto

        return round(imposto, 2)

    @staticmethod
    def calcularRef(baseCalculo):
        FAIXAS = INSS.FAIXAS
        if baseCalculo <= FAIXAS[0]:
            return 7
        elif (baseCalculo > FAIXAS[0] and baseCalculo <= FAIXAS[1]):
            return 9
        elif (baseCalculo > FAIXAS[1] and baseCalculo <= FAIXAS[2]):
            return 12
        else:
            return 14